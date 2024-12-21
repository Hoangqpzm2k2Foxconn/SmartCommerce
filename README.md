
# SmartCommerce

A Django-based e-commerce platform with integrated payment processing, online courses, and software marketplace.

## Features

- Secure payment processing
- Online course platform
- Software marketplace
- RESTful API
- Docker support

## Documents

Please view in `Software-Development-and-Life-Cycle` for more information

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Copy `.env.example` to `.env` and configure
4. Install dependencies: `pip install -r requirements/local.txt`
5. Run migrations: `python manage.py migrate`
6. Start development server: `python manage.py runserver`

## Docker Setup

```bash
docker-compose up --build
```

## Testing

```bash
pytest
```

## License

MIT
