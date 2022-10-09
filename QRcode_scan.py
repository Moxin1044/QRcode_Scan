# -*- coding: utf-8-*-
from PIL import Image
import pyzbar.pyzbar as pyzbar
 
def QRcode_message(image):
    img = Image.open(image)
    # 因为一张图片可能是一张二维码，也可能里面有许多二维码
    barcodes = pyzbar.decode(img)
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        print(barcodeData)
 
if __name__ == '__main__':
    QRcode_message('test.png')