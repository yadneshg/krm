"""empty message

Revision ID: 05bbfcb37313
Revises: f79d5c827c9b
Create Date: 2020-08-27 12:50:02.848739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05bbfcb37313'
down_revision = 'f79d5c827c9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('salary_master',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('emp_id', sa.Integer(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=False),
    sa.Column('effective_date', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('salary_master')
    op.drop_table('account_category')
    # ### end Alembic commands ###