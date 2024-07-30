import numpy as np
import matplotlib.pyplot as plt

def generate_signal(f1, f2, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    return t, signal

def compute_fft(signal, sampling_rate):
    N = len(signal)
    fft_result = np.fft.fft(signal)
    fft_freq = np.fft.fftfreq(N, 1 / sampling_rate)
    fft_magnitude = np.abs(fft_result) / N  # Normalize the magnitude
    return fft_freq[:N // 2], fft_magnitude[:N // 2]

def plot_signal_and_fft(t, signal, fft_freq, fft_magnitude):
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    plt.plot(t, signal)
    plt.title('Time Domain Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

    plt.subplot(1, 2, 2)
    plt.plot(fft_freq, fft_magnitude)
    plt.title('Frequency Domain Signal')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')

    plt.tight_layout()
    plt.show()

f1 = 50
f2 = 120
sampling_rate = 1000  # 1 kHz
duration = 1  # 1 second

t, signal = generate_signal(f1, f2, sampling_rate, duration)

fft_freq, fft_magnitude = compute_fft(signal, sampling_rate)

plot_signal_and_fft(t, signal, fft_freq, fft_magnitude)
