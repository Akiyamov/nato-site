from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/о-компании")
def about():
    return render_template("about.html")

@app.route("/уголь")
def coal():
    return render_template("coal.html")

@app.route("/песок")
def sand():
    return render_template("sand.html")

@app.route("/щебень")
def stone():
    return render_template("stone.html")

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == "__main__":
    app.run(host='0.0.0.0')