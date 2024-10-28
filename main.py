from microbit import *

def mostrar_temperatura():
    temperatura_actual = input.temperature()
    temperatura_maxima = 30
    basic.clear_screen()
    led.plot_bar_graph(temperatura_actual, temperatura_maxima)

mostrar_temperatura()
