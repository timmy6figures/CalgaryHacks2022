import numpy as np
from flask_server.flaskr.functionality.barcodes import get_barcode_data
from flask_server.flaskr.functionality.errors import InvalidJson

def json_to_barcode(json):
    try:
        img = json["image"]
    except Exception:
        raise InvalidJson()
    
    img = np.array(json["image"])
    return get_barcode_data(img)
