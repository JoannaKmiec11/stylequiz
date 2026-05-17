# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A Flask web app that runs a 40-question communication style quiz. Users answer forced-choice questions and receive a result identifying their dominant communication style (Action, Process, People, or Idea) — inspired by the Ned Herrmann model.

## Running the app

```bash
# Activate venv first (Windows)
venv\Scripts\activate

# Set required environment variable
set SECRET_KEY=your-secret-key-here

# Run development server
python app.py
# App runs on http://0.0.0.0:5000 with debug=True
```

`SECRET_KEY` is required — Flask sessions will not work without it. No build step, no test suite, no linter configured.

## Architecture

All data lives in static Python dicts — **no database is used** despite `Flask-SQLAlchemy` being listed in `requirements.txt`.

**Quiz flow:**
1. `/` — landing page, links to `/question/`
2. `/question/<number>` (1–40) — shows two answer choices; POST stores the selected answer's style ID (1–4) in `session[number]`, then redirects to next question
3. `/result/` — tallies session values per style, clears session, renders result

**Scoring logic in `app.py:result()`:** Each answer in `seed_data/questions.py` maps directly to a style integer (1–4). The result route sums all style votes, finds the max, and handles ties by rendering `your_styles.html` instead of `your_style.html`.

**Known bug:** The tie-detection loop at `app.py:46` compares `if key == style` where `style` is the last value from the session-scanning loop above — it should be `comm_styles[0]`. This means ties may be detected incorrectly.

## Key files

- `app.py` — all routes; Flask session holds quiz state between questions
- `seed_data/questions.py` — dict of 40 questions; each entry maps two answer strings → style ID
- `seed_data/styles.py` — dict of 4 style definitions (Name, Description, People)
- `templates/` — Jinja2 templates; `your_style.html` (single result) vs `your_styles.html` (tied result)
- `static/styles/main.css` — uses Poppins from Google Fonts; teal accent `rgb(43, 214, 180)`

## Notes

- A database layer is planned (Flask-SQLAlchemy is already in `requirements.txt`) but not yet implemented — all data is currently static dicts

