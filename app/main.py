from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({"status": "ok"})

@app.route('/')
def hello_world():
    return jsonify({"mensaje": "¡Hola! Esta es una aplicación de ejemplo para CI/CD"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
