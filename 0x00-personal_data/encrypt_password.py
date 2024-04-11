#!/usr/bin/env python3
"""implement a hash_password function"""

import bcrypt


def hash_password(password: str) -> bytes:
    """returns salted and hashed password"""
    encoded = password.encode()
    hashpwd = bcrypt.hashpwd(encoded, bcrypt.gensalt())

    return hashpwd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate that the provided password matches the hashed password"""
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
