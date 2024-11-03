let modo = ""
let x = 0
let y = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    modo = "estacio_meteorologica"
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    modo = "moure_la_gota"
})
function estacio_meteorologica() {
    let temperatura_actual = input.temperature()
    let temperatura_maxima = 50
    basic.clearScreen()
    led.plotBarGraph(temperatura_actual, temperatura_maxima)
}

function moure_la_gota() {
    
    let img = images.createImage(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    img.setPixel(x, y, true)
    img.showImage(0)
    let acc_x = input.acceleration(Dimension.X)
    let acc_y = input.acceleration(Dimension.Y)
    if (acc_x <= 150 && x > 0) {
        x -= 1
    }
    
    if (acc_x > 150 && x < 4) {
        x += 1
    }
    
    if (acc_y <= 150 && y > 0) {
        y -= 1
    }
    
    if (acc_y > 150 && y < 4) {
        y += 1
    }
    
}

basic.forever(function on_forever() {
    if (modo == "estacio_meteorologica") {
        estacio_meteorologica()
    } else if (modo == "moure_la_gota") {
        moure_la_gota()
    }
    
})
