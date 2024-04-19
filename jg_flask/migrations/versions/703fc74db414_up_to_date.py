"""Up to date

Revision ID: 703fc74db414
Revises: c7091f5ce772
Create Date: 2024-04-18 17:16:20.498965

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '703fc74db414'
down_revision = 'c7091f5ce772'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('super_user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=60),
               type_=sa.String(length=300),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fav_activities', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('fav_foods', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('fav_shopping', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('fav_accomodations', sa.JSON(), nullable=True))
        batch_op.drop_column('interests')
        batch_op.drop_column('gender')
        batch_op.drop_column('age')
        batch_op.drop_column('accommodations')
        batch_op.drop_column('transportation')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('transportation', mysql.VARCHAR(length=5), nullable=True))
        batch_op.add_column(sa.Column('accommodations', mysql.VARCHAR(length=5), nullable=True))
        batch_op.add_column(sa.Column('age', mysql.VARCHAR(length=5), nullable=True))
        batch_op.add_column(sa.Column('gender', mysql.VARCHAR(length=5), nullable=True))
        batch_op.add_column(sa.Column('interests', mysql.VARCHAR(length=10), nullable=True))
        batch_op.drop_column('fav_accomodations')
        batch_op.drop_column('fav_shopping')
        batch_op.drop_column('fav_foods')
        batch_op.drop_column('fav_activities')

    with op.batch_alter_table('super_user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=300),
               type_=mysql.VARCHAR(length=60),
               existing_nullable=False)

    # ### end Alembic commands ###