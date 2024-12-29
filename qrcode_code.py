"""pip install qrcode"""
import qrcode as qr
img = qr.make("https://github.com/abhinavdwivedi05")
img.save("abhinav_git.png")