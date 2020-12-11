from database.models import User, Platform


def get_or_create(user_id: int, platform: str) -> User:
    platform = Platform.get(name=platform)
    return User.get_or_create(user_id=user_id, platform=platform)
