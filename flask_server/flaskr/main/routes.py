from flask import Blueprint, request
from flaskr.functionality.handle_images import json_to_barcode
from flaskr.functionality.errors import InvalidBarcode, InvalidJson, MultipleBarcode

# this creates a blueprint for the visualization grouping
# the url prefix is prepended to the urls associated to this blueprint
main = Blueprint('main', __name__)

@main.route('/', methods=('GET',))
@main.route('/home', methods=('GET',))
def home():
    return 'Hello World!'


@main.route('/barcodeImage', methods=('POST',))
def barcodeImage():
    content = request.json
    print(content)
    try:
        barcode = json_to_barcode(content)
        return 'good'
    except Exception as e:
        print(e)
        return 'bad'