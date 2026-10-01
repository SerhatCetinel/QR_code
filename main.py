import pyqrcode

url = input("Enter the url here: ")

qrcode = pyqrcode.create(url)
qrcode.png("qrcode.png", scale=6)
