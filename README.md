# Warehouse-Inventory-Management-System-using-Barcode-QR-Code-and-RFID

📦 Warehouse Inventory Management System
A smart, tech-enabled inventory management system using Barcode, QR Code, and RFID for efficient stock tracking and real-time updates. Built with Python Flask, SQLite/MySQL, and integrated with OpenCV, pyzbar, and RFID hardware.
🚀 Features
•	🔐 Admin & Staff Login
•	📦 Add/Edit/Delete Inventory Items
•	📷 Barcode & QR Code Scanning (Camera/File Upload)
•	📶 RFID Tag Detection (Auto-In/Out)
•	📊 Stock In / Stock Out Module
•	🔍 Search & Filter Inventory
•	📉 Low-Stock Alerts
•	📄 Report Generation (CSV, PDF)
•	💾 Backup & Restore Inventory Data
•	🖥️ Simple and Clean Web UI
🛠️ Tech Stack
Layer	Technology
Frontend	HTML, CSS, JavaScript, Bootstrap
Backend	Python (Flask)
Database	SQLite / MySQL
Barcode/QR	OpenCV + Pyzbar
RFID Reader	MFRC522 / USB RFID Reader
Others	SQLAlchemy, Flask-WTF
📂 Project Structure

Warehouse-Inventory-Management/
├── app.py
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── add_item.html
│   ├── scan_item.html
│   └── report.html
├── rfid/
│   └── rfid_scanner.py
├── barcode_scanner.py
├── database.db
├── requirements.txt
└── README.md

✅ Installation
1.	1. Clone the Repository
git clone https://github.com/yourusername/Warehouse-Inventory-Management.git
cd Warehouse-Inventory-Management
2.	2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3.	3. Install Dependencies
pip install -r requirements.txt
4.	4. Run the App
python app.py
App will run at http://127.0.0.1:5000
🔍 Barcode/QR Scanner
- Uses pyzbar and OpenCV to scan barcode/QR from:
  - Live Camera
  - Uploaded Image
📶 RFID Scanner
- Connect your RFID module (MFRC522 or USB Reader)
- Detects and logs tag scans automatically
📸 Screenshots
📷 Include screenshots of:
- Dashboard
- Add Inventory
- Scan Item
- RFID Logs
📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙋‍♂️ Developer
Rajvardhan Singh Parmar
B.Tech (IT-IoT), MITS Gwalior
Email: thakurrajvardhansinghparmar@gmail.com
GitHub: @yourusername
💡 Future Enhancements
•	🔁 Real-time sync with cloud database
•	📱 Mobile App using Flutter/React Native
•	📧 Email & SMS Alerts
•	📦 API for third-party ERP integration
📬 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
