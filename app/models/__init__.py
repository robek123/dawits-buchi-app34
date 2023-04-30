from app.models.users import User, UserCreate, UserUpdate


def get_model(name: str):
    return models.get(name)
