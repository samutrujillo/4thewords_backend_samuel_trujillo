from sqlmodel import SQLModel, create_engine, Session
from app.models.legend_model import Legend
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session