#decode QR

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("/home/princy/Pictures/myQR.png")
result = decode(img)
print(result)