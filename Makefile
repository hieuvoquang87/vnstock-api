.PHONY: setup dev test lint format clean

# Setup development environment
setup:
	poetry install
	poetry env activate
	poetry export -f requirements.txt --output requirements.txt --without-hashes

# Run development server
dev:
	uvicorn app.main:app --reload --port 8000

# Run tests
test:
	pytest -v

# Check code with linters
lint:
	flake8 app tests
	mypy app tests

# Format code
format:
	black app tests
	isort app tests

# Clean up cache files
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +

# Install dev dependencies (linting, formatting)
dev-deps:
	poetry add --group dev flake8 mypy black isort pytest-cov

# Run API with production settings
prod:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

# Create application directories
dirs:
	mkdir -p app/{api/{rest/v1/{stocks,market},graphql/resolvers},services,datasources,repositories,models/{domain,schemas,entities},infrastructure/{auth,cache,database}}
	mkdir -p tests/{unit,integration}
	touch app/__init__.py
	touch app/api/__init__.py
	touch app/api/rest/__init__.py
	touch app/api/rest/v1/__init__.py
	touch app/api/graphql/__init__.py 