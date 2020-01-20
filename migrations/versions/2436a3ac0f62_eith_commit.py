"""eith commit

Revision ID: 2436a3ac0f62
Revises: 68eac5fb23db
Create Date: 2019-09-23 19:39:35.398088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2436a3ac0f62'
down_revision = '68eac5fb23db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscribe')
    # ### end Alembic commands ###
