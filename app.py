import os
import sqlite3
import cv2
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from pyzbar.pyzbar import decode
from PIL import Image

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Database initialization
def init_db():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS warehouse (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE)''')
    c.execute('''CREATE TABLE IF NOT EXISTS item (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    barcode TEXT,
                    rfid TEXT,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    warehouse_id INTEGER,
                    FOREIGN KEY(warehouse_id) REFERENCES warehouse(id))''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''SELECT item.id, item.name, item.barcode, item.rfid, item.quantity, warehouse.name 
                 FROM item LEFT JOIN warehouse ON item.warehouse_id = warehouse.id''')
    items = c.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('SELECT * FROM warehouse')
    warehouses = c.fetchall()

    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        warehouse_id = request.form.get('warehouse_id')
        barcode = request.form.get('barcode', '')
        rfid = request.form.get('rfid', '')

        # Handle barcode from uploaded image
        if 'barcode_image' in request.files:
            file = request.files['barcode_image']
            if file.filename != '':
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(filepath)
                img = Image.open(filepath)
                decoded = decode(img)
                if decoded:
                    barcode = decoded[0].data.decode('utf-8')

        # Handle barcode from camera
        if request.form.get('camera_scan') == '1':
            cap = cv2.VideoCapture(0)
            barcode = ''
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                barcodes = decode(frame)
                for b in barcodes:
                    barcode = b.data.decode('utf-8')
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                if barcode:
                    break
            cap.release()
            cv2.destroyAllWindows()

        # Handle RFID from simulated serial (manual or simulated input)
        if request.form.get('rfid_scan') == '1':
            # Simulated RFID input; replace with actual serial reading if needed
            rfid = "SIMULATED_RFID_123456"

        c.execute('INSERT INTO item (name, quantity, barcode, rfid, warehouse_id) VALUES (?, ?, ?, ?, ?)',
                  (name, quantity, barcode, rfid, warehouse_id))
        conn.commit()
        flash("Item added successfully!", "success")
        return redirect(url_for('index'))

    return render_template('add_item.html', warehouses=warehouses)

@app.route('/warehouses')
def warehouses():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('SELECT * FROM warehouse')
    data = c.fetchall()
    conn.close()
    return render_template('warehouses.html', warehouses=data)

@app.route('/add_warehouse', methods=['GET', 'POST'])
def add_warehouse():
    if request.method == 'POST':
        name = request.form['name']
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        c.execute('INSERT INTO warehouse (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        return redirect(url_for('warehouses'))
    return render_template('add_warehouse.html')

@app.route('/rfid_tracker', methods=['GET', 'POST'])
def rfid_tracker():
    item = None
    if request.method == 'POST':
        rfid = request.form['rfid']
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        c.execute('SELECT * FROM item WHERE rfid = ?', (rfid,))
        item = c.fetchone()
        conn.close()
    return render_template('rfid_tracker.html', item=item)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
