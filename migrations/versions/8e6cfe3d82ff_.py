"""empty message

Revision ID: 8e6cfe3d82ff
Revises: 
Create Date: 2022-10-05 21:41:42.672074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e6cfe3d82ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stack',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('stack_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['stack_id'], ['stack.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operand')
    op.drop_table('stack')
    # ### end Alembic commands ###