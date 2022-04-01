from py_dsp.data.signals import SincWave
import matplotlib.pyplot as plt

def run():
    my_sine = SincWave(amplitude=100, start_time=-5, end_time=5)
    fig_size = (10, 5)
    f = plt.figure(figsize=fig_size)
    graph = my_sine.get_graph(f, save_graph=True)
