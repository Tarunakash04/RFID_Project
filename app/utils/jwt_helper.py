# File: app/utils/jwt_helper.py

import jwt
import datetime
from typing import Dict, Any
from app.config import JWT_SECRET, JWT_ALGO, JWT_EXP_DELTA_SECONDS

class JWTError(Exception):
    """Custom exception for JWT errors."""
    pass

def create_token(payload: Dict[str, Any]) -> str:
    """
    Generate a signed JWT token with standard claims.
        Args:
        payload (dict): User-specific information, e.g., {"sub": "user_id", "role": "student"}
        Returns:
        str: Signed JWT token
    """
    now = datetime.datetime.utcnow()
    payload.update({
        "iat": now,
        "exp": now + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    })
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)
    return token

def verify_token(token: str) -> Dict[str, Any]:
    """
    Verify a JWT token and return its payload.
        Args:
        token (str): JWT token string
        Returns:
        dict: Decoded payload if valid
        Raises:
        JWTError: If token is expired or invalid
    """
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        return decoded
    except jwt.ExpiredSignatureError:
        raise JWTError("Token has expired")
    except jwt.InvalidTokenError:
        raise JWTError("Token is invalid")

def decode_token_unverified(token: str) -> Dict[str, Any]:
    """
    Decode a JWT without verifying signature (for debugging/logging purposes only).
        Args:
        token (str): JWT token string
        Returns:
        dict: Decoded payload
    """
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        return decoded
    except Exception:
        raise JWTError("Cannot decode token")
