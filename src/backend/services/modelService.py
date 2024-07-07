from sqlalchemy.exc import SQLAlchemyError
from models.modelModel import model
from . import db

class ModelService:
    @staticmethod
    def create_model(name, max_token, min_token):
        try:
            new_model = model.insert().values(
                name=name,
                max_token=max_token,
                min_token=min_token
            )
            db.session.execute(new_model)
            db.session.commit()
            return {"message": "Model created successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def get_model(model_id):
        try:
            result = db.session.execute(model.select().where(model.c.id == model_id)).fetchone()
            if result:
                return dict(result)
            else:
                return {"error": "Model not found"}
        except SQLAlchemyError as e:
            return {"error": str(e)}

    @staticmethod
    def update_model(model_id, **kwargs):
        try:
            update_values = {key: value for key, value in kwargs.items() if value is not None}
            if update_values:
                db.session.execute(model.update().where(model.c.id == model_id).values(**update_values))
                db.session.commit()
                return {"message": "Model updated successfully"}
            else:
                return {"error": "No values provided for update"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def delete_model(model_id):
        try:
            db.session.execute(model.delete().where(model.c.id == model_id))
            db.session.commit()
            return {"message": "Model deleted successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}
