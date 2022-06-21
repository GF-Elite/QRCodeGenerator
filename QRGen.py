#Imports
try:
    import qrcode
    import time
    import pyfiglet
except ImportError as imp: 
    print("Error !")
    time.sleep(1)
    print("Please enter the command: pip3 install -r requirementsQ.txt")
    time.sleep(2)
#End of Imports

#Main program
gen=pyfiglet.figlet_format("QR  GENERATOR")
print(gen)
print("\n")
print("[+] Github: @new92")
print("\n")
print("[01] Generate QR code(s)")
print("[02] Exit")
print("\n")
option=input("[::] Please choose an option: ")
while option != "01" and option != "1" and option != "02" and option != "2":
    print("Invalid option !")
    time.sleep(2)
    choice=input("[::] Please enter again: ")
if option == "01" or option == "1":
    times=int(input("How many QR codes do you want to make ? "))
    while times < 0:
        print("Invalid number !")
        time.sleep(1)
        times=int(input("Please enter again: "))
    if times == 1:
        website=input("Please enter the link for the QR code: ")
        time.sleep(2)
        link=""+str(website)
        qrC = qrcode.QRCode(version = 2,
                        box_size = 10,
                        border = 10)
        qrC.add_data(link)
        qrC.make(fit=True)
        img = qrC.make_image(fill = "black")
        img.save("qrcode.png")
        print("Successfully saved at: qrcode.png")
    else: 
        for i in range(times):
            website=input("Please enter the link for the number "+str(i + 1)+" QR code: ")
            time.sleep(2)
            link=""+str(website)
            qrC = qrcode.QRCode(version = 2,
                            box_size = 10,
                            border = 10)
            qrC.add_data(link)
            qrC.make(fit=True)
            QRimg= qrC.make_image(fill = "black")
            QRimg.save("qrcode0000"+str(i)+".png")
            print("Successfully saved at: qrcode.png")
elif option == "02" or option == "2":
    exit(0)
#End of the Program
