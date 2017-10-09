from concierge.models import (
    Customer,
    Picks,
    Stylist
)
from concierge.utils.db import Session


class CustomerManager:
    """
    A class for interacting with the customer model.
    """
    @classmethod
    def get_customer_by_whatever(cls, *args, **kwargs):
        """
        Just returns the first the customer in the db
        """
        return Session().query(Customer).first()


class StylistManager:
    """
    A class for interacting with the stylist model.
    """
    @classmethod
    def get_stylist_by_whatever(cls, *args, **kwargs):
        """
        Just returns the first the stylist in the db
        """
        return Session().query(Stylist).first()


class PicksManager:
    """
    A class for managing picks.
    """
    @classmethod
    def create_picks(cls, stylist_id, customer_id, *product_ids):
        session = Session()
        try:
            stylist = session.query(Stylist).filter_by(id=stylist_id).one()
            customer = session.query(Customer).filter_by(id=customer_id).one()
            session.add_all([
                Picks(stylist=stylist, customer=customer, ruecom_id=p_id)
                for p_id in product_ids
            ])
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()
