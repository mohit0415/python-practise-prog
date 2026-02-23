from database_config import session

def help_db():
    db = session()
    try:
        yield db
    finally:
        db.close()