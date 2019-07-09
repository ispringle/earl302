import base64
from flask import Flask, redirect
app = Flask(__name__)

@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def return_url(path):
	requested_url = get_url(path)
	print(requested_url)
	return redirect(requested_url)

def get_url(encoding):
	url = str(base64.b64decode(encoding)[:-1])[2:-1]
	if 'http://' in url:
		return url
	else:
		return 'http://' + url

