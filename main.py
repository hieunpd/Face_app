# [START gae_python37_app]
from flask import Flask, render_template, request, redirect, flash, send_from_directory
import requests

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)



@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')



if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)
# [END gae_python37_app]
