from microbit import *

modo = ""
x = 0
y = 0

def on_button_pressed_a():
    global modo
    modo = "estacio_meteorologica"

def on_button_pressed_b():
    global modo
    modo = "moure_la_gota"

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

def estacio_meteorologica():
    temperatura_actual = input.temperature()
    temperatura_maxima = 50
    basic.clear_screen()
    led.plot_bar_graph(temperatura_actual, temperatura_maxima)

def moure_la_gota():
    global x, y

    img = images.create_image("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    img.set_pixel(x, y, True)
    img.show_image(0)

    acc_x = input.acceleration(Dimension.X)
    acc_y = input.acceleration(Dimension.Y)

    if acc_x <= 150 and x > 0:
        x -= 1
    if acc_x > 150 and x < 4:
        x += 1
    if acc_y <= 150 and y > 0:
        y -= 1
    if acc_y > 150 and y < 4:
        y += 1

def on_forever():
    if modo == "estacio_meteorologica":
        estacio_meteorologica()
    elif modo == "moure_la_gota":
        moure_la_gota()
basic.forever(on_forever)
