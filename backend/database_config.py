from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = 'mysql+pymysql://root:empover#1@localhost:3306/practdata'
db_engine = create_engine(db_url)
session = sessionmaker(autoflush=False,bind=db_engine)


# db_url = 'mysql+pymysql://root:empover#1@localhost:3306/practdata'
# db_engine = create_engine(db_url)
# sessionmaker(autoflush=False,bind=db_engine)

