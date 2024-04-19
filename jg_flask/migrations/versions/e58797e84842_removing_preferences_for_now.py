"""Removing preferences for now

Revision ID: e58797e84842
Revises: 4f2fbd17b1a6
Create Date: 2024-04-12 18:35:16.520987

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e58797e84842'
down_revision = '4f2fbd17b1a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('fav_activities')
        batch_op.drop_column('fav_accomodations')
        batch_op.drop_column('fav_shopping')
        batch_op.drop_column('fav_foods')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fav_foods', mysql.VARCHAR(length=1000), nullable=True))
        batch_op.add_column(sa.Column('fav_shopping', mysql.VARCHAR(length=1000), nullable=True))
        batch_op.add_column(sa.Column('fav_accomodations', mysql.VARCHAR(length=1000), nullable=True))
        batch_op.add_column(sa.Column('fav_activities', mysql.VARCHAR(length=1000), nullable=True))

    # ### end Alembic commands ###