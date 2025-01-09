def on_button_pressed_a():
    global Alarm
    Alarm = False
    music.stop_melody(MelodyStopOptions.ALL)
input.on_button_pressed(Button.A, on_button_pressed_a)

Alarm = False
Alarm = True

def on_forever():
    if Alarm == True:
        music._play_default_background(music.built_in_playable_melody(Melodies.CHASE),
            music.PlaybackMode.IN_BACKGROUND)
basic.forever(on_forever)
