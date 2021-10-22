from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from workshop.settings import settings

engine = create_engine(
    url=settings.database_url,
    connect_args={'check_same_thread': False}
)

Session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
