import sqlalchemy as sa
from sqlalchemy import TIMESTAMP, text

from app.database import Base


class Post(Base):
    __tablename__ = 'post'
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    title = sa.Column(sa.String(length=256), nullable=False)
    content = sa.Column(sa.String(length=256), nullable=False)
    published = sa.Column(sa.Boolean(), nullable=False, default=True)
    created_at = sa.Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
