import pyaudio
import numpy as np
import json
from tensorflow.keras.models import load_model
import librosa
import librosa.feature

chord_label = None

# Import the trained model (Update the MODEL_PATH to the location of your Keras model)
MODEL_PATH = "model.h5"
model = load_model(MODEL_PATH)

# Load training data to get the mapping of labels
DATA_PATH = "data.json"
with open(DATA_PATH, "r") as file:
    data = json.load(file)

# chord_label = None

def calculate_pcp(audio_data, sr):
    # Zakładając, że audio_data to już przetworzona tablica NumPy z danymi audio
    # i sr to częstotliwość próbkowania

    # Bezpośrednie przekazanie danych audio i sr do funkcji librosa
    chroma = librosa.feature.chroma_stft(y=audio_data, sr=sr)

    chroma_norm = librosa.util.normalize(chroma)
    pcp = np.mean(chroma_norm, axis=1)

    return pcp

def classify_buffer(buffer, rate):
    global chord_label
    # Convert buffer to float32 and normalize
    audio_data = np.frombuffer(buffer, dtype=np.int16).astype(np.float32) / np.iinfo(np.int16).max

    # Pass the audio data to calculate_pcp
    pcp = calculate_pcp(audio_data, rate)
    pcp = pcp[np.newaxis, ..., np.newaxis]  # Reshape for the model if needed

    # Use the model to predict
    predictions = model.predict(pcp)
    new_chord_label = np.argmax(predictions)
    confidence = np.max(predictions)
    if confidence >= 0.95 and new_chord_label != 20:
        # if new_chord_label == chord_label:
        print(f"Identified chord: {data['mapping'][new_chord_label]} with confidence: {confidence}")
        # chord_label = new_chord_label

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

def record_and_classify(mic_index):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 8192
    RECORD_SECONDS = 50

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=mic_index)  # Ustawienie wybranego mikrofonu

    print("* Recording and classifying...")
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        buffer = stream.read(CHUNK, exception_on_overflow=False)
        classify_buffer(buffer, RATE)

    print("* Done.")
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    mic_index = select_microphone()
    input("Press Enter to start recording...")
    record_and_classify(mic_index)