"""rename address

Revision ID: b3ca843f8c1b
Revises: e333193b5b03
Create Date: 2024-10-01 22:46:52.968282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3ca843f8c1b'
down_revision = 'e333193b5b03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # op.add_column('departments', sa.Column('location', sa.String(), nullable=True))
    # op.drop_column('departments', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
    # op.drop_column('departments', 'location')
    # ### end Alembic commands ###
