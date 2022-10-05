"""empty message

Revision ID: 178ff8111787
Revises: 8e6cfe3d82ff
Create Date: 2022-10-05 22:20:32.715243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '178ff8111787'
down_revision = '8e6cfe3d82ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    operator_table = op.create_table(
        'operator',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.bulk_insert(
        operator_table,
        [
            {"id": 1, "name": "Addition"},
            {"id": 2, "name": "Subtraction"},
            {"id": 3, "name": "Multiplication"},
            {"id": 4, "name": "Division"},
        ]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operator')
    # ### end Alembic commands ###