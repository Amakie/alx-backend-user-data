#!/usr/bin/python3 env
"""auth class"""

from flask import request
from typing import List, TypeVar


class Auth:
    """auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """header function"""
        if request is None:
            return None

    def current_user(self, request=None):
        """current user function"""
        if request is None:
            return None
