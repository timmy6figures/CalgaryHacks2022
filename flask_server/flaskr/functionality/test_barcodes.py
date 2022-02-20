import os
import cv2
from barcodes import get_barcode_data

def main():
    test_dir = "./test_imgs"
    for img_path in os.listdir(test_dir):
        im = cv2.imread(os.path.join(test_dir, img_path))
        cv2.imshow(img_path, cv2.resize(im, (600,600)))
        barcode = get_barcode_data(im)
        print(barcode)
        cv2.waitKey(0)

if __name__ == '__main__':
    main()