import flask_server.flaskr
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify

app = flask_server.flaskr.create_app()

if __name__ == '__main__':
    app.run(debug=True)

    @app.route('/geo', methods=['GET', 'POST'])
    def geo():
        return render_template('geo.html')

    @app.route('/postmethod', methods=['GET', 'POST'])
    def get_post_location():
        where = request.form['location']
        return where