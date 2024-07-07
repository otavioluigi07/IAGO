from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from models.historicModel import historic
from . import db

class HistoricService:
    @staticmethod
    def create_historic(user_id, subscription_id, total_price, payment_method, status):
        try:
            new_purchase = historic.insert().values(
                user_id=user_id,
                purchase_date=datetime.utcnow(),
                subscription_id=subscription_id,
                total_price=total_price,
                payment_method=payment_method,
                status=status
            )
            db.session.execute(new_purchase)
            db.session.commit()
            return {"message": "Purchase history created successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def get_historic(historic_id):
        try:
            result = db.session.execute(historic.select().where(historic.c.id == historic_id)).fetchone()
            if result:
                return dict(result)
            else:
                return {"error": "Purchase history not found"}
        except SQLAlchemyError as e:
            return {"error": str(e)}

    @staticmethod
    def update_historic(historic_id, **kwargs):
        try:
            update_values = {key: value for key, value in kwargs.items() if value is not None}
            if update_values:
                db.session.execute(historic.update().where(historic.c.id == historic_id).values(**update_values))
                db.session.commit()
                return {"message": "Purchase history updated successfully"}
            else:
                return {"error": "No values provided for update"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def delete_historic(historic_id):
        try:
            db.session.execute(historic.delete().where(historic.c.id == historic_id))
            db.session.commit()
            return {"message": "Purchase history deleted successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}
