# rt_backend/Dockerfile
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

# Port to expose
EXPOSE 8000

CMD ["gunicorn", "rt_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
