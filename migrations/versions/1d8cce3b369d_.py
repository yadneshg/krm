"""empty message

Revision ID: 1d8cce3b369d
Revises: ecf0fcbfb21d
Create Date: 2020-08-12 22:56:29.211015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d8cce3b369d'
down_revision = 'ecf0fcbfb21d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee_master', sa.Column('is_working', sa.Boolean(), nullable=True))
    op.add_column('unit_master', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('unit_master', 'is_active')
    op.drop_column('employee_master', 'is_working')
    # ### end Alembic commands ###
