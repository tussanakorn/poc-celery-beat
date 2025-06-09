# Celery & Celery Beat Proof of Concept

A simple proof-of-concept project demonstrating the use of [Celery](https://docs.celeryq.dev/) and [Celery Beat](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html) for distributed task processing and periodic task scheduling in Python.

## Features

- Asynchronous task processing with Celery
- Periodic task scheduling using Celery Beat
- RabbitMQ message broker with Docker Compose
- Fast Python package management with uv
- Redis support with RedisInsight UI
- Easy-to-understand project structure

## Getting Started

### Prerequisites

- Python 3.8+
- [uv](https://docs.astral.sh/uv/) - Ultra-fast Python package installer
- Docker & Docker Compose (for message brokers)

### Installation

1. **Install uv** (if not already installed):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and setup the project:**

   ```bash
   git clone https://github.com/yourusername/poc-celery.git
   cd poc-celery

   # Create virtual environment and install dependencies
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install "celery[rabbitmq]"
   ```

3. **Start services using Docker:**

   ```bash
   # Start RabbitMQ (recommended)
   docker compose up -d rabbitmq

   # Or start Redis if preferred
   docker compose up -d redis
   ```

### Running the Project

1. **Start the Celery worker:**

   ```bash
   celery -A tasks worker --loglevel=info
   ```

2. **Start Celery Beat for periodic tasks:**

   ```bash
   celery -A scheduler beat --loglevel=info
   ```

3. **Test tasks in Python:**

   ```python
   from tasks import hello
   result = hello.delay('World')
   print(result.get())  # Output: Hello, World
   ```

## Project Structure

- `tasks.py` - Basic async task examples
- `scheduler.py` - Periodic task scheduling examples  
- `docker-compose.yml` - Redis and RabbitMQ services
- `README.md` - This file

## Services & UIs

- **RabbitMQ Management**: http://localhost:15672 (guest/guest)
- **RedisInsight**: http://localhost:5540 (Redis monitoring)

## Development with uv

Add new dependencies:

```bash
uv pip install package_name
```

Generate requirements.txt:

```bash
uv pip freeze > requirements.txt
```

Create/sync from pyproject.toml:

```bash
uv pip install -e .
```

## Example Tasks

The project includes:
- `hello(name)` - Simple async task with 5-second delay
- `print_time()` - Periodic task that prints current time every 10 seconds
