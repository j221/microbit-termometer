def on_forever():
    def on_button_pressed_a():
        temp = input.temperature()
        basic.show_number(temp)
        basic.pause(10000)
        basic.clear_screen()

    input.on_button_pressed(Button.A, on_button_pressed_a)

basic.forever(on_forever)
