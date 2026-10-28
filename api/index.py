"""Vercel entrypoint for SkinCheck (FastAPI).

Vercel treats files under api/ as serverless functions. This file only
re-exports the real app from app.main, so local development (run.py)
and Vercel use the same application object.

Note: the .h5 model is NOT in the repo (GitHub 100 MB limit, .gitignore).
On Vercel, face-scan AI will fail until a model is provided at runtime
(see VERCEL_NOTES.md) — the rest of the app (auth, dashboard, history)
still runs.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app  # noqa: E402,F401  (re-exported for Vercel)
