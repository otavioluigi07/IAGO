from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from models.userModel import user
from . import db

class UserService:
    @staticmethod
    def create_user(name, email, occupation, cell, age, gender, subscription_id, role):
        try:
            new_user = user.insert().values(
                name=name,
                email=email,
                occupation=occupation,
                cell=cell,
                age=age,
                gender=gender,
                subscription_id= 0,
                role=role
            )
            db.session.execute(new_user)
            db.session.commit()
            return {"message": "User created successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def get_all_users():
        try:
            result = db.session.execute(user.select()).fetchall()
            users = [dict(row) for row in result]
            return users
        except SQLAlchemyError as e:
            return {"error": str(e)}
        
    @staticmethod
    def get_user(user_id):
        try:
            result = db.session.execute(user.select().where(user.c.id == user_id)).fetchone()
            if result:
                return dict(result)
            else:
                return {"error": "User not found"}
        except SQLAlchemyError as e:
            return {"error": str(e)}

    @staticmethod
    def update_user(user_id, **kwargs):
        try:
            update_values = {key: value for key, value in kwargs.items() if value is not None}
            if update_values:
                db.session.execute(user.update().where(user.c.id == user_id).values(**update_values))
                db.session.commit()
                return {"message": "User updated successfully"}
            else:
                return {"error": "No values provided for update"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def delete_user(user_id):
        try:
            db.session.execute(user.delete().where(user.c.id == user_id))
            db.session.commit()
            return {"message": "User deleted successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}
