# ViFolio
This project is a web application built using the Flask framework in Python. The application is designed to showcase your portfolio of projects and allow visitors to view them, filter them by type, and view details about each project.

## Technologies
The web application is built using the **Flask** framework in Python. The data for the projects is stored in a **SQLite database**, and the application also uses various Flask extensions such as : 
* Flask-Login for user authentication, 
* Flask-Mail for sending emails
* Flask-Bootstrap and Flask-CKEditor for styling and rich text editing, respectively.

## Getting Started
here are the instructions to get the project up and running on a local machine:

1. Clone the repository to your local machine using `git clone https://github.com/your-username/your-repo.git`.

1. Install the required dependencies by running ``pip install -r requirements.txt`` in your terminal.

1. Create a file called `.env` in the root directory of your project and add the following environment variables:
```
SECRET_KEY_FLASK=<your-secret-flask-key>
MAIL_USERNAME_VE=<your-gmail-address>
MAIL_PASSWORD_APP_VE=<your-gmail-password>
PHONE_NUMBER=<your-phone-number>
```

4. Create a local instance of the SQLite database by running **python** in your terminal and executing the following commands:
```
from main import db
db.create_all()
exit()
```
5. Run the application by running `python main.py` in your terminal.

6. Open your web browser and go to http://localhost:5000 to view the application.

That's it! You should now be able to see and interact with the application on your local machine.

## Usage
A venir

## Contact

Feel free to contact me for any questions or feedback:

* **Name:** Velda MB.
* **Email:** veldambayen@gmail.com
* **LinkedIn:** www.linkedin.com/in/al-velda-de-mbayen
* **Website:** www.vifolio.com

You can also find me on [GitHub](https://github.com/Rhejna).
