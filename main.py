"""
Author: new92
Github: https://www.github.com/new92
Program for generating QR codes
"""
try:
    import sys
    import platform
    from os import system
    from time import sleep
    import qrcode
except ImportError as imp: 
    print("[!] WARNING: Not all packages used in this program have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux') == True:
        system("sudo pip install -r requirements.txt")
        pass
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
        pass
    elif platform.system() == 'Windows':
        system("pip3 install -r requirements.txt")
        pass

print("""
░██████╗░██████╗░  ░█████╗░░█████╗░██████╗░███████╗  ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔═══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║██╗██║██████╔╝  ██║░░╚═╝██║░░██║██║░░██║█████╗░░  ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
╚██████╔╝██╔══██╗  ██║░░██╗██║░░██║██║░░██║██╔══╝░░  ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
░╚═██╔═╝░██║░░██║  ╚█████╔╝╚█████╔╝██████╔╝███████╗  ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝  ░╚════╝░░╚════╝░╚═════╝░╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
""")
print("\n")
print("[+] Github: https://www.github.com/new92")
print("\n")
print("[+] Program for generating QR codes")
print("\n")
print("[01] Generate QR code(s)")
print("[02] Exit")
print("\n")
option=int(input("[::] Please enter the number of the option (from above): "))
while option < 1 or option > 2 or option == None:
    print("[!] Invalid number !")
    sleep(2)
    choice=int(input("[::] Please enter again: "))
if option == 1:
    times=int(input("[+] How many QR codes do you want to make ? "))
    if times == 1:
        website=input("[+] Please enter the link for the QR code: ")
        sleep(2)
        link=""+str(website)
        qrC = qrcode.QRCode(version = 2,box_size = 10,border = 10)
        qrC.add_data(link)
        qrC.make(fit=True)
        img = qrC.make_image(fill = "black")
        img.save("qrcode.png")
        print("[!] Successfully saved at: qrcode.png")
    else: 
        for i in range(int(times)):
            website=input("[+] Please enter the link for the number "+str(i + 1)+" QR code: ")
            sleep(2)
            link=""+str(website)
            qrC = qrcode.QRCode(version = 2,box_size = 10,border = 10)
            qrC.add_data(link)
            qrC.make(fit=True)
            QRimg= qrC.make_image(fill = "black")
            QRimg.save("qrcode"+str(i)+".png")
            print(f"[+] Successfully saved at: qrcode{i}.png")
elif option == 2:
    print("[+] Exiting...")
    quit(0)
