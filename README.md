# QuizMe Application

This is a **Django-based web application** designed to run locally on your machine. Follow the instructions below to set up and run the project.


## **Project Overview**

- **Framework:** Django  
- **Project Name:** Quiz  
- **App Name:** QuizMe

---

## **Directory Structure**

Here is the basic structure of the project:

```plaintext
QGIS_app/                       # Project-level folder
│
├── QGIS_app/                   # Configuration files (project level)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── QGIS/                       # App-level folder
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/              # HTML Templates
│   ├── static/                 # Static Files (CSS, JS, images)
│   └── migrations/             # Database Migrations
│
├── db.sqlite3                  # SQLite Database (created after migration)
├── manage.py                   # Django Management File
└── README.md                   # Project Documentation
```

---

## **How to Run the Project Locally**

Follow the steps below to set up and run the project on your system.

### **1. Clone the Repository**

First, clone the project repository from GitHub:

```bash
git clone <https://github.com/AbhishekKumar0313/QuizMe->
cd Quiz
```


### **2. Install Required Libraries**

Install the necessary dependencies for the project:

```bash
pip install django
```

---

### **3. Apply Migrations**

Navigate to the project-level folder (where `manage.py` is located) and apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **4. Run the Development Server**

Start the Django development server using the command:

```bash
python manage.py runserver
```

Once the server starts successfully, you will see an output similar to this:

```plaintext
Starting development server at http://127.0.0.1:8000/
```

---

### **5. View the Application**

Open a web browser and go to:

```
http://127.0.0.1:8000/
```

You should now see the application running.

---

## **Troubleshooting**

If you encounter any issues, here are some common solutions:

1. **"ModuleNotFoundError: No module named 'django'"**  
   Run the following command to install Django:  
   ```bash
   pip install django
   ```

2. **Database Errors**  
   Ensure you run migrations properly using:  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---
## **Screenshots**
![Login Page](https://github.com/AbhishekKumar0313/QuizMe-/blob/master/Screenshot%202024-12-18%20125418.png)
![Home Page](https://github.com/AbhishekKumar0313/QuizMe-/blob/master/Screenshot%202024-12-18%20125459.png)
![Quiz Page](https://github.com/AbhishekKumar0313/QuizMe-/blob/master/Screenshot%202024-12-18%20125614.png)
![Result Page](https://github.com/AbhishekKumar0313/QuizMe-/blob/master/Screenshot%202024-12-18%20125626.png)
