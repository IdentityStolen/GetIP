# Deployment Guide for GetIP (Django)

## Deployment

To deploy this Django project on a production server:

1. **Choose a Hosting Provider**
   - Use a cloud provider (e.g., DigitalOcean, AWS, Azure) or a VPS.

2. **Install Dependencies on the Server**
   - Install Python 3, pip, and virtualenv.
   - Install a production web server (e.g., Gunicorn or uWSGI).
   - Install a reverse proxy (e.g., Nginx or Apache).

3. **Clone Your Repository**
   ```bash
   git clone <your-repo-url>
   cd GetIP
   ```

4. **Set Up a Virtual Environment and Install Requirements**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Configure Django for Production**
   - Set `DEBUG = False` in `Hello/settings.py`.
   - Set `ALLOWED_HOSTS` to your server’s domain or IP.
   - Collect static files:
     ```bash
     python manage.py collectstatic
     ```

6. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run Gunicorn (or uWSGI) as the Application Server**
   ```bash
   gunicorn Hello.wsgi:application --bind 0.0.0.0:8000
   ```

9. **Set Up Nginx as a Reverse Proxy**
   - Configure Nginx to forward requests to Gunicorn.
   - Serve static files directly from Nginx.

10. **Secure Your Server**
    - Set up a firewall.
    - Use HTTPS (e.g., with Let’s Encrypt).

11. **Monitor and Maintain**
    - Use process managers like systemd or supervisor to keep Gunicorn running.
    - Monitor logs and server health.

For more details, refer to the [Django deployment checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/) and your hosting provider’s documentation.

