# FastAPI Web Application

A modern Python web application built with FastAPI, featuring RESTful API endpoints, request validation, and comprehensive testing.

## Features

- **FastAPI Framework**: High-performance async web framework
- **Pydantic Validation**: Automatic request/response validation
- **CORS Support**: Cross-Origin Resource Sharing enabled
- **Comprehensive Tests**: Unit tests with pytest
- **API Versioning**: v1 API structure for future versioning
- **Configuration Management**: Environment-based settings
- **Dependency Injection**: Built-in dependency management

## Project Structure

```
INFO-5731/
├── src/                      # Source code
│   ├── __init__.py
│   ├── main.py              # Main FastAPI application
│   ├── config.py            # Configuration settings
│   ├── dependencies.py       # Dependency injection
│   ├── models/              # Data models
│   │   ├── __init__.py
│   │   └── schemas.py       # Pydantic schemas
│   └── api/                 # API routes
│       └── v1/              # API v1
│           ├── __init__.py
│           └── routes.py    # Route endpoints
├── tests/                   # Test suite
│   ├── __init__.py
│   └── test_main.py         # Main tests
├── requirements.txt         # Project dependencies
├── pyproject.toml          # Project configuration
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Requirements

- Python >= 3.9
- FastAPI
- Uvicorn
- Pydantic
- pytest (for testing)

## Installation

### 1. Create and activate virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. (Optional) Install development dependencies

```bash
pip install -e ".[dev]"
```

## Running the Application

```bash
# Using uvicorn directly
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# The application will be available at:
# http://localhost:8000
```

### API Documentation

Once running, access the interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Health Check
- `GET /health` - Check application health

### Items (Example endpoints)
- `GET /api/v1/items` - Get all items
- `GET /api/v1/items/{item_id}` - Get specific item
- `POST /api/v1/items` - Create new item
- `PUT /api/v1/items/{item_id}` - Update item
- `DELETE /api/v1/items/{item_id}` - Delete item

## Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=src tests/
```

## Environment Variables

Create a `.env` file in the project root:

```
APP_NAME=FastAPI Application
DEBUG=False
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Development

### Code Formatting
```bash
black src/ tests/
```

### Code Linting
```bash
flake8 src/ tests/
```

### Type Checking
```bash
mypy src/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Happy coding! 🚀**
