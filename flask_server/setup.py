import flaskr

app = flaskr.create_app()

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

