"""empty message

Revision ID: 0898ac9abb57
Revises: 636a9031d3e5
Create Date: 2021-03-17 13:15:59.330313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0898ac9abb57'
down_revision = '636a9031d3e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('venue', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'upcoming_shows_count')
    op.drop_column('venue', 'past_shows_count')
    # ### end Alembic commands ###