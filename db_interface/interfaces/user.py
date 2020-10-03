from db_interface.models import User


def get_or_create(user_id: int) -> User:
    return User.get_or_create(id=user_id)
