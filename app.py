from flask import Flask, render_template
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pokemon/<name>')
def get_pokemon(name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Pokemon not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
