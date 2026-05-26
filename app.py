from flask import Flask, request, jsonify

app = Flask(__name__)

# FASE 2: Ruta reparada (Fuerza de manera estricta que toda placa se guarde en MAYÚSCULAS)
@app.route('/api/peritajes', methods=['POST'])
def crear_peritaje():
    datos = request.get_json()
    placa = datos.get('placa') 
    
    # CIRUGÍA DE CÓDIGO: Aplicamos .upper() para transformar el string a mayúsculas estrictas
    if placa:
        placa = placa.upper() [cite: 33]
    
    # Simulación de guardar en la base de datos / JSON
    return jsonify({"mensaje": "Peritaje registrado", "placa_guardada": placa}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)