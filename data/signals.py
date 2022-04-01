import os
import numpy as np
import matplotlib.pyplot as plt
import datetime

class SineWave:
    """
    Creates a sine waveform Asin(wt+phi) where A is amplitude, w is frequency and phi is phase
    """
    def __init__(self, amplitude, freq, num_samples=1000, phase=0, start_time=0, end_time=10):
        self.amplitude = amplitude
        self.freq = freq
        self.num_samples = num_samples
        self.phase = phase
        self.time_vals = np.arange(start_time, end_time, (end_time - start_time) / self.num_samples)
        self.data_pts = self.amplitude * np.sin(self.freq * self.time_vals + self.phase)

    def get_graph(self, figure, show_grid=False, save=False):
        figure.add_subplot(1, 1, 1)
        plt.plot(self.time_vals, self.data_pts)
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.grid(show_grid)
        plt.title(f"{str(self.amplitude)}sin({str(self.freq)}t+{str(round(self.phase,3))})", size=16)
        save_dir = os.getcwd() + "graphs/"
        if save:
            plt.savefig(save_dir + "sine_signal_" + datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png")
        return figure

class CosWave:
    """
    Creates a cosine waveform Acos(wt+phi) where A is amplitude, w is frequency and phi is phase
    """
    def __init__(self, amplitude, freq, num_samples=1000, phase=0, start_time=0, end_time=10):
        self.amplitude = amplitude
        self.freq = freq
        self.num_samples = num_samples
        self.phase = phase
        self.time_vals = np.arange(start_time, end_time, (end_time - start_time) / self.num_samples)
        self.data_pts = self.amplitude * np.cos(self.freq * self.time_vals + self.phase)

    def get_graph(self, figure, show_grid=False, save_graph=False):
        figure.add_subplot(1, 1, 1)
        plt.plot(self.time_vals, self.data_pts)
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.grid(show_grid)
        plt.title(f"{str(self.amplitude)}cos({str(self.freq)}t+{str(round(self.phase,3))})", size=16)
        save_dir = os.getcwd() + "graphs/"
        if save_graph:
            plt.savefig(save_dir + "cosine_signal_" + datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png")
        return figure

class SincWave:
    """
    Creates a sinc waveform Asinc(At) where A is amplitude which can also be used to simulate 
    nascent Dirac delta function with large A
    """
    def __init__(self, amplitude, num_samples=1000, start_time=0, end_time=10):
        self.amplitude = amplitude
        self.num_samples = num_samples
        self.time_vals = np.arange(start_time, end_time, (end_time - start_time) / self.num_samples)
        self.data_pts = self.amplitude * np.sinc(self.amplitude * self.time_vals)

    def get_graph(self, figure, show_grid=False, save_graph=False):
        figure.add_subplot(1, 1, 1)
        plt.plot(self.time_vals, self.data_pts)
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.grid(show_grid)
        plt.title(f"{str(self.amplitude)}sinc({str(self.amplitude)}t)", size=16)
        save_dir = os.getcwd() + "graphs/"
        if save_graph:
            plt.savefig(save_dir + "sinc_signal_" + datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png")
        return figure

# class RectPulse:
#     """
#     """

# class RectWave:
#     """
#     """

if __name__ == "__main__":
    my_sine = SincWave(amplitude=100, start_time=-5, end_time=5)
    fig_size = (10, 5)
    f = plt.figure(figsize=fig_size)
    graph = my_sine.get_graph(f, save_graph=True)
