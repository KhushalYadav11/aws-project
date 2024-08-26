from flask import Flask, render_template, request
import boto3
import pymysql
import os
from config import *

app = Flask(__name__)

db_conn = pymysql.connect(
    host=customhost,
    user=customuser,
    password=custompass,
    db=customdb,
    port=3306
)

custombucket = custombucket
region = customregion

@app.route("/", methods=['GET', 'POST'])
def home():
    print("Current working directory:", os.getcwd())
    print("Templates directory contents:", os.listdir('templates'))
    return render_template('AddEmp.html')

@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')

@app.route("/addemp", methods=['POST'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    pri_skill = request.form['pri_skill']
    location = request.form['location']
    emp_image_file = request.files['emp_image_file']

    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    if emp_image_file.filename == "":
        return "Please select a file"

    try:
        cursor.execute(insert_sql, (emp_id, first_name, last_name, pri_skill, location))
        db_conn.commit()

        emp_name = first_name + " " + last_name

        emp_image_file_name_in_s3 = "emp-id-" + str(emp_id) + "_image_file"
        s3 = boto3.resource('s3')

        try:
            print("Data inserted in MySQL RDS... uploading image to S3...")
            s3.Bucket(custombucket).put_object(Key=emp_image_file_name_in_s3, Body=emp_image_file)

            bucket_location = boto3.client('s3').get_bucket_location(Bucket=custombucket)
            s3_location = bucket_location['LocationConstraint']

            if s3_location is None:
                s3_location = ''
            else:
                s3_location = '-' + s3_location

            object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
                s3_location,
                custombucket,
                emp_image_file_name_in_s3
            )

            print("Image successfully uploaded to S3 at the following URL:")
            print(object_url)

        except Exception as e:
            return str(e)

    except Exception as e:
        return str(e)
    finally:
        cursor.close()

    return "Employee data successfully added with the image uploaded to S3"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
