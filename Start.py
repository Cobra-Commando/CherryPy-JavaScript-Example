# WARNING: Program will sometimes result in a *500 Internal Server Error*
# Program uses vanilla JavaScript implemented via HTML, nothing too fancy
# Demo shows limits of using CherryPy and PySimpleGUI; use NodeJS instead

# try/catch import installs all of the three Python modules needed for this program
try:
    import PySimpleGUI as sg
    import cherrypy as ch
    import webbrowser as wb

# Testing done with PyCharm IDE 2021.1.1 using PySimpleGUI v4.40.0 / CherryPy v18.6.0
except ImportError:
    import subprocess
    subprocess.check_call(["python3", '-m', 'pip', 'install', 'PySimpleGUI==4.40.0'])
    subprocess.check_call(["python3", '-m', 'pip', 'install', 'CherryPy==18.6.0'])
    import PySimpleGUI as sg
    import cherrypy as ch
    import webbrowser as wb

# Main window for PySimpleGUI with dialog input box
layout = [[sg.Text('Write down a phrase below:')],
                 [sg.InputText(key='-IN-')],
                 [sg.Submit(), sg.Cancel()]]

# Main window title bar displays name of Python program
window = sg.Window('CherryPy-JavaScript Demo', layout)

# Main window self-closes after an input phrase is entered
event, values = window.read()
window.close()

# JS-wrapper class for looping the input dialog string 10x
def js_wrapper(wrap : str):
    supreme = "\"" + wrap + "\""
    el_1 = "\n<script type = \"text/javascript\">"
    el_2 = "\nvar count;"
    el_3 = "\nfor (count = 0; count < 10; count++) {"
    el_4 = "\n\tdocument.write(" + supreme + ");"
    el_5 = "\n\tdocument.write(\"<br />\");"
    el_6 = "\n}"
    el_7 = "\n</script>"
    crunchy = el_1 + el_2 + el_3 + el_4 + el_5 + el_6 + el_7
    return crunchy

# initiates CherryPy HTTP server for input dialog string
def open_browser(phrase: str):
    # Please note program is *buggy* if/when it's closed
    wb.open('http://127.0.0.1:8080/', new=2)
    class DisplayLocal(object):
        def index(self):
            # calls JS wrapper class
            test = js_wrapper(phrase)
            return test
        index.exposed = True
    ch.quickstart(DisplayLocal())

# window event triggers web browser open @ localhost:8080
text_input = values['-IN-']
open_browser(text_input)





