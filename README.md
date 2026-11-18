# Expense Tracker (Mini)

A small, realistic Python project used to test the **Prod-to-PR** agent on a real-ish codebase.

## Features
- Add expenses
- Calculate total spending
- Calculate remaining budget
- Summarize spending by category

## Setup & test
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Known issue (for testing)
There is a bug in `remaining_budget`: it does not subtract expenses correctly in all cases. See the GitHub issue labeled `ai-fix` for details.
