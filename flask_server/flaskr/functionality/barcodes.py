from pyzbar import pyzbar
import cv2
from errors import InvalidBarcode, MultipleBarcode

def draw_barcode_to_image(object, image):
    image = cv2.rectangle(
        image,
        (object.rect.left, object.rect.top),
        (object.rect.left+object.rect.width, object.rect.top+object.rect.height),
        color=(0,255,0),
        thickness=5
    )
    return image

def extract_barcode_(img):
    decoded_objects = pyzbar.decode(img)
    return decoded_objects

def get_barcode_data(img):
    barcode = extract_barcode_(img)
    if(len(barcode) == 0):
        raise InvalidBarcode()
    if(len(barcode) > 1):
        raise MultipleBarcode(len(barcode))
    print(barcode)
    return barcode[0].data

