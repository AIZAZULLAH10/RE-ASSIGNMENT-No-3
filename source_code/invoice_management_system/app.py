"""
Legacy Invoice Management System
A simulated legacy web application for reverse engineering demonstration.
This app mimics common patterns found in undocumented legacy systems:
- Hidden form tokens
- Inline JavaScript validation
- Session-based authentication
- File-based data storage
- Hardcoded credentials
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import json
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'legacy_secret_key_1985'  # Hardcoded secret (common in legacy)

# Legacy data storage (simulating old flat-file database)
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

USERS_FILE = os.path.join(DATA_DIR, 'users.json')
INVOICES_FILE = os.path.join(DATA_DIR, 'invoices.json')
LOG_FILE = os.path.join(DATA_DIR, 'activity.log')

# Initialize legacy data
def init_legacy_data():
    if not os.path.exists(USERS_FILE):
        users = [
            {"id": 1, "username": "admin", "password": "admin123", "role": "admin"},
            {"id": 2, "username": "user1", "password": "password1", "role": "user"},
            {"id": 3, "username": "accountant", "password": "acc2020", "role": "user"}
        ]
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f, indent=2)

    if not os.path.exists(INVOICES_FILE):
        invoices = [
            {"id": "INV-001", "customer": "ABC Corp", "amount": 1500.00, "tax": 135.00, "date": "2024-01-15", "status": "paid"},
            {"id": "INV-002", "customer": "XYZ Ltd", "amount": 2300.50, "tax": 207.05, "date": "2024-01-20", "status": "pending"},
            {"id": "INV-003", "customer": "Global Tech", "amount": 875.25, "tax": 78.77, "date": "2024-02-01", "status": "paid"}
        ]
        with open(INVOICES_FILE, 'w') as f:
            json.dump(invoices, f, indent=2)

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            f.write(f"[{datetime.now()}] System initialized\n")

def log_activity(action):
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{datetime.now()}] {action}\n")

def get_users():
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def get_invoices():
    with open(INVOICES_FILE, 'r') as f:
        return json.load(f)

def save_invoices(invoices):
    with open(INVOICES_FILE, 'w') as f:
        json.dump(invoices, f, indent=2)

# Generate hidden token (simulating legacy anti-CSRF mechanism)
def generate_token():
    return str(uuid.uuid4())[:8].upper()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        form_token = request.form.get('form_token', '')

        # Check token (legacy validation)
        if form_token != session.get('form_token'):
            error = 'Invalid session token. Please refresh the page.'
            log_activity(f"Failed login attempt for {username} - invalid token")
        else:
            users = get_users()
            user = next((u for u in users if u['username'] == username and u['password'] == password), None)

            if user:
                session['logged_in'] = True
                session['username'] = user['username']
                session['role'] = user['role']
                log_activity(f"User {username} logged in successfully")
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid username or password!'
                log_activity(f"Failed login attempt for {username}")

    token = generate_token()
    session['form_token'] = token

    return render_template('login.html', error=error, token=token)

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    invoices = get_invoices()
    total_amount = sum(inv['amount'] for inv in invoices)
    total_tax = sum(inv['tax'] for inv in invoices)

    return render_template('dashboard.html',
                         username=session.get('username'),
                         role=session.get('role'),
                         invoices=invoices,
                         total_amount=total_amount,
                         total_tax=total_tax,
                         invoice_count=len(invoices))

@app.route('/add-invoice', methods=['GET', 'POST'])
def add_invoice():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    error = None
    success = None

    if request.method == 'POST':
        customer = request.form.get('customer', '')
        amount_str = request.form.get('amount', '0')
        form_token = request.form.get('form_token', '')

        # Validate token
        if form_token != session.get('form_token'):
            error = 'Invalid form token!'
        elif not customer or not amount_str:
            error = 'All fields are required!'
        else:
            try:
                amount = float(amount_str)
                if amount <= 0:
                    error = 'Amount must be greater than zero!'
                else:
                    # Auto-calculate tax (10%)
                    tax = amount * 0.10
                    invoice_id = f"INV-{len(get_invoices()) + 1:03d}"

                    new_invoice = {
                        "id": invoice_id,
                        "customer": customer,
                        "amount": amount,
                        "tax": round(tax, 2),
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "status": "pending"
                    }

                    invoices = get_invoices()
                    invoices.append(new_invoice)
                    save_invoices(invoices)

                    log_activity(f"Invoice {invoice_id} created by {session.get('username')}")
                    success = f"Invoice {invoice_id} created successfully!"
            except ValueError:
                error = 'Invalid amount format!'

    token = generate_token()
    session['form_token'] = token

    return render_template('add_invoice.html', error=error, success=success, token=token)

@app.route('/search-orders', methods=['GET', 'POST'])
def search_orders():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    results = []
    keyword = ''

    if request.method == 'POST':
        keyword = request.form.get('keyword', '').lower()
        invoices = get_invoices()
        results = [inv for inv in invoices if keyword in inv['customer'].lower() or keyword in inv['id'].lower()]
        log_activity(f"Search performed by {session.get('username')} for '{keyword}'")
    else:
        results = get_invoices()

    return render_template('search.html', results=results, keyword=keyword)

@app.route('/logout')
def logout():
    log_activity(f"User {session.get('username')} logged out")
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_legacy_data()
    print("Legacy Invoice System starting on http://localhost:5000")
    print("Default credentials: admin / admin123")
    app.run(host='0.0.0.0', port=5000, debug=True)
