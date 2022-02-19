class InvalidBarcode(Exception):
    def __init__(self):
        super(InvalidBarcode, self).__init__("No barcode found in image.")

class MultipleBarcode(Exception):
    def __init__(self, count):
        super(InvalidBarcode, self).__init__(f"Found {count} batcodes in image, please take picture with just one.")

class InvalidJson(Exception):
    def __init__(self):
        super(InvalidJson, self).__init__("Request did not contain image.")