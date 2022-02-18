from flask import Blueprint

# this creates a blueprint for the visualization grouping
# the url prefix is prepended to the urls associated to this blueprint
vis = Blueprint('visualizations', __name__) #, url_prefix='/visualization')

@vis.route('/view', methods=('GET',))
def view():
    return 'Hello from visualizations'