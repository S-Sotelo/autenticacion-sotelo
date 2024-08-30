"""empty message

Revision ID: 2c20beac00d0
Revises: 61145ab5f3f5
Create Date: 2024-07-17 11:52:32.574701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c20beac00d0'
down_revision = '61145ab5f3f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('post_categories',
    sa.Column('categories_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categories_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('categories_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_categories')
    op.drop_table('categories')
    # ### end Alembic commands ###
