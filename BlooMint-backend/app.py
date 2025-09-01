# 1️⃣ Imports
from flask import Flask, request, jsonify  # Flask imports
import mysql.connector                      # MySQL connector
import requests                              # Python requests library (for Flutterwave API)

print("Starting app.py")     # <-- optional, just to check if Python runs the file

# 2️⃣ Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",        # usually localhost
    user="root",             # your MySQL username
    password="john316",  #  <--your actual password
    database="bloomint_db"   # <--the new database you want to use
)

print("Connected to MySQL successfully!")  # <-- confirms connection worked

# 3️⃣ Create the Flask app
app = Flask(__name__)
@app.route('/create_payment', methods=['POST'])
def create_payment():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    item = data.get('item')
    
    # Payment payload
    payload = {
        "tx_ref": "BlooMint_" + str(data.get('order_id', 1)),  # unique order reference
        "amount": data.get('amount', 1200),  # default 1200
        "currency": "KES",
        "payment_options": "card, mobilemoney, ussd",
        "customer": {"email": email, "name": name},
        "redirect_url": "http://127.0.0.1:5000/payment_callback"  # temporary
    }

    # Headers with your Client Secret
    headers = {
        "Authorization": "HytorRJG596J4ZzDXQjYetpUCEHOB8xk",  # <-- new client  secret key
        "Content-Type": "application/json"
    }

    # Send request to Flutterwave
    response = requests.post("https://api.flutterwave.com/v3/payments", json=payload, headers=headers)
    return jsonify(response.json())

# 4️⃣ Define a route
@app.route('/')
def home():
    return "BlooMint Backend is Running!"

# 5️⃣ Run the Flask app
@app.route('/add-test')
def add_test():
    # Create a cursor object
    cursor = mydb.cursor()

    # SQL to create a table (if it doesn't exist)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        )
    """)

    # SQL to insert a test record
    cursor.execute("INSERT INTO test_table (name) VALUES (%s)", ("Faith",))

    # Commit changes to the database
    mydb.commit()

    return "Test record added to MySQL!" 

@app.route('/add_order', methods=['POST'])
def add_order():
    data = request.json  # Get JSON data from the request
    name = data.get('name')
    email = data.get('email')
    product = data.get('product')
    quantity = data.get('quantity')
    custom_pack = data.get('custom_pack', '')  # Optional field

    # Create a cursor object
    cursor = mydb.cursor()

    # Insert order into database
    sql = "INSERT INTO orders (name, email, product, quantity, custom_pack) VALUES (%s, %s, %s, %s, %s)"
    values = (name, email, product, quantity, custom_pack)
    cursor.execute(sql, values)
    mydb.commit()

    return jsonify({"message": "Order added successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
  

@app.route('/add_order', methods=['POST'])
def add_order():
    data = request.get_json()  # Get JSON from front end
    name = data.get('name')
    email = data.get('email')
    items = data.get('items')  # This should be a list of products

    if not items:
        return jsonify({'message': 'No items in cart'}), 400

    try:
        mycursor = mydb.cursor()
        for item in items:
            product_name = item['name']
            price = item['price']
            quantity = 1  # you can change if you add quantity selection later
            custom_pack = ""  # optional, for now leave empty
            sql = "INSERT INTO orders (name, email, product, quantity, custom_pack) VALUES (%s, %s, %s, %s, %s)"
            values = (name, email, product_name, quantity, custom_pack)
            mycursor.execute(sql, values)
        mydb.commit()
        return jsonify({'message': 'Order successfully added!'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error adding order'}), 500 
    if __name__ == "__main__":
        app.run(debug=True)