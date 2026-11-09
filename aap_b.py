from flask import Flask, jsonify

app = Flask(__name__)

# Rota RESTful retornando JSON
@app.route('/api/hello', methods=['GET'])
def api_hello():
    return jsonify({
        "status": "sucesso",
        "mensagem": "Hello World RESTful!",
        "codigo": 200
    })

if __name__ == '__main__':
    app.run(debug=True)