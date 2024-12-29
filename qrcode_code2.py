import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)

link=input("Enter Your Link: ")
name=input("Enter Your Qr Name: ")
qr.add_data(link)
qr.make(fit=True)

custom=input("Do You want to Customize your Qr Code (Y/N)")
if custom=="Y"or"y":
    colour1=input("Enter The QR Colour: ")
    bg_colour=input("Enter The Baground Colour: ")
    img=qr.make_image(fill_color=colour1,back_color=bg_colour)
    img.save(name)
elif custom=="N"or"n":
    img=qr.make_image(fill_color="black",back_color="white")
    img.save(name)
else:
    print("Enter correct Value")

