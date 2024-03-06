import json
import os
import librosa
import librosa.feature
import numpy as np

DATASET_PATH = "Resources/Chords"
JSON_PATH = "data.json"
SAMPLE_RATE = 22050


# def calculate_pcp(file_path):
#     # Wczytanie sygnału dźwiękowego
#     y, sr = librosa.load(file_path)
#
#
#     # Ekstrakcja cech dźwiękowych
#     chroma = librosa.feature.chroma_stft(y=y, sr=sr)
#
#     # Normalizacja cech do przedziału [0, 1]
#     chroma_norm = librosa.util.normalize(chroma)
#
#     # Obliczenie średniej po czasie, aby uzyskać profil pcp
#     pcp = np.mean(chroma_norm, axis=1)
#
#     return pcp

def calculate_pcp(audio_data, sr):
    # Zakładając, że audio_data to już przetworzona tablica NumPy z danymi audio
    # i sr to częstotliwość próbkowania

    # Bezpośrednie przekazanie danych audio i sr do funkcji librosa
    chroma = librosa.feature.chroma_stft(y=audio_data, sr=sr)

    chroma_norm = librosa.util.normalize(chroma)
    pcp = np.mean(chroma_norm, axis=1)

    return pcp


# def save_pcp(dataset_path, json_path):
#     # Dictionary to store data
#     data = {
#         "mapping": [],
#         "pcp": [],
#         "labels": []
#     }
#
#     # Loop through all
#     for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
#
#         # Ensure that we are not at the root (dataset) level
#         if dirpath is not dataset_path:
#
#             # Save the semantic label
#             semantic_label = dirpath.split("\\")[-1]  # Changed backslash to forward slash for compatibility
#             data["mapping"].append(semantic_label)
#             print("\nProcessing {}".format(semantic_label))
#
#             # Process files for a specific chord
#             for f in filenames:
#                 # Load audio file
#                 file_path = os.path.join(dirpath, f)
#
#                 pcp = calculate_pcp(file_path)
#
#
#                 data["pcp"].append(pcp.tolist())
#                 data["labels"].append(i - 1)
#
#     with open(json_path, "w") as file:
#         json.dump(data, file, indent=4)
#
#
# save_pcp(dataset_path=DATASET_PATH, json_path=JSON_PATH)

# calculate_pcp("Resources/Chords/a/a1.wav")
