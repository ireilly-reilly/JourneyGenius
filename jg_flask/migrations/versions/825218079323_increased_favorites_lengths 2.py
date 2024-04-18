"""Increased favorites lengths

Revision ID: 825218079323
Revises: 7a199159634a
Create Date: 2024-04-10 15:12:32.807065

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '825218079323'
down_revision = '7a199159634a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('fav_activities',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=300),
               existing_nullable=True)
        batch_op.alter_column('fav_foods',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=300),
               existing_nullable=True)
        batch_op.alter_column('fav_shopping',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=300),
               existing_nullable=True)
        batch_op.alter_column('fav_accomodations',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=300),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('fav_accomodations',
               existing_type=sa.String(length=300),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('fav_shopping',
               existing_type=sa.String(length=300),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('fav_foods',
               existing_type=sa.String(length=300),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('fav_activities',
               existing_type=sa.String(length=300),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###