# library-MS
This project is a simple backend system built using Django to manage students and books for a library. It provides basic functionality for handling student registrations, displaying a list of available books, and managing the borrowing and returning of books. The project follows a Model-View-Template (MVT) pattern, utilizing Django's robust framework for handling backend logic, database models, and rendering HTML templates.
How to Run the Project:

To run the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/library-management-api.git
    cd library-management-api
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv myproject
    source env/bin/activate  # Windows: env\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Start the server**:
    ```bash
    python manage.py runserver
    ```

6. Access the app at `http://127.0.0.1:8000/`.

---

# 1.Student Model:
The `Student` model contains information about students registered in the library system. It has the following fields:
- `Student_name`: A `CharField` to store the student's full name.
- `register_id`: A unique identifier for each student.
- `Student_contact`: Contact information for the student.
- `active`: A `BooleanField` that marks whether the student is currently active in the system.

Usage: This model is used to store and retrieve student information in the views.

---
# 2. Views

# Admin View :
- **URL**: `/admin/`
- **Description**: Displays the Admin page. This view renders `Admin.html` and passes the current tab (`"Admin"`) to the context.

#### **Students View**:
- **URL**: `/students/`
- **Description**: Renders a list of all students stored in the database, passing the list to `Student.html` for display.

#### **Save Student**:
- **URL**: `/save-student/`
- **Description**: Handles the registration of a new student. It extracts form data from the request and saves a new student record to the database, then redirects back to the students list.

#### **Books View**:
- **URL**: `/books/`
- **Description**: Displays the `Books.html` page.

#### **Returns View**:
- **URL**: `/returns/`
- **Description**: Renders the `Returns.html` page .

---

### 3. Templates

#### **Admin.html**
- Displays the Admin interface, where administrative tasks can be managed.

#### **Student.html**
- Shows a table of all registered students fetched from the database.

#### **Books.html**
- A placeholder page where available books will be displayed.

#### **Returns.html**
- A placeholder page for managing book returns.

---

### 4. Endpoints

| Method | URL            | Description                              |
|--------|----------------|------------------------------------------|
| GET    | `/admin/`       | Renders the Admin page                   |
| GET    | `/students/`    | Fetches and displays the list of students|
| POST   | `/save-student/`| Saves a new student to the database      |
| GET    | `/books/`       | Displays the Books page                  |
| GET    | `/returns/`     | Displays the Returns page                |

---

### 5. Form Handling

The `save_student` view handles form submissions for adding new students. The form data is extracted from the `POST` request and used to create a new `Student` record, which is then saved to the database.

**Form Fields**:
- `Student_name`
- `register_id`
- `Student_contact`

# 6. Possible features to add in the future:
- Add more functionality for book management (CRUD operations for books).
- Implement book borrowing and return functionalities.
- Add validation to the student registration form.
- Enhance the Admin page to provide detailed reports on library activity.
- Improve security by implementing role-based access control (RBAC) for admin and student roles.
- Integrate testing and API documentation using Swagger/OpenAPI standards.




