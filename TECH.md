# TECH.md — Stack Decisions & Rationale

_Last updated: 2026-03-26 | Author: Developer Agent_

---

## Language: Python 3

**Why:** Python is the default choice for rapid prototyping and backend services in this system. It has excellent library support, and the team (Philip) is comfortable with it. The hello.py proof-of-work was already written in Python, so continuing in the same language keeps the stack consistent.

---

## API Framework: FastAPI

**Why:**
- Lightweight and fast — suitable for a simple health-check endpoint
- Auto-generates OpenAPI docs (Swagger UI) at `/docs` out of the box
- Async-capable, though not needed at this scale
- Aligns with Philip's stated preference (USER.md: "FastAPI or Node for backend")
- Easy to write unit tests against using `TestClient` from `httpx`/`starlette`

**Alternative considered:** Flask — simpler, but lacks built-in type hints and auto-docs. FastAPI is the better forward-looking choice.

---

## Testing: pytest + httpx

**Why:**
- `pytest` is the Python testing standard — minimal setup, clear output
- `httpx` (via `starlette.testclient`) lets us test FastAPI routes without running a live server
- Keeps test setup fast and self-contained

---

## Deployment Target: Vercel

**Why:**
- Philip explicitly prefers Vercel as a deployment platform
- FastAPI can be deployed to Vercel via the `@vercel/python` runtime with a `vercel.json` config
- Zero-config SSL, global CDN, free tier sufficient for this use case

---

## Directory Structure

```
code/
├── README.md          # Project overview and structure
├── TECH.md            # This file — stack decisions
├── hello.py           # Sprint 1 proof-of-work script
├── app/
│   ├── main.py        # FastAPI application entry point
│   └── tests/
│       └── test_main.py  # Unit tests for the health-check endpoint
├── requirements.txt   # Python dependencies
└── vercel.json        # Vercel deployment configuration
```

---

## Dependency Management

Dependencies will be pinned in `requirements.txt` for reproducibility. No virtual environment is committed — consumers should create their own with `python -m venv .venv && pip install -r requirements.txt`.
