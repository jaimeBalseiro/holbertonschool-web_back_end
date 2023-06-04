#!/usr/bin/env python3
"""
    encryption password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """expects one string argument name password and returns
       a salted, hashed password, which is a byte string.

    Args:
        password (str): password

    Returns:
        bytes: encryption password
    """
    if password:
        return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
