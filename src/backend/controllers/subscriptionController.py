from flask import request, jsonify
from . import app
from services.subscriptionService import SubscriptionService

@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    data = request.json
    result = SubscriptionService.create_subscription(
        name=data.get('name'),
        price=data.get('price'),
        model=data.get('model'),
        active=data.get('active')
    )
    return jsonify(result)

@app.route('/subscriptions/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    result = SubscriptionService.get_subscription(subscription_id)
    return jsonify(result)

@app.route('/subscriptions/<int:subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    data = request.json
    result = SubscriptionService.update_subscription(
        subscription_id,
        name=data.get('name'),
        price=data.get('price'),
        model=data.get('model'),
        active=data.get('active')
    )
    return jsonify(result)

@app.route('/subscriptions/<int:subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    result = SubscriptionService.delete_subscription(subscription_id)
    return jsonify(result)
