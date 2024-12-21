
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements/base.txt requirements/base.txt
COPY requirements/production.txt requirements/production.txt
RUN pip install -r requirements/production.txt

# Copy project
COPY . .

# Run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input
