# Flask and Vue.js CRUD Application with MongoDB

This project is a full-stack web application for managing users, built with Flask for the backend, Vue.js for the frontend, and MongoDB as the database. It includes a Python script to import user data into MongoDB and a Vue.js-powered interface to manage users through a CRUD interface.

---

## Features

### Backend (Flask):
- **Data Import**: A Python script (`parser.py`) to import user data from a JSON file into MongoDB.
- **API Endpoints**:
  - Create, retrieve, update, and delete user records.
  - Serve static files for the frontend.
- **Error Handling**: Robust error responses for invalid inputs and unexpected issues.
- **CORS Support**: Cross-origin requests enabled for smooth frontend-backend integration.

### Frontend (Vue.js):
- **Dynamic User Interface**: Built with a UI library for intuitive design (e.g., Vuetify).
- **CRUD Operations**:
  - View users in a paginated table.
  - Create and edit users with modal forms.
  - Delete users with confirmation dialogs.
- **User Details Page**: Displays all details of a user and allows editing or deleting.

---

## Prerequisites

### General:
- Python 3.8+
- Node.js 16+
- MongoDB (local or cloud instance)

### Libraries/Dependencies:
- Flask
- Flask-PyMongo
- Flask-CORS
- Vue.js
- A Vue.js UI library (e.g., Vuetify)

---

## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:tecnodiniz/functional-users-crud.git
cd project
```

---

### 2. Backend Setup

Navigate to the backend folder and set up the virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

#### Configure MongoDB
Ensure MongoDB is running locally or provide a valid URI. Update `parser.py` and `app.py` if necessary.

#### Import Data
Run the `parser.py` script to import user data into MongoDB:
```bash
python parser.py
```

#### Start the Flask Server
```bash
python app.py
```
The backend server will run at `http://127.0.0.1:5000`.

---


### 3. Frontend Setup

# Frontend (Vue.js)
The frontend is already built and located in the static directory of the backend. If you need to rebuild it:

Navigate to the frontend folder and install dependencies:
```bash
cd ../frontend
npm install
```

#### Build the Frontend
```bash
npm run build
```
This will generate production files in the `../backend/static` folder.

---

### 4. Run the Application

Open a browser and visit:
```text
http://127.0.0.1:5000
```

---

## API Endpoints

### Home Route
**`GET /`**
- Serves the Vue.js frontend.

### Create User
**`POST /users`**
- **Body**: JSON object with user details.
- **Response**: Confirmation of creation.

### Retrieve All Users
**`GET /users`**
- **Response**: List of all users.

### Retrieve a User
**`GET /users/<id>`**
- **Response**: User details or 404 if not found.

### Update User
**`PUT /users/<id>`**
- **Body**: JSON object with updated details.
- **Response**: Confirmation of update or 404 if not found.

### Delete User
**`DELETE /users/<id>`**
- **Response**: Confirmation of deletion or 404 if not found.

---

## Project Structure

```text
project/
├── backend/
│   ├── app.py               # Flask backend
│   ├── parser.py            # Data import script
│   ├── users.json           # User data file
│   ├── static/              # Frontend production files
│   └── requirements.txt     # Backend dependencies
├── frontend/
│   ├── src/
│   │   ├── components/      # Vue components
│   │   ├── routes/          # Vue routes
│   │   ├── views/           # MainPage.vue, UserDetail.vue
│   │   └── App.vue          # Vue app entry point
│   ├── public/              # Static files (e.g., index.html)
│   └── package.json         # Frontend dependencies
└── README.md                # Project instructions
```

---

## Example Usage

Use tools like Postman or cURL to test the API.

### Create a User
```bash
curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d '{"username": "JohnDoe", "roles": ["admin"], "preferences": {"timezone": "UTC"}}'
```

### Fetch All Users
```bash
curl http://127.0.0.1:5000/users
```

### Update a User
```bash
curl -X PUT http://127.0.0.1:5000/users/<user_id> \
-H "Content-Type: application/json" \
-d '{"username": "UpdatedName"}'
```

### Delete a User
```bash
curl -X DELETE http://127.0.0.1:5000/users/<user_id>
```

---

## Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Vue.js Documentation](https://vuejs.org/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [Vuetify](https://vuetifyjs.com/en/)

