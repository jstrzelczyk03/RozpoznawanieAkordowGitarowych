import math
import pyaudio
import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

class AudioRecord:
    def __init__(self, buffer_size=1024, sample_rate=16384):
        self.buffer_size = buffer_size
        self.sample_rate = sample_rate
        self.data = []
        self.is_recording = False
        self.p = pyaudio.PyAudio()
        self.stream = None

    def _callback(self, in_data, frame_count, time_info, status):
        audio_data = np.frombuffer(in_data, dtype=np.int16)
        self.data.extend(audio_data)
        return (in_data, pyaudio.paContinue)

    def start_recording(self):
        self.is_recording = True
        print("Recording started...")
        self.data = []  # Clear previous data
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=self.sample_rate,
                                  input=True,
                                  stream_callback=self._callback)
        self.stream.start_stream()

    def stop_recording(self):
        self.is_recording = False
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        print("Recording stopped.")


def hammingWindow(data, size, j):
    result = []
    for i in range(j * size, (j + 1) * size):
        result.append(data[i] * 0.5 * (1.0 - math.cos(2.0 * math.pi * i / (size - 1))))
    return result


def find_max_frequency(signal_samples, sample_rate):
    fft_result = fft(signal_samples)
    frequencies = np.fft.fftfreq(len(fft_result), d=1 / sample_rate)
    print(frequencies)
    positive_frequencies = frequencies[:len(frequencies) // 2]
    max_amplitude_index = np.argmax(np.abs(fft_result[:len(fft_result) // 2]))
    print(max_amplitude_index)
    max_frequency = positive_frequencies[max_amplitude_index]
    return abs(max_frequency)


if __name__ == "__main__":
    audio_recorder = AudioRecord()
    audio_recorder.start_recording()
    input("Press Enter to stop recording...")
    audio_recorder.stop_recording()

    for i in range(len(audio_recorder.data)):
        audio_recorder.data[i] = abs(audio_recorder.data[i])

    for i in range(len(audio_recorder.data)):
        if audio_recorder.data[i] < 100:
            audio_recorder.data[i] = 0

    print("Recorded samples:", audio_recorder.data)

    size_hamming = 4096
    new_data = hammingWindow(audio_recorder.data, size_hamming, 0)

    max_frequency = find_max_frequency(new_data, 4096)
    print("Max Frequency:", max_frequency)

    # Wykres FFT
    plt.figure(figsize=(10, 6))
    plt.plot(np.fft.fftfreq(size_hamming, d=1 / audio_recorder.sample_rate)[:size_hamming // 2],
             np.abs(fft(new_data))[:size_hamming // 2])
    plt.title('FFT of the Audio Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.show()

    # Wczytaj dane audio
    audio_samples = audio_recorder.data

    # Stworzenie wektora czasu dla próbek audio
    time_vector = np.arange(0, len(audio_samples)) / audio_recorder.sample_rate

    # Wykres amplitudy próbek
    plt.figure(figsize=(10, 6))
    plt.plot(time_vector, audio_samples)
    plt.title('Amplitude of Audio Samples')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()
