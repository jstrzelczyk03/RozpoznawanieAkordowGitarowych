import math
import numpy as np
import pyaudio
import matplotlib.pyplot as plt


class AudioRecord:
    def __init__(self, buffer_size=1024, sample_rate=44000):
        self.buffer_size = buffer_size
        self.sample_rate = sample_rate
        self.data = []
        self.is_recording = False
        self.p = pyaudio.PyAudio()
        self.stream = None

    def _callback(self, in_data, frame_count, time_info, status):
        audio_data = np.frombuffer(in_data, dtype=np.int16)
        self.data.extend(audio_data)
        return in_data, pyaudio.paContinue

    def start_recording(self):
        self.is_recording = True
        print("Recording started...")
        self.data = []
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


# Nalozenie okna hamminga na sygnal
def hammingWindow(data, size):
    hamming_window = np.hamming(size)
    result = data * hamming_window
    return result


if __name__ == "__main__":
    audio_recorder = AudioRecord()
    audio_recorder.start_recording()
    input("Press Enter to stop recording...")
    audio_recorder.stop_recording()

    samples_signal = np.array(audio_recorder.data)

    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(len(samples_signal)) / audio_recorder.sample_rate, samples_signal)
    plt.title('Recorded Audio Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

    for i in range(len(samples_signal)):
        if math.fabs(samples_signal[i]) < 500:
            samples_signal[i] = 0

    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(len(samples_signal)) / audio_recorder.sample_rate, samples_signal)
    plt.title('Recorded Audio Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

    samples_signal = hammingWindow(samples_signal, len(samples_signal))

    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(len(samples_signal)) / audio_recorder.sample_rate, samples_signal)
    plt.title('Recorded Audio Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()


    #
    # # plt.figure(figsize=(10, 6))
    # # plt.plot(np.arange(len(samples_signal)) / audio_recorder.sample_rate, samples_signal)
    # # plt.title('Recorded Audio Signal with Hamming Window')
    # # plt.xlabel('Time (s)')
    # # plt.ylabel('Amplitude')
    # # plt.show()
    #
    # FFT of the Signal
    def plot_fft(signal, sample_rate):
        fft_result = np.fft.fft(signal)
        frequencies = np.fft.fftfreq(len(fft_result), d=1 / sample_rate)

        positive_frequencies = frequencies[:len(frequencies) // 2]
        magnitude_spectrum = np.abs(fft_result[:len(fft_result) // 2])

        plt.figure(figsize=(10, 6))
        plt.plot(positive_frequencies, magnitude_spectrum)
        plt.title('FFT of the Signal')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude')
        plt.show()

        # Sorting frequencies by amplitude from highest to lowest
        top_indices = np.argsort(magnitude_spectrum)[::-1]
        top_frequencies = positive_frequencies[top_indices]

        # Filtering frequencies below 375 Hz
        top_frequencies = [freq for freq in top_frequencies if (375 >= freq >= 70)]

        filtered_frequencies = [top_frequencies[0]]

        for freq in top_frequencies[1:]:
            if_add = True
            for i in range(len(filtered_frequencies)):
                if abs(filtered_frequencies[i] - freq) <= 20:
                    if_add = False
            if if_add:
                filtered_frequencies.append(freq)
                if len(filtered_frequencies) == 6:
                    break
        print(f"\nZnalezione częstotliwości: {filtered_frequencies}")
        return filtered_frequencies


    #
    def recognize_chord(filtered_frequences):
        with open("database.txt", "r") as file:
            list_of_complient = []
            numer_of_compliant = 0
            content = file.read()
            chords = content.split("\n")
            for i in range(len(chords)):
                chords[i] = chords[i].split(",")

            for chord in chords:
                for freq in filtered_frequences:
                    for c in chord[1:]:
                        if math.fabs(float(c) - freq) < 4:
                            numer_of_compliant += 1

                list_of_complient.append(numer_of_compliant)
                numer_of_compliant = 0
            # print(list_of_complient)
            # print(chords)

            max = list_of_complient[0]
            index = 0
            for n in list_of_complient:
                if n > max:
                    max = n
                    index = list_of_complient.index(n)
            print(f"Znaleziony akord {chords[index][0]}")


    recognize_chord(plot_fft(samples_signal, audio_recorder.sample_rate))
