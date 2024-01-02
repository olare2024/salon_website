# Salon Website

Welcome to the Salon Website project! This web application is built using Django and MySQL to manage salon services, appointments, and client information.

## Features

- **Appointment Management:** Schedule, view, and manage salon appointments.
  
- **Service Catalog:** Maintain a catalog of salon services, including details and pricing.

- **Staff Management:** Keep track of salon staff, their schedules, and assigned services.

- **Client Profiles:** Manage client information, including appointment history and preferences.

## Technologies Used

- **Backend Framework:** [Django](https://www.djangoproject.com/)
  
- **Database:** [MySQL](https://www.mysql.com/)

## Setup

### Prerequisites

- [Python](https://www.python.org/) (version 3.x)
- [MySQL](https://www.mysql.com/)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/olare2024/salon_website.git
    cd salon_website
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure database settings:

    - Create a MySQL database for the project.
    - Copy the `.env.example` file to `.env` and update the database configuration.

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Access the admin interface to manage services, staff, and other data:

    ```bash
    python manage.py createsuperuser
    ```

    Visit `http://localhost:8000/admin` and log in using the superuser credentials.

2. Explore the main website for features such as appointment scheduling and client profiles.

## Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, please open an [issue](https://github.com/olare2024/salon_website/issues) or submit a [pull request](https://github.com/olare2024/salon_website/pulls).

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For inquiries and support, please contact [your.email@example.com].
