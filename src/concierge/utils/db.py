from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_connection(user='concierge_app', password='password', host='db', db='concierge'):
    """
    get a connection to the database
    """
    connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(
        user,
        password,
        host,
        5432,
        db
    )

    connection = create_engine(connection_string)
    metadata = MetaData(bind=connection)

    return connection, metadata


Base = declarative_base()
connection, metadata = get_connection()
Session = sessionmaker(bind=connection)
