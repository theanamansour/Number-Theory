import base64
import hashlib
import hmac
import os
import re
import secrets
from app.db import get_connection

EMAIL_REGEX = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"


def validate_email(email: str):
    if not re.match(EMAIL_REGEX, email):
        raise ValueError("Please enter a valid email address.")


def validate_username(username: str):
    username = username.strip()

    if len(username) < 2:
        raise ValueError("Username must be at least 2 characters long.")

    if len(username) > 30:
        raise ValueError("Username must be at most 30 characters long.")

    return username


def validate_password_strength(password: str):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

    if not any(c.islower() for c in password):
        raise ValueError("Password must contain at least one lowercase letter.")

    if not any(c.isupper() for c in password):
        raise ValueError("Password must contain at least one uppercase letter.")

    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain at least one digit.")

    if not any(not c.isalnum() for c in password):
        raise ValueError("Password must contain at least one special character.")


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    iterations = 100_000
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iterations)
    salt_b64 = base64.b64encode(salt).decode()
    dk_b64 = base64.b64encode(dk).decode()
    return f"pbkdf2_sha256${iterations}${salt_b64}${dk_b64}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        algorithm, iterations, salt_b64, dk_b64 = stored_hash.split("$")

        if algorithm != "pbkdf2_sha256":
            return False

        salt = base64.b64decode(salt_b64.encode())
        expected_dk = base64.b64decode(dk_b64.encode())

        new_dk = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt,
            int(iterations)
        )

        return hmac.compare_digest(new_dk, expected_dk)

    except Exception:
        return False


def get_user_by_email(email: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = %s",
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


def create_user(username: str, email: str, password: str):
    username = validate_username(username)
    email = email.strip().lower()

    validate_email(email)
    validate_password_strength(password)

    if get_user_by_email(email):
        raise ValueError("This email is already in use.")

    password_hash = hash_password(password)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (username, email, password_hash)
        VALUES (%s, %s, %s)
        RETURNING id, username, email, created_at
        """,
        (username, email, password_hash)
    )

    user = cursor.fetchone()

    conn.commit()

    cursor.close()
    conn.close()

    return dict(user)


def create_session_token(user_id: int) -> str:
    token = secrets.token_hex(32)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sessions (user_id, token)
        VALUES (%s, %s)
        """,
        (user_id, token)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return token


def login_user(email: str, password: str):
    email = email.strip().lower()
    user = get_user_by_email(email)

    if not user:
        raise ValueError("No account found with this email. Please create an account.")

    if not verify_password(password, user["password_hash"]):
        raise ValueError("Incorrect password. Please try again.")

    token = create_session_token(user["id"])

    return {
        "token": token,
        "user": {
            "id": user["id"],
            "username": user["username"],
            "email": user["email"],
            "created_at": user["created_at"]
        }
    }


def check_email_status(email: str):
    email = email.strip().lower()

    validate_email(email)

    user = get_user_by_email(email)

    return {
        "email": email,
        "available": user is None,
        "message": "Email is available." if user is None else "This email is already in use."
    }


def get_user_by_token(token: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT users.id, users.username, users.email, users.created_at
        FROM sessions
        JOIN users ON sessions.user_id = users.id
        WHERE sessions.token = %s
        """,
        (token,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return None

    return dict(user)


def delete_session_token(token: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM sessions WHERE token = %s",
        (token,)
    )

    conn.commit()
    deleted = cursor.rowcount

    cursor.close()
    conn.close()

    return deleted > 0