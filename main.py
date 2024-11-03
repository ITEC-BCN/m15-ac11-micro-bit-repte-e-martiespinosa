from microbit import *

x = 0
y = 0

def on_forever():
    temperatura_actual = input.temperature()
    temperatura_maxima = 50
    basic.clear_screen()
    led.plot_bar_graph(temperatura_actual, temperatura_maxima)

    img = images.create_image("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    img.set_pixel(x, y, True)
    img.show_image(0)

    acc_x = input.acceleration(Dimension.X)
    acc_y = input.acceleration(Dimension.Y)

    global x, y
    if acc_x <= 150 and x > 0:
        x -= 1
    if acc_x > 150 and x < 4:
        x += 1
    if acc_y <= 150 and y > 0:
        y -= 1
    if acc_y > 150 and y < 4:
        y += 1

basic.forever(on_forever)
