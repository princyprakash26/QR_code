#decode QR

import json
from pyzbar.pyzbar import decode
from PIL import Image

with open('config.json') as f:
    config = json.load(f)

img = Image.open((config['path']))
result = decode(img)
print(result)