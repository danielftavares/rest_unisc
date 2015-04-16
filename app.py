#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response
import math

app = Flask(__name__)

@app.route('/quadrado/<int:lado>', methods=['GET'])
def infoquadrado(lado):
	return jsonify({"area": lado * lado, "perimetro": lado * 4, "lado": lado})

@app.route('/quadrado', methods=['POST', 'PUT'])
def infoquadradopost():
	slado = request.form["lado"]
	if not slado:
		abort(400)
	try:
		slado = int(slado)
	except:
		abort(400)
	return infoquadrado(int(request.form["lado"]))

@app.route('/retangulo/<int:base>/<int:altura>', methods=['GET'])
def inforetangulo(base, altura):
	return jsonify({"area": base * altura, "perimetro": (base * 2) + (altura * 2), "base": base, "altura": altura })

@app.route('/triangulo/<int:base>/<int:altura>', methods=['GET'])
def infotriangulo(base, altura):
	hipotenusa =  calculahipotenusa(base, altura)
	return jsonify({
		"area": (base * altura)/2, 
		"perimetro": base + altura + hipotenusa,
		"base": base,
		"altura": altura,
		"hipotenusa": hipotenusa})

@app.route('/circulo/<int:raio>', methods=['GET'])
def infocirculo(raio):
	return jsonify({
		"area": math.pow(raio, 2) * math.pi,
		"perimetro": 2 * math.pi * raio,
		"raio": raio,
		"diametro": raio * 2 })

@app.route('/trapezio/<int:baseMaior>/<int:baseMenor>/<int:altura>', methods=['GET'])
def infotrapezio(baseMaior, baseMenor, altura):
	a1 =  baseMenor * altura
	a2 = ((baseMaior - baseMenor) * altura) / 2
	return jsonify({
		"area": a1 + a2,
		"perimetro": baseMaior + baseMenor + altura + calculahipotenusa(baseMaior - baseMenor, altura)})

@app.route('/losango/<int:diagonal1>/<int:diagonal2>', methods=['GET'])
def infolosango(diagonal1, diagonal2):
	return jsonify({
		"area": (diagonal1 * diagonal2)/2,
		"perimetro": 4 * calculahipotenusa(diagonal1/2, diagonal2 / 2)}
		)

def calculahipotenusa(base, altura):
	return  math.sqrt( math.pow(base, 2) + math.pow(altura, 2) )

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Parâmetros de entrada inconsistentes/inexistentes'}), 400)

if __name__ == '__main__':
	app.run(debug=True)