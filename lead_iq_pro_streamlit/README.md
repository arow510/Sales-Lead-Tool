# LeadIQ Pro — AI-Powered Sales Lead Intelligence Platform

A Streamlit starter app for enterprise sales lead management with:

- CSV / Excel upload
- Dashboard KPIs
- Lead explorer and filters
- Rule-based lead scoring engine
- Lead detail view
- AI assistant placeholder
- Login-ready structure
- Database-ready structure

## 1. Create virtual environment

```bash
python -m venv .venv
```

Activate it:

### Windows PowerShell
```bash
.venv\Scripts\Activate.ps1
```

### macOS/Linux
```bash
source .venv/bin/activate
```

## 2. Install requirements

```bash
pip install -r requirements.txt
```

## 3. Run app

```bash
streamlit run app.py
```

## 4. Default login

```text
Username: admin
Password: admin123
```

Change this later before production.

## 5. Suggested next improvements

- Replace simple login with secure authentication
- Add Postgres or Snowflake database
- Add ML model training with historical conversion data
- Add OpenAI / Azure OpenAI outreach email generation
- Add audit logging
- Add user roles and row-level access
