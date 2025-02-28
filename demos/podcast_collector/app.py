import flask

from db import database

app = flask.Flask(__name__ )

@app.route('/')
def index():
    return flask.render_template('index.html', podcasts=database.podcasts)

@app.route('/about')
def about():
    return flask.render_template('about.html')

if __name__ == '__main__':
    app.run()
