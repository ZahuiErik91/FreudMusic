# Backend Guidelines

## Architecture
- Modular: Separate music generation, streaming, and API logic.
- Use environment variables for configuration (e.g., YouTube stream key).
- Document all modules and functions with docstrings.

## Code Standards
- Use Python 3.8+.
- Follow PEP8 style guide.
- Use type hints where possible.
- Write clear, descriptive function and variable names.
- Handle errors gracefully and log exceptions.

## API
- Use FastAPI or Flask for REST endpoints.
- Validate all incoming data.
- Return clear error messages and status codes.

## Testing
- Write unit tests for all major modules.
- Use pytest or unittest. 