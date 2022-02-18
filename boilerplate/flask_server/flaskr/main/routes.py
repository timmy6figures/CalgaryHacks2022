from flask import Blueprint

# this creates a blueprint for the visualization grouping
# the url prefix is prepended to the urls associated to this blueprint
main = Blueprint('main', __name__) #, url_prefix='/visualization')

@main.route('/', methods=('GET',))
@main.route('/home', methods=('GET',))
def home():
    return 'Hello World!'