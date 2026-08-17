"""
Minimal SQLAlchemy model + session setup for storing post summaries.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

from src.config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)


class PostSummary(Base):
    __tablename__ = "post_summaries"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    post_count = Column(Integer, nullable=False)


def init_db():
    Base.metadata.create_all(engine)


def save_summary(summary_df):
    init_db()
    session = SessionLocal()
    try:
        for _, row in summary_df.iterrows():
            session.add(PostSummary(user_id=int(row["userId"]), post_count=int(row["post_count"])))
        session.commit()
    finally:
        session.close()
