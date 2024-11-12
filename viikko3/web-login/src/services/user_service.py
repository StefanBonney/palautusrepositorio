import re

from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user
    
    def is_username_taken(self, username):
        return self._user_repository.find_by_username(username) is not None

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        # Käyttäjätunnuksen on oltava merkeistä a-z koostuva vähintään 3 merkin pituinen merkkijono
        if len(username) < 3 or not username.islower() or not username.isalpha():
            raise UserInputError("Username must be at least 3 characters and contain only a-z")

        # joka ei ole vielä käytössä
        if self.is_username_taken(username):
            raise UserInputError("Username is already in use")

        # Salasanan on oltava pituudeltaan vähintään 8 merkkiä ja se ei saa koostua pelkästään kirjaimista
        if len(password) < 8 or password.isalpha():
            raise UserInputError("Password must be at least 8 characters and contain more than just letters")

        # Password and confirmation must match
        if password != password_confirmation:
            raise UserInputError("Password and confirmation do not match")

user_service = UserService()
