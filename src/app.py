from flask import Flask, request, jsonify
import uuid
import math

app = Flask(__name__)

# Dictionary to store receipts
receipts = {}

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    data = request.json
    receipt_id = str(uuid.uuid4())  # Generate unique ID
    points = calculate_points(data)  # Calculate points based on receipt data
    receipts[receipt_id] = points
    return jsonify({'id': receipt_id}), 200

@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    if receipt_id in receipts:
        return jsonify({'points': receipts[receipt_id]}), 200
    else:
        return jsonify({'error': 'Receipt not found'}), 404

def calculate_points(receipt):
    points = 0
    # Rule 1: Alphanumeric characters in retailer name
    points += sum(c.isalnum() for c in receipt['retailer'])

    # Convert total to float
    total = float(receipt['total'])

    # Rule 2: Total is a round dollar amount
    if total.is_integer():
        points += 50

    # Rule 3: Total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # Rule 4: 5 points for every two items
    num_items = len(receipt['items'])
    points += (num_items // 2) * 5

    # Rule 5: Item description length multiple of 3
    for item in receipt['items']:
        description = item['shortDescription'].strip()
        if len(description) % 3 == 0:
            price = float(item['price'])
            item_points = math.ceil(price * 0.2)
            points += item_points

    # Rule 6: Purchase day is odd
    purchase_date = receipt['purchaseDate']
    day = int(purchase_date.split('-')[2])
    if day % 2 != 0:
        points += 6

    # Rule 7: Purchase time between 2:00pm and 4:00pm
    time_str = receipt['purchaseTime']
    hour, minute = map(int, time_str.split(':'))
    time_in_minutes = hour * 60 + minute
    # Check if time is after 2:00pm (14:00:01) and before 4:00pm (16:00:00)
    if 14 * 60 + 1 <= time_in_minutes < 16 * 60:
        points += 10

    return points

if __name__ == '__main__':
    app.run(debug=True)