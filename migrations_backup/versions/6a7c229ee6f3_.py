"""empty message

Revision ID: 6a7c229ee6f3
Revises: dbfc1458e01f
Create Date: 2020-02-07 01:41:29.999142

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6a7c229ee6f3'
down_revision = 'dbfc1458e01f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genre_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Venue', 'Genre', ['genre_id'], ['id'])
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'Venue', type_='foreignkey')
    op.drop_column('Venue', 'genre_id')
    # ### end Alembic commands ###
