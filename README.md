# GetIP

This repository is created using copilot agent via prompt engineering using GPT-4.1 model.
GetIP is a simple Django web application that displays the user's IP address (either IPv4 or IPv6) after they enter their name. It demonstrates basic Django form handling, template rendering, and how to extract the client IP address from a request.

## Features
- Enter your name and see a personalized greeting.
- Detects and displays your IPv4 and/or IPv6 address.

## Project Structure
- `Hello/` - Main Django project settings and configuration.
- `helloapp/` - Django app containing views, URLs, and templates.
- `helloapp/templates/helloapp/ask_name_and_show_ip.html` - Main HTML template for user interaction.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd GetIP
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Django:**
   ```bash
   pip install django
   ```
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
6. **Open your browser and visit:**
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage
- Enter your name in the form and submit.
- The app will greet you and show your detected IP address(es).

## Notes
- This project is for demonstration and educational purposes.
- Do not use DEBUG=True in production.
- The app does not store any user data.

## License
MIT License
