from flask import Flask, request, jsonify

app = Flask(__name__)

# FASE 2: Ruta con el bug (guarda la placa tal como llega, incluso en minúsculas)
@app.route('/api/peritajes', methods=['POST'])
def crear_peritaje():
    datos = request.get_json()
    placa = datos.get('placa') # Aquí está el problema, no valida mayúsculas
    
    # Simulación de guardar en la base de datos / JSON
    return jsonify({"mensaje": "Peritaje registrado", "placa_guardada": placa}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)