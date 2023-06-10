#!/usr/bin/env python3
"""
Auth module
"""
from db import DB
from uuid import uuid4
from user import User
from bcrypt import hashpw, gensalt, checkpw
from typing import TypeVar
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """hash a password pass for user

    Args:
        password (str): password of user

    Returns:
        str: password hashed
    """
    return hashpw(password.encode('utf-8'), gensalt())
