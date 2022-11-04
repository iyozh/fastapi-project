import sqlalchemy as sa

from database.base_class import Base


class User(Base):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    username = sa.Column(sa.String, unique=True, index=True)
    email = sa.Column(sa.String, unique=True, index=True)
    hashed_password = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean, default=True)
