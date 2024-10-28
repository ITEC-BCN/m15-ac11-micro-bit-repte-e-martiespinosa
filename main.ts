let x = 0
let y = 0
basic.forever(function on_forever() {
    let temperatura_actual = input.temperature()
    let temperatura_maxima = 30
    basic.clearScreen()
    led.plotBarGraph(temperatura_actual, temperatura_maxima)
    let img = images.createImage(`
        # . . . .
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
        let x -= 1
    }
    
    if (acc_x > 150 && x < 4) {
        x += 1
    }
    
    if (acc_y <= 150 && y > 0) {
        let y -= 1
    }
    
    if (acc_y > 150 && y < 4) {
        y += 1
    }
    
})
