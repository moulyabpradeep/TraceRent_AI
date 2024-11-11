from sqlalchemy.orm import Session
from app.models.user import User

from sqlalchemy.orm import Session
# Save a user to the database and return the user ID
def save_user_to_db(db: Session, user_data: User) -> int:
    
    new_user = User(
        username=user_data['user_email'],
        password=user_data['user_password'],
        name=user_data['name_of_user'],
        email=user_data['user_email'],
        phone=user_data['user_phone']
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.user_id


# Retrieve a user from the database by email
def get_user_from_db(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()