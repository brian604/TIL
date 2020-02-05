import flask

server = flask.Flask('my server')


@server.route('/')
def home():
    return flask.render_template('homework.html')


server.run(port=8080, debug=True)
