import qrcode

data = "https://converstiontoolbox.vercel.app/"

qr = qrcode.make(data)

qr.save("my_qr.png")

print("QR Code generated successfully!")
