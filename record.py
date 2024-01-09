import pyaudio
import numpy as np

class AudioRecord:
    def __init__(self, buffer_size=1024, sample_rate=16000):
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


if __name__ == "__main__":
    audio_recorder = AudioRecord()
    audio_recorder.start_recording()
    input("Press Enter to stop recording...")
    audio_recorder.stop_recording()

    size = len(audio_recorder.data)

    for i in range(size):
        if audio_recorder.data[i] < 0:
            audio_recorder.data[i] *= -1
    print("Recorded samples:", audio_recorder.data)




