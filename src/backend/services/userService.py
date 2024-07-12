from sqlalchemy.exc import SQLAlchemyError
from models.userModel import User
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash


class UserService:
    @staticmethod
    def create_user(name, email, password, occupation, cell, age, gender, subscription_id, role):
        from database.database import db  # Importação localizada
        try:
            hashed_password = generate_password_hash(password)

            new_user = User(
                name=name,
                email=email,
                password=hashed_password,
                occupation=occupation,
                cell=cell,
                age=age,
                gender=gender,
                subscription_id=subscription_id,
                role=role
            )
            db.session.add(new_user)
            db.session.commit()
            return {"message": "User created successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def get_all_user():
        from database.database import db  # Importação localizada
        try:
            users = User.query.all()
            return [user.to_dict() for user in users]
        except SQLAlchemyError as e:
            return {"error": str(e)}

    @staticmethod
    def get_user(user_id):
        from database.database import db  # Importação localizada
        try:
            user = User.query.get(user_id)
            if user:
                return user.to_dict()
            else:
                return {"error": "User not found"}
        except SQLAlchemyError as e:
            return {"error": str(e)}

    @staticmethod
    def update_user(user_id, name, email, password, occupation, cell, age, gender, subscription_id, role):
        from database.database import db  # Importação localizada
        try:
            user = User.query.get(user_id)
            if user:
                user.name = name
                user.email = email
                user.password = password
                user.occupation = occupation
                user.cell = cell
                user.age = age
                user.gender = gender
                user.subscription_id = subscription_id
                user.role = role
                db.session.commit()
                return {"message": "User updated successfully"}
            else:
                return {"error": "User not found"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def delete_user(user_id):
        from database.database import db  # Importação localizada
        try:
            user = User.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return {"message": "User deleted successfully"}
            else:
                return {"error": "User not found"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}
        
    @staticmethod
    def login(email, password):
        from database.database import db
        try:
            # Busca o usuário pelo email
            user = db.session.query(User).filter_by(email=email).first()

            if user:
                # Verifica a senha
                if check_password_hash(user.password, password):
                    authenticated = True
                    return {"message": "Login successful"}, authenticated, user.id, user.name, user.email, user.occupation, user.cell, user.age,user.gender, user.subscription_id, user.role, user.password
                
                else:
                    authenticated = False
                    return {"error": "Invalid password"}, authenticated
            else:
                authenticated = False
                return {"error": "User not found"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}