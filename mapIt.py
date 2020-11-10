#! python3
# this script launches a map in the browser using an address
# from the commmand line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get the address from the command line
    address = ' '.join(sys.argv[1:])
else:
    # Get the address from the clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
