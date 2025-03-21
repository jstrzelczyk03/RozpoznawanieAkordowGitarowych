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
    if confidence >= 0.97 and new_chord_label != 20:
        chord = data['mapping'][new_chord_label]
        print(f"Identified chord: {chord} with confidence: {confidence}")
        queue.put(chord)

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
            chord = queue.get_nowait()
            update_chord_image(chord)
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