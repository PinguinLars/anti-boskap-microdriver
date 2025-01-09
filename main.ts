input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Alarm = false
    music.stopMelody(MelodyStopOptions.All)
})
let Alarm = false
Alarm = true
basic.forever(function on_forever() {
    if (Alarm == true) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Chase), music.PlaybackMode.InBackground)
    }
    
})
