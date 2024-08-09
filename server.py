from flask import Flask, request, jsonify, Response
import requests
import os
import urllib.request

replica = os.environ.get('CS_REPLICA')
server = os.environ.get('CS_SERVER')
port = int(os.environ.get('PORT'))

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    redirect_url = request.args.get('redirect')

    if redirect_url:
        try:
            contents = urllib.request.urlopen(redirect_url).read()
            return contents
            # Send a GET request to the redirect URL
            response = requests.get(redirect_url)

            # Create a Flask response object with the content from the external request
            flask_response = Response(response.content)

            # Set the status code and headers from the external response
            flask_response.status_code = response.status_code
            flask_response.headers = response.headers

            return flask_response

        except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 400

        return jsonify({"message": "No redirect URL provided"}), 400

    else:
        return f'Response:{server}:{replica}:/{path}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
