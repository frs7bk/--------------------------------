# Portfolio Website Deployment on Render

## Deployment Instructions

1. Extract this ZIP file
2. Upload the files to a Git repository
3. Create a new Web Service in Render connected to your repository
4. Configure the service with these settings:
   - Build Command: `pip install -r render-requirements.txt && python render_setup.py`
   - Start Command: `gunicorn --bind 0.0.0.0:$PORT --workers 2 app:app`
5. Set the following environment variables:
   - DATABASE_URL: Your PostgreSQL database URL
   - FLASK_SECRET_KEY: A random secret key
   - SESSION_SECRET: A random session secret
   - FLASK_APP: app.py
   - FLASK_ENV: production

## Important Notes

- The first deployment may take a few minutes to complete
- Database tables will be created automatically on first run
- You may need to create an admin user manually after deployment
