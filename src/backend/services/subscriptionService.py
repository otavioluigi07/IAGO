from sqlalchemy.exc import SQLAlchemyError
from models.subscriptionModel import Subscription

class SubscriptionService:
    @staticmethod
    def create_subscription(name, price, model, active):
        from database.database import db  # Importação localizada
        try:
            new_subscription = Subscription.insert().values(
                name=name,
                price=price,
                model=model,
                active=active
            )
            db.session.execute(new_subscription)
            db.session.commit()
            return {"message": "Subscription created successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def get_subscription(subscription_id):
        from database.database import db  # Importação localizada
        try:
            result = db.session.execute(Subscription.select().where(Subscription.c.id == subscription_id)).fetchone()
            if result:
                return dict(result)
            else:
                return {"error": "Subscription not found"}
        except SQLAlchemyError as e:
            return {"error": str(e)}
            
    @staticmethod
    def get_all_subscription():
        from database.database import db  # Importação localizada
        try:
            subs = Subscription.query.all()
            return [sub.to_dict() for sub in subs]
        except SQLAlchemyError as e:
            return {"error": str(e)}

    @staticmethod
    def update_subscription(subscription_id, **kwargs):
        from database.database import db  # Importação localizada
        try:
            update_values = {key: value for key, value in kwargs.items() if value is not None}
            if update_values:
                db.session.execute(Subscription.update().where(Subscription.c.id == subscription_id).values(**update_values))
                db.session.commit()
                return {"message": "Subscription updated successfully"}
            else:
                return {"error": "No values provided for update"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def delete_subscription(subscription_id):
        from database.database import db  # Importação localizada
        try:
            db.session.execute(Subscription.delete().where(Subscription.c.id == subscription_id))
            db.session.commit()
            return {"message": "Subscription deleted successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}
