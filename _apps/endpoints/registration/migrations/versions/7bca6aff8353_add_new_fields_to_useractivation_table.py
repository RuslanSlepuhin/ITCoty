"""Add new fields to UserActivation table

Revision ID: 7bca6aff8353
Revises: 6bdf8e7f62ba
Create Date: 2023-09-08 11:03:11.714891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bca6aff8353'
down_revision = '6bdf8e7f62ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_activation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activated', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_activation', schema=None) as batch_op:
        batch_op.drop_column('created_at')
        batch_op.drop_column('activated')

    # ### end Alembic commands ###
