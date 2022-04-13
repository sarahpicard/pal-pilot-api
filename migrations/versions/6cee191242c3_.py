"""empty message

Revision ID: 6cee191242c3
Revises: b7541f615b42
Create Date: 2022-04-09 15:45:18.449610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cee191242c3'
down_revision = 'b7541f615b42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('allergies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('allergy', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('pet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pet_id'], ['pets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('allergies')
    # ### end Alembic commands ###
