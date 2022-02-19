import numpy as np
from barcodes import get_barcode_data
from errors import InvalidJson

def json_to_barcode(json):
    try:
        img = json["image"]
    except Exception:
        raise InvalidJson()
    
    img = np.array(json["image"])
    return get_barcode_data(img)
