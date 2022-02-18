import os

from flask import Flask

def create_app(test_config=None):
    # name is used to know the where the app is instatiated from
    # instance relative config tells app that config files are relative to the 
    # instance folder. The instance folder contains things we dont want in version control
    # this includes a database file if necessary or secrets
    app = Flask(__name__, instance_relative_config=True)

    # this instantiates what the config will be holding for us
    app.config.grom_mapping(
        SECRET_KEY='dev'
    )

    if(test_config is None):
        # if we are not testing we should load the config from the config file
        app.config.from_pyfile('config.py', silent=True)
    else:
        # if we are testing use the test config
        app.config.from_mapping(test_config)

    # ensure an instance path was properly created or we should throw an error
    if(not os.path.exists(app.instance_path)):
        raise Exception('Instance path does not exist')

    # load and register all the routes in the respective routes.py files
    from flaskr.main.routes import main
    app.register_blueprint(main)
    from flaskr.visualizations.routes import vis
    app.register_blueprint(vis)
    
    return app

