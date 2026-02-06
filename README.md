# Valentine's Website

A tiny Python + HTML Valentine's page.

## Local run

```bash
python3 app.py
```

Then open `http://localhost:8000/index.html`.

## Render deploy settings

Use these commands in Render:

- **Build Command:** `echo "No build step required"`
- **Start Command:** `python3 app.py`

`python` may not exist in Render containers, but `python3` does.
