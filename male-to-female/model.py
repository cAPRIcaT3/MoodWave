import torch
import torchaudio
import matplotlib.pyplot as plt

def plot_spectrogram(spec, title="Spectrogram"):
    plt.figure(figsize=(12, 4))
    plt.imshow(spec[0].numpy(), cmap='viridis', aspect='auto', origin='lower')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.colorbar(format="%+2.0f dB")
    plt.show()

def main():
    # Replace 'your_audio_file.wav' with the path to your audio file
    audio_file_path = 'your_audio_file.wav'

    # Load the audio file
    waveform, sample_rate = torchaudio.load(audio_file_path)

    # Apply a short-time Fourier transform (STFT) to compute spectrogram
    specgram = torchaudio.transforms.MelSpectrogram()(waveform)

    # Plot the spectrogram
    plot_spectrogram(specgram, title="Mel Spectrogram")

if __name__ == "__main__":
    main()
