from flask import Blueprint, request, jsonify
from apps.services.cliente_service import ClienteService



cliente_controller = Blueprint('cliente_controller', __name__)
cliente_service = ClienteService()

@cliente_controller.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.get_json()
    nuevo_cliente = cliente_service.crear_cliente(data)
    return jsonify(nuevo_cliente), 201

@cliente_controller.route('/clientes', methods=['GET'])
def obtener_clientes():
    clientes = cliente_service.leer_clientes()
    return jsonify(clientes), 200

@cliente_controller.route('/clientes/<int:idCliente>', methods=['PUT'])
def actualizar_cliente(idCliente):
    data = request.get_json()
    cliente_actualizado = cliente_service.actualizar_cliente(idCliente, data)
    return jsonify(cliente_actualizado), 200

@cliente_controller.route('/clientes/verificar', methods=['POST'])
def verificar_cliente():
    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({"error": "Falta el email"}), 400

    registrado = cliente_service.verificar_cliente(email)
    return jsonify({"registrado": registrado}), 200

@cliente_controller.route('/clientes/<int:idCliente>', methods=['DELETE'])
def eliminar_cliente(idCliente):
    cliente_service.eliminar_cliente(idCliente)
    return '', 204

