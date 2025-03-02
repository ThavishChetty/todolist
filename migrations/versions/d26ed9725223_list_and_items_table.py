"""list and items table

Revision ID: d26ed9725223
Revises: 
Create Date: 2025-03-02 21:07:41.167707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd26ed9725223'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('listname', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('list', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_list_listname'), ['listname'], unique=True)

    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('itemname', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=140), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('list_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_item_itemname'), ['itemname'], unique=True)
        batch_op.create_index(batch_op.f('ix_item_list_id'), ['list_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_item_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_item_timestamp'))
        batch_op.drop_index(batch_op.f('ix_item_list_id'))
        batch_op.drop_index(batch_op.f('ix_item_itemname'))

    op.drop_table('item')
    with op.batch_alter_table('list', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_list_listname'))

    op.drop_table('list')
    # ### end Alembic commands ###
