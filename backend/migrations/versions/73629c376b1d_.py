"""empty message

Revision ID: 73629c376b1d
Revises: ba68c97a0956
Create Date: 2018-08-08 16:23:21.172982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73629c376b1d'
down_revision = 'ba68c97a0956'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('abstract', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'abstract')
    # ### end Alembic commands ###
