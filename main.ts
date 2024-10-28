function mostrar_temperatura() {
    let temperatura_actual = input.temperature()
    let temperatura_maxima = 30
    basic.clearScreen()
    led.plotBarGraph(temperatura_actual, temperatura_maxima)
}

mostrar_temperatura()
