from microbit import *

def on_forever():
    temperatura_actual = input.temperature()
    temperatura_maxima = 30
    basic.clear_screen()
    led.plot_bar_graph(temperatura_actual, temperatura_maxima)

basic.forever(on_forever)
