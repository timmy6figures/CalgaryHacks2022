import os
import cv2
from pyzbar import pyzbar

def draw_barcode_to_image(object, image):
    """
    :param object: This is the barcode object, we use the position to draw on the image.
    :param image: This is the image the barcode was extracted from.
    :return: The image with the drawn on box surrounding the extracted barcode. 
    """
    image = cv2.rectangle(
        image,
        (object.rect.left, object.rect.top),
        (object.rect.left+object.rect.width, object.rect.top+object.rect.height),
        color=(0,255,0),
        thickness=5
    )
    return image

def extract_barcode_(img):
    """
    This function uses pyzbar to pull the barcode information from images fed into it.
    :param img: Image to extract the barcode data from.
    :return: The objects extracted from the image, this is a list of barcodes.
    """
    decoded_objects = pyzbar.decode(img)
    return decoded_objects

def get_barcode_data(img):
    """This function takes in an image and transforms it into an extracted barcode.

    Args:
        img (np.array): This is an array of image data that represents the image sent to the server.

    Raises:
        InvalidBarcode: This error is thrown when no barcode can be extracted from an image.
        MultipleBarcode: This error is thrown when multiple barcodes are found in the image.

    Returns:
        string: The barcode as a string extracted from the image.
    """
    barcode = extract_barcode_(img)
    if(len(barcode) == 0):
        print('no barcode')
        return ""
    if(len(barcode) > 1):
        print('too many barcodes')
        return ""
    return barcode[0]

def main():
    test_dir = "./test_imgs"
    for img_path in os.listdir(test_dir):
        if('barcode3' not in img_path):
            continue
        im = cv2.resize(cv2.imread(os.path.join(test_dir, img_path)), (600,600))
        cv2.imshow(img_path, im)
        cv2.waitKey(0)
        barcode_object = get_barcode_data(im)
        barcode = barcode_object.data
        print(barcode_object)
        print(barcode)
        image = draw_barcode_to_image(barcode_object, im)
        cv2.imshow(img_path, image)
        cv2.waitKey(0)

if __name__ == '__main__':
    main()