# E2E Test Company 2 — Code

This directory contains the technical implementation for **e2e-1773572856**.

## Project Structure

```
code/
├── README.md          # This file — project overview and structure
├── hello.py           # Proof-of-work: Hello World script
├── TECH.md            # Stack decisions and rationale
└── app/
    ├── main.py        # FastAPI health-check endpoint
    └── tests/
        └── test_main.py  # Unit tests for the health-check endpoint
```

## Getting Started

### Prerequisites
- Python 3.9+
- pip

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the API locally
```bash
uvicorn app.main:app --reload
```

### Run tests
```bash
pytest app/tests/
```

## Endpoints

| Method | Path       | Description                    |
|--------|------------|--------------------------------|
| GET    | `/health`  | Returns company status as JSON |

## Notes
- This codebase is scaffolded and maintained autonomously by the Developer agent.
- See `TECH.md` for architecture and stack decisions.
