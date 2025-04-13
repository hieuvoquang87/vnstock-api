.PHONY: setup dev test lint format clean

# Setup development environment
setup:
	pip install uv
	uv pip install -r pyproject.toml

# Run development server
dev:
	uv run uvicorn app.main:app --reload --port 8000

# Run tests
test:
	uv run pytest -v

# Check code with linters
lint:
	uv run flake8 app tests
	uv run mypy app tests

# Format code
format:
	uv run black app tests
	uv run isort app tests

# Clean up cache files
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +

# Install dev dependencies (linting, formatting)
dev-deps:
	uv add --group dev flake8 mypy black isort pytest-cov

# Run API with production settings
prod:
	uv run uvicorn app.main:app --host 0.0.0.0 --port 8000

# Create application directories
dirs:
	mkdir -p app/{api/{rest/v1/{stocks,market},graphql/resolvers},services,datasources,repositories,models/{domain,schemas,entities},infrastructure/{auth,cache,database}}
	mkdir -p tests/{unit,integration}
	touch app/__init__.py
	touch app/api/__init__.py
	touch app/api/rest/__init__.py
	touch app/api/rest/v1/__init__.py
	touch app/api/graphql/__init__.py 