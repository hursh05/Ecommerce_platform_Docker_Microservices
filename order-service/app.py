from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka:9092')

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    producer.send('orders', bytes(str(data), 'utf-8'))
    return jsonify({"message": "Order created and event sent to Kafka!"}), 201
