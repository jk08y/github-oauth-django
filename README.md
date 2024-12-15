# Django GitHub OAuth Login Project

## Overview

This is a Django web application that implements GitHub OAuth authentication, allowing users to log in to the application using their GitHub credentials. The project demonstrates a clean, secure way of integrating social authentication into a Django web application.

## Features

- GitHub OAuth 2.0 Authentication
- Secure login process
- User profile page
- Environment variable management
- Simple and clean UI

## Prerequisites

- Python 3.8+
- pip
- GitHub Account
- GitHub OAuth Application

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/jko8y/github-oauth-django.git
cd github-oauth-django
```

### 2. Create Virtual Environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. GitHub OAuth Setup

1. Go to [GitHub Developer Settings](https://github.com/settings/developers)
2. Click "New OAuth App"
3. Fill in the details:
   - **Homepage URL**: `http://localhost:8000`
   - **Authorization callback URL**: `http://localhost:8000/social-auth/complete/github/`
4. Generate a **Client ID** and **Client Secret**

### 5. Configure Environment Variables

Create a `.env` file in the project root with the following content:

```
DJANGO_SECRET_KEY=your_django_secret_key
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
```

**Note**: Generate a secure Django secret key using Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 6. Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## Project Structure

```
github_oauth_project/
│
├── github_oauth_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── accounts/
│           ├── login.html
│           └── profile.html
│
├── .env
└── requirements.txt
```

## Authentication Flow

1. User clicks "Login with GitHub"
2. Redirected to GitHub OAuth page
3. User grants permissions
4. GitHub sends authorization code
5. Application exchanges code for access token
6. User is logged in and redirected to profile

## Security Considerations

- Never commit `.env` file to version control
- Use strong, unique secret keys
- Keep GitHub OAuth credentials confidential
- Use HTTPS in production

## Customization

- Modify `accounts/views.py` to add custom logic
- Customize templates in `accounts/templates/`
- Extend user model if needed

## Troubleshooting

- Ensure all dependencies are installed
- Check GitHub OAuth app settings
- Verify environment variables
- Clear browser cache if login issues persist

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

JK - [Lets connect on 𝕏](https://x.com/jk08y)
