# Budget App

## Installation
Follow these steps to set up and run the Flask project locally.

### Prerequisites
Ensure you have the following installed on your machine:
* Python 3.6+
* pip

### Steps
1. Clone the Repository
```
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

2. Create a Virtual Environment
It's a good practice to create a virtual environment to isolate the project's dependencies.
```
python3 -m venv venv
```
3. Activate the Virtual Environment
  * On Windows:
```
venv\Scripts\activate
```
  * On macOS and Linux:
```
source venv/bin/activate
```
4. Install Dependencies
Install the required Python packages using pip.
```
pip install -r requirements.txt
```
5. Start the Flask application with:
```
flask run
```
6. Access the Application
Open your web browser and navigate to `http://127.0.0.1:5000`.

### Additional Notes
* **Static Files**: Ensure your static files (CSS, JS, images) are correctly referenced in your templates.
* **Modals and Flash Messages**: Ensure Bootstrap and other dependencies are correctly included in your HTML templates.
* **Database Configuration**: Customize the database settings in the .env file as needed for your environment.

### Troubleshooting
If you encounter any issues during installation, please check the following:
* Ensure all dependencies are installed correctly.
* Verify that the virtual environment is activated.
* Check for any error messages in the terminal and address them accordingly.
