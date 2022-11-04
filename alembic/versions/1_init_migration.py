"""empty message

Revision ID: 8e8779e25503
Revises: 
Create Date: 2022-11-01 19:50:55.595656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e8779e25503'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('user',
                    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
                    sa.Column('username', sa.String(length=256), nullable=False),
                    sa.Column('email', sa.String(length=256), nullable=False),
                    sa.Column('hashed_password', sa.String(length=256), nullable=False),
                    sa.Column('is_active', sa.Boolean, nullable=False))
    # op.create_table('post', sa.Column('title', sa.String(length=256), nullable=False),
    #                 sa.Column('content', sa.String(length=256), nullable=False),
    #                 sa.Column('published', sa.Boolean, nullable=False, server_default='1'),
    #                 sa.Column('created_at', sa.TIMESTAMP, nullable=False))


def downgrade() -> None:
    op.drop_table('user')
