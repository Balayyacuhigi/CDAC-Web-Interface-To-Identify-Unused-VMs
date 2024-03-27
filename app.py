from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Sample VM data with last access time
vm_data = [
    {"name": "Linux", "last_access": datetime.now()- timedelta(days=random.randint(0, 365))},
    {"name": "Hyper-V", "last_access": datetime.now()- timedelta(days=random.randint(0, 365))},
    {"name": "Xen", "last_access": datetime.now() - timedelta(days=random.randint(0, 365))},
    {"name": "QEMU", "last_access": datetime.now() - timedelta(days=random.randint(0, 365))},
    {"name": "VMware Fusion", "last_access": datetime.now() - timedelta(days=random.randint(0, 365))},
    {"name": "Oracle VM VirtualBox", "last_access": datetime.now() - timedelta(days=random.randint(0, 365))},
    {"name": "VMware ESXi", "last_access": datetime.now()- timedelta(days=random.randint(0, 365))},
    {"name": "Red hat virtualization", "last_access": datetime.now()- timedelta(days=random.randint(0, 365))},
    {"name": "Virtual DOS Machine", "last_access": datetime.now() - timedelta(days=random.randint(0, 365))},
]

def filter_vms_by_last_access(threshold_months):
    filtered_vms = []
    for vm in vm_data:
        days_since_last_access = (datetime.now() - vm["last_access"]).days
        months_since_last_access = days_since_last_access // 30  
        if months_since_last_access >= threshold_months:
            filtered_vms.append(vm)
    return filtered_vms

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    # Assuming you have a fixed username and password for this example
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'cdac' and password == '2003':
        return redirect(url_for('select_month'))
    else:
        return "Invalid credentials. Please try again."

@app.route('/select_month')
def select_month():
    return render_template('index.html')

@app.route('/vm_access', methods=['POST'])
def vm_access():
    threshold_months = int(request.form.get('threshold'))
    filtered_vms = filter_vms_by_last_access(threshold_months)
    return render_template('vm_access.html', vms=filtered_vms)

if __name__ == '__main__':
    app.run(debug=True)