from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import mysql.connector
import pymysql

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# MySQL Configuration
try:
    db = pymysql.connect(
        host='localhost',
        user='harsh',
        password='123456789',
        database='easyapply_test'
    )
    if db.open:
        print("Connection to the database successfull!!")
except pymysql.Error as e:
    print(f'Error connecting to MySQL: {e}')

# Connect to MySQL
# db = mysql.connector.connect(**mysql_config)
cursor = db.cursor()

@app.get("/")
async def serve_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit")
async def submit_form(request:Request):
    data = await    request.json()
    name = data['name']
    email = data['email']
    message = data['message']
    print("Form Data:", name, email, message)
    # Insert data into MySQL
    sql = "INSERT INTO form_data (username, email, message) VALUES (%s, %s, %s)"
    values = (name, email, message)
    cursor.execute(sql, values)
    db.commit()

    return templates.TemplateResponse("success.html", {"request": request, "name": name})