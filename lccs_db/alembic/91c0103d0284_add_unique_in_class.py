"""add_unique_in_class

Revision ID: 91c0103d0284
Revises: 237031a776fb
Create Date: 2021-03-04 08:38:55.907674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91c0103d0284'
down_revision = '237031a776fb'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('classes_name_key'), 'classes', ['name', 'class_system_id'], schema='lccs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('classes_name_key'), 'classes', schema='lccs', type_='unique')
    # ### end Alembic commands ###