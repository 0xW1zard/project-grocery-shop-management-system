# 🛒 Grocery Store Web Application

This is a **3-tier web application** for managing a grocery store, built using **Python, Flask, MySQL**, and **HTML/CSS/JS/Bootstrap**.

---

## 🧱 Application Architecture

1. **Frontend**: HTML, CSS, JavaScript, Bootstrap  
2. **Backend**: Python, Flask  
3. **Database**: MySQL

---

## 📸 Screenshot

![Homepage](homepage.jpg)

---

## 🚀 Features

- Add, update, and delete grocery items
- Inventory management with real-time database
- Responsive web interface
- Clean design using Bootstrap
- **NEW**: Delete functionality for both orders and products
- **NEW**: Enhanced security with parameterized queries
- **NEW**: Improved UI with action buttons

---

## 🛠️ Installation Instructions

1. Install MySQL:  
   [Download MySQL](https://dev.mysql.com/downloads/installer/)

2. Install required Python packages:

```bash
pip install -r backend/requirements.txt
```

3. Set up the database:
```bash
mysql -u root -p < database/grocery_store.sql
```

4. Run the application:
```bash
cd backend
python server.py
```

5. Open your browser and go to: `http://127.0.0.1:5000`

---

## 🔧 Recent Enhancements

- ✅ Delete order functionality with proper foreign key handling
- ✅ Enhanced delete product functionality with security improvements
- ✅ Fixed CSS case sensitivity issues
- ✅ Added Action columns with delete buttons
- ✅ Improved UI with responsive design
- ✅ SQL injection protection
- ✅ Better error handling and user experience

---

## 📁 Project Structure

```
grocery-store-webapp/
├── backend/          # Flask server and Python backend
├── database/         # MySQL schema and data
├── ui/              # Frontend HTML, CSS, and JavaScript
└── README.md        # This file
```
