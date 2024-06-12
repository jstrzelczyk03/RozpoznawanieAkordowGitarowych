import pyaudio
import numpy as np
import json
from tensorflow.keras.models import load_model
import librosa
import librosa.feature
import threading
import time
from queue import Queue
from Sieci_neuronowe.GUI.gui import update_chord_image, start_gui, toggle_state


# Nowe funkcje
def extract_stft_features(audio_data, sr, n_fft=2048, hop_length=512):
    stft = librosa.stft(audio_data, n_fft=n_fft, hop_length=hop_length)
    stft_magnitude, _ = librosa.magphase(stft)
    return stft_magnitude


def classify_strum_direction(stft_features):
    num_frames = stft_features.shape[1]
    mid_point = num_frames // 2

    lower_band_first_half = stft_features[0:len(stft_features) // 2, :mid_point]
    lower_band_second_half = stft_features[0:len(stft_features) // 2, mid_point:]

    upper_band_first_half = stft_features[len(stft_features) // 2:, :mid_point]
    upper_band_second_half = stft_features[len(stft_features) // 2:, mid_point:]

    lower_band_energy_first_half = lower_band_first_half.sum(axis=0)
    lower_band_energy_second_half = lower_band_second_half.sum(axis=0)

    upper_band_energy_first_half = upper_band_first_half.sum(axis=0)
    upper_band_energy_second_half = upper_band_second_half.sum(axis=0)

    lower_band_energy_diff = lower_band_energy_second_half.mean() - lower_band_energy_first_half.mean()
    upper_band_energy_diff = upper_band_energy_second_half.mean() - upper_band_energy_first_half.mean()

    if lower_band_energy_diff > 0 and upper_band_energy_diff > 0:
        return "down"
    elif lower_band_energy_diff < 0 and upper_band_energy_diff < 0:
        return "up"
    else:
        return "uncertain"


chord_label = None
MODEL_PATH = "model.h5"
model = load_model(MODEL_PATH)
DATA_PATH = "data.json"
with open(DATA_PATH, "r") as file:
    data = json.load(file)


def calculate_pcp(audio_data, sr):
    chroma = librosa.feature.chroma_stft(y=audio_data, sr=sr)
    chroma_norm = librosa.util.normalize(chroma)
    pcp = np.mean(chroma_norm, axis=1)
    return pcp


def classify_buffer(buffer, rate, queue):
    audio_data = np.frombuffer(buffer, dtype=np.int16).astype(np.float32) / np.iinfo(np.int16).max
    pcp = calculate_pcp(audio_data, rate)
    pcp = pcp[np.newaxis, ..., np.newaxis]
    predictions = model.predict(pcp)

    new_chord_label = np.argmax(predictions)
    confidence = np.max(predictions)

    # Extract STFT features and classify strum direction
    stft_features = extract_stft_features(audio_data, rate)
    strum_direction = classify_strum_direction(stft_features)

    if confidence >= 0.97 and new_chord_label != 20:
        chord = data['mapping'][new_chord_label]
        lower_band_energy_diff = stft_features[0:len(stft_features) // 2,
                                 :stft_features.shape[1] // 2].sum() - stft_features[0:len(stft_features) // 2,
                                                                       stft_features.shape[1] // 2:].sum()
        upper_band_energy_diff = stft_features[len(stft_features) // 2:,
                                 :stft_features.shape[1] // 2].sum() - stft_features[len(stft_features) // 2:,
                                                                       stft_features.shape[1] // 2:].sum()
        print(f"Identified chord: {chord} with confidence: {confidence}, Strum direction: {strum_direction}")
        print(
            f"Lower band energy difference: {lower_band_energy_diff}, Upper band energy difference: {upper_band_energy_diff}")
        queue.put((chord, strum_direction))


def list_microphones():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if (p.get_device_info_by_index(i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_index(i).get('name'))
    p.terminate()


def select_microphone():
    list_microphones()
    index = int(input("Wybierz indeks urządzenia do używania: "))
    return index


def record_and_classify(mic_index, queue):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 16000
    RECORD_SECONDS = 80
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=mic_index)
    print("* Recording and classifying...")
    try:
        while toggle_state.is_set():
            buffer = stream.read(CHUNK, exception_on_overflow=False)
            classify_buffer(buffer, RATE, queue)
    except Exception as e:
        print(f"Recording error: {e}")
    finally:
        print("* Done.")
        stream.stop_stream()
        stream.close()
        p.terminate()


def start_recording(mic_index, queue):
    if toggle_state.is_set():
        recording_thread = threading.Thread(target=record_and_classify, args=(mic_index, queue))
        recording_thread.start()
    else:
        print("Recording is not started because toggle_state is not set.")


def process_queue(queue):
    try:
        while True:
            chord, strum_direction = queue.get_nowait()
            update_chord_image(chord, strum_direction)
    except Exception as e:
        pass
    window.after(100, process_queue, queue)


if __name__ == "__main__":
    mic_index = select_microphone()
    input("Press Enter to start GUI...")

    # Utwórz kolejkę
    queue = Queue()

    # Uruchomienie GUI
    global window
    window = start_gui()
    window.after(100, process_queue, queue)


    # Uruchomienie monitorowania stanu toggle_state i nagrywania
    def monitor_toggle_state():
        while True:
            if toggle_state.is_set():
                start_recording(mic_index, queue)
                while toggle_state.is_set():
                    time.sleep(0.1)
            time.sleep(0.1)


    monitor_thread = threading.Thread(target=monitor_toggle_state, daemon=True)
    monitor_thread.start()

    window.mainloop()
