"""empty message

Revision ID: 9b76f6ba8d3d
Revises: 43bd92fba073
Create Date: 2018-06-24 17:09:15.872827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b76f6ba8d3d'
down_revision = '43bd92fba073'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('price', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'price')
    # ### end Alembic commands ###
