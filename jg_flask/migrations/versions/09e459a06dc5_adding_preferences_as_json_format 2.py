"""Adding preferences as JSON format

Revision ID: 09e459a06dc5
Revises: e58797e84842
Create Date: 2024-04-12 18:35:48.442819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09e459a06dc5'
down_revision = 'e58797e84842'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fav_activities', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('fav_foods', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('fav_shopping', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('fav_accomodations', sa.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('fav_accomodations')
        batch_op.drop_column('fav_shopping')
        batch_op.drop_column('fav_foods')
        batch_op.drop_column('fav_activities')

    # ### end Alembic commands ###