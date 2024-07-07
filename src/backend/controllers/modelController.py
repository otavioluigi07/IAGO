from flask import request, jsonify
from . import app
from services.modelService import ModelService

@app.route('/models', methods=['POST'])
def create_model():
    data = request.json
    result = ModelService.create_model(
        name=data.get('name'),
        max_token=data.get('max_token'),
        min_token=data.get('min_token')
    )
    return jsonify(result)

@app.route('/models/<int:model_id>', methods=['GET'])
def get_model(model_id):
    result = ModelService.get_model(model_id)
    return jsonify(result)

@app.route('/models/<int:model_id>', methods=['PUT'])
def update_model(model_id):
    data = request.json
    result = ModelService.update_model(
        model_id,
        name=data.get('name'),
        max_token=data.get('max_token'),
        min_token=data.get('min_token')
    )
    return jsonify(result)

@app.route('/models/<int:model_id>', methods=['DELETE'])
def delete_model(model_id):
    result = ModelService.delete_model(model_id)
    return jsonify(result)
