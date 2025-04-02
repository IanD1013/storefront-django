# Django Storefront

A full-featured e-commerce backend built with Django and Django REST Framework, following the [Ultimate Django Series](https://codewithmosh.com/p/the-ultimate-django-series) course.

## Features

- RESTful API with Django REST Framework
- JWT Authentication
- MySQL Database Integration
- Redis Caching
- Celery for Background Tasks
- Automated Testing with pytest
- Performance Optimization
- Content Types Framework
- Generic Relationships
- Django Admin Integration

## Tech Stack

- Python 3.x
- Django
- Django REST Framework
- MySQL
- Redis
- Celery
- pytest
- JWT Authentication

## Prerequisites

- Python 3.x
- MySQL Server
- Redis Server
- pipenv (for dependency management)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd storefront
```

2. Install dependencies:
```bash
pipenv install
```

3. Set up environment variables:
Create a `.env` file in the root directory with:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=mysql://user:password@localhost:3306/dbname
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Testing

Run tests with pytest:
```bash
pytest
```

## Project Structure

- `store/` - Main application module
- `core/` - Core functionality and shared components
- `playground/` - Testing and development playground
- `tags/` - Tag management system
- `likes/` - Like functionality
- `media/` - User-uploaded media files
- `locustfiles/` - Load testing configurations