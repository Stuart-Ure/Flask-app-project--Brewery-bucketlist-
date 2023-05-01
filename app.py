
from flask import Flask, render_template

from controllers.city_controller import cities_blueprint
from controllers.brewery_controller import brewery_blueprint

app = Flask(__name__)

app.register_blueprint(cities_blueprint)
app.register_blueprint(brewery_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)