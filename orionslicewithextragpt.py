Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import librosa
import librosa.display
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from pydub import AudioSegment
... 
... class OrionSlice:
...     def __init__(self, audio_path):
...         self.audio_path = audio_path
...         self.y, self.sr = librosa.load(audio_path, sr=None)
...         self.slices = []
... 
...     def auto_chop(self, method='onset', n_slices=16):
...         """ Auto-detects and slices audio based on selected method. """
...         if method == 'onset':
...             onset_frames = librosa.onset.onset_detect(y=self.y, sr=self.sr, backtrack=True)
...             self.slices = librosa.frames_to_samples(onset_frames)
...         elif method == 'fixed':
...             self.slices = np.linspace(0, len(self.y), n_slices, dtype=int)
...         return self.slices
... 
...     def save_slices(self, output_folder="slices"):
...         """ Saves detected slices as separate WAV files. """
...         for i, start in enumerate(self.slices[:-1]):
...             end = self.slices[i+1]
...             slice_audio = self.y[start:end]
...             sf.write(f"{output_folder}/slice_{i}.wav", slice_audio, self.sr)
... 
...     def plot_waveform(self):
...         """ Plots waveform with detected slice points. """
...         plt.figure(figsize=(12, 4))
...         librosa.display.waveshow(self.y, sr=self.sr)
...         plt.vlines(librosa.samples_to_time(self.slices), ymin=-1, ymax=1, color='r', linestyle='dashed')
...         plt.title("Orion Slice - Auto Chop Preview")
...         plt.show()
... 
... # Example Usage
... audio_path = "your_audio_file.wav"
... orion = OrionSlice(audio_path)
... orion.auto_chop(method='onset')
... orion.plot_waveform()
... orion.save_slices()
