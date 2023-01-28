from ..db.connection import SessionLocal


# Get DB Connection Session
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


