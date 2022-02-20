import flask_server.flaskr
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify

app = flask_server.flaskr.create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
