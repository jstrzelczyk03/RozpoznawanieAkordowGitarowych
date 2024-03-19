import pyaudio
import numpy as np
import json
from tensorflow.keras.models import load_model
from preprocess import calculate_pcp


chord_label = None

# Import the trained model (Update the MODEL_PATH to the location of your Keras model)
MODEL_PATH = "model.h5"
model = load_model(MODEL_PATH)

# Load training data to get the mapping of labels
DATA_PATH = "data.json"
with open(DATA_PATH, "r") as file:
    data = json.load(file)


# chord_label = None

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
    if confidence >= 0.985 and new_chord_label != 10:
        # if new_chord_label == chord_label:
        print(f"Identified chord: {data['mapping'][new_chord_label]} with confidence: {confidence}")
        # chord_label = new_chord_label


def record_and_classify():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 8192  # Adjusted for more frequent predictions
    RECORD_SECONDS = 50  # Reduced for quicker testing

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* Recording and classifying...")
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        buffer = stream.read(CHUNK, exception_on_overflow=False)
        classify_buffer(buffer, RATE)

    print("* Done.")

    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    input("Press Enter to start recording...")
    record_and_classify()
