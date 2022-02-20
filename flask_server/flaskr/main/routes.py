from flask import Blueprint, request, jsonify, current_app
from flaskr.functionality.barcodes import get_barcode_data
from flaskr.functionality.barcode_to_info_edamame import get_product_information
from flaskr.functionality.errors import InvalidBarcode, MultipleBarcode

import numpy as np

# this creates a blueprint for the visualization grouping
# the url prefix is prepended to the urls associated to this blueprint
main = Blueprint('main', __name__)

@main.route('/', methods=('GET',))
@main.route('/home', methods=('GET',))
def home():
    return 'Hello World!'

@main.route('/barcodeImage', methods=('POST',))
def barcodeImage():
    print(request)
    content = request.json
    print(content)

    # read the image from the request body
    img = None
    try:
        img = np.array(content["image"])
    except Exception:
        jsonify({'error': 'no image'})
    
    # read the barcode data from the image that was sent in the request body
    try:
        barcode = get_barcode_data(img)
    except InvalidBarcode as e:
        jsonify({'error': 'invalid barcode'})
    except MultipleBarcode as e:
        jsonify({'error': 'multiple barcode'})

    # get the nutritional info from the barcode
    try:
        info = get_product_information(current_app.config['APP_ID'], current_app.config['APP_KEY'], barcode=barcode)
    except Exception as e:
        jsonify({'error': 'no product information'})

    return jsonify({'info': info})
    