#create QRcode

import qrcode

data = "Always Be Happy"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color ='red', black_color = "white")
img.save('/home/princy/Pictures/myQR.png')
