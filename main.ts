basic.forever(function on_forever() {
    input.onButtonPressed(Button.A, function on_button_pressed_a() {
        let temp = input.temperature()
        basic.showNumber(temp)
        basic.pause(10000)
        basic.clearScreen()
    })
})
