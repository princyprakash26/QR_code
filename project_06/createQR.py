#create QRcode

import json
import qrcode

with open('config.json') as f:
    config = json.load(f)

data = "Always Be Happy"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color ='red', black_color = "white")
img.save(config['path'])
