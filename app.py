from flask import Flask, render_template

from controllers.albums_controller import albums_blueprint
from controllers.record_label_controller import record_labels_blueprint

app = Flask(__name__)

app.register_blueprint(albums_blueprint)
app.register_blueprint(record_labels_blueprint)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)