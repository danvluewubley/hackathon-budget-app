# Budget Made Simple
A web application to help users manage their budgeting efficiently. This app allows users to log in, track their spending, and view their budgeting dashboard.

## Features
* User authentication (sign up, log in, log out)
* Dashboard for budgeting overview
* Flash messages for user feedback
* Bootstrap for responsive design

## Installation
Follow these steps to set up and run the Flask project locally.

### Prerequisites
Ensure you have the following installed on your machine:
* Python 3.6+
* pip

### Steps
1. Clone the Repository
```
git clone https://github.com/danvluewubley/hackathon-budget-app.git
cd hackathon-budget-app
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
5. Set Environment Variables
 * On Windows:
```
set FLASK_APP=app
```
* On macOS and Linux:
```
export FLASK_APP=app
```
6. Start the Flask application with:
```
flask run
```
7. Access the Application
Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage
* Sign Up: Create a new account.
* Login: Access your dashboard by logging in.
* Dashboard: View and manage your budget.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature-name).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature/your-feature-name).
6. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/danvluewubley/hackathon-budget-app/blob/main/LICENSE) file for details.
