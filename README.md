# ALX Django Learning Lab

A collection of Django learning exercises and projects completed while building backend development fundamentals.

## Project

The main Django project is in `LibraryProject/`.

It currently includes exercises covering:

- Django project and application structure
- Models and database relationships
- Django admin
- CRUD operations
- Custom model permissions
- User profiles and roles
- Django ORM queries
- Forms and signals
- Authentication and authorization concepts

## Structure

```text
LibraryProject/
├── manage.py
├── LibraryProject/        # Django project configuration
└── apps/
    ├── bookshelf/         # Book model and CRUD exercises
    └── relationship_app/  # Relationships, roles, permissions, and ORM exercises
```

## Running locally

From the `LibraryProject/` directory:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install django
python manage.py migrate
python manage.py runserver
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Then open the local development server shown by Django.

## Configuration

The project keeps the Django secret out of source control. For local development, `DJANGO_SECRET_KEY` may be supplied through the environment. `DEBUG` and `ALLOWED_HOSTS` can also be configured with environment variables.

Do not use development defaults in a production deployment.

## Learning notes

The repository intentionally preserves coursework exercises and their progression. Documentation is improved for clarity without rewriting the underlying learning work merely for cosmetic reasons.
