
---

## **📌 `README.md` (Django Signals Testing Guide)**

```md
# Django Signals Testing

This repository demonstrates how **Django signals** work, covering:
- **Synchronous execution** of signals.
- **Signals running in the same thread** as the caller.
- **Signals running within the same database transaction**.

---

## 🚀 **Setup Instructions**

### **1️⃣ Clone the Repository**
If you haven't already cloned the repository, run:
```bash
git clone https://github.com/vasu2901/AccuknoxAssignment.git
cd django-signals-demo
```

---

### **2️⃣ Create and Activate a Virtual Environment**
Create a virtual environment (if not already set up):
```bash
python -m venv venv
```
Activate the virtual environment:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

---

### **3️⃣ Install Dependencies**
After activating the virtual environment, install the required packages:

```bash
pip install django
```

---

### **4️⃣ Set Up Django Project**
1. Navigate to your Django project folder:
   ```bash
   cd accuknox
   ```

2. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

---

## 🛠 **Running the Signals Tests**

1. Start the Django shell:
   ```bash
   python manage.py shell
   ```
2. Inside the Django shell, import the test script:
   ```python
   import testapp.test
   ```

---

## 📌 **Expected Output**
After running the tests, you should see something like this:

```
>>> import testapp.test   
Main thread ID: 7768

>>> Testing Synchronous Execution
Sync Signal handler started
Sync Signal handler finished
Thread Signal handler running in thread: 7768
Transaction Signal received.
User exists in DB: True

>>> Testing Same-Thread Execution
Sync Signal handler started
Sync Signal handler finished
Thread Signal handler running in thread: 7768
Transaction Signal received.
User exists in DB: True

>>> Testing Transaction Behavior
Sync Signal handler started
Sync Signal handler finished
Thread Signal handler running in thread: 7768
Transaction Signal received.
User exists in DB: True
User created but transaction not committed yet
Transaction committed
```

---
