from flask import Flask, request
import os
import urllib.request

replica = os.environ.get('CS_REPLICA')
server = os.environ.get('CS_SERVER')
port = int(os.environ.get('PORT'))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'], defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    redirect_url = request.args.get('redirect')

    if redirect_url:
        try:
            contents = urllib.request.urlopen(redirect_url).read()
            return contents

        except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 400

        return jsonify({"message": "No redirect URL provided"}), 400

    else:
        return f'Response:{server}:{replica}:{port}:/{path}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
