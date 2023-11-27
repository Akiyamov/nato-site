from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/гифки')
def gifs():
    return render_template('gifs.html')

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')