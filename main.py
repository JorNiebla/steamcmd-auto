import PySimpleGUI as sg
import shlex, subprocess
import sys


def calldownload(appid, workshopid):
    print(f'Downloading {workshopid} from {appid}')
    args = "steamcmd/steamcmd.exe +force_install_dir steam/cs1_ds +login anonymous +app_update 480 +quit"
    clean_args = shlex.split(args)
    return subprocess.Popen(clean_args, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
         # process line here

#########################################################

# All the stuff inside your window.
layout = [  [sg.Text("APPID")],
            [sg.InputText()],
            [sg.Text("WORKSHOPID")],
            [sg.InputText()],
            [sg.Button('Download'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
steamcmd_proc = None

while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Download':
        if steamcmd_proc != None:
            print('Steamcmd ya ejecutado')
            break
        steamcmd_proc = calldownload(values[0],values[1])

    if steamcmd_proc != None:
        sg.Print(steamcmd_proc.stdout, wait=True)

window.close()