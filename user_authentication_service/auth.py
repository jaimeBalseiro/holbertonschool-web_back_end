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


def _generate_uuid() -> str:
    """generate uuid

    Returns:
        str: representation of a new UUID
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register a user

        Args:
            email (str): email of user
            password (str): password of user

        Returns:
            User: user registered
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """valid login of user

        Args:
            email (str): email of user
            password (str): password of user

        Returns:
            bool: [description]
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """
        Create new session and return the session ID
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return

    def get_user_from_session_id(self, session_id: str) -> str:
        """get user from session id

        Args:
            session_id (str): session id of user

        Returns:
            str: user email
        """
        if session_id is None:
            return
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user.email
        except NoResultFound:
            return

    def destroy_session(self, user_id: int) -> None:
        """destroy session

        Args:
            user_id (int): user id
        """
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            pass
