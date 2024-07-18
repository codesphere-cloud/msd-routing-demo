from flask import Flask, request
import os

replica = os.environ.get('CS_REPLICA')
server = os.environ.get('CS_SERVER')
port = int(os.environ.get('PORT'))

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return f'Response:{server}:{replica}:/{path}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
