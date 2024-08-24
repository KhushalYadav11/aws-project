Employee Management Flask App
This project is a Flask web application for managing employee records. It allows users to add employee details and upload images to an AWS S3 bucket. The employee data is stored in an AWS RDS MySQL database.

Project Structure
EmpApp.py: The main Flask application file.
config.py: Contains configuration details for connecting to the MySQL RDS instance and S3 bucket.
templates/: Directory containing HTML templates for the Flask application.
AddEmp.html: Form to add employee details.
about.html: About page template.

Prerequisites:
-Python 3.x
-Flask
-PyMySQL
-Boto3
-An AWS account with RDS and S3 services configured

Setup
1. Clone the Repository

2. Install Dependencies
Create a virtual environment and install the necessary packages.

3. Configure config.py
Ensure config.py contains the following configuration with your RDS and S3 details

4. Create HTML Templates
Create the templates directory in the root of your project if it doesn't exist. Add the following HTML files:
'templates/AddEmp.html'

Running the Application
Start the Flask application: python EmpApp.py
Visit http://127.0.0.1:8080 in your web browser to access the application.



Troubleshooting
-TemplateNotFound Error: Ensure the HTML templates are placed in the templates directory.
-ModuleNotFoundError: Install the necessary Python packages within your virtual environment.

Contributing
Feel free to submit issues or pull requests.
