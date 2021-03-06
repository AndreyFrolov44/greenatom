"""3

Revision ID: 9f9d0b6ece8b
Revises: e05bdd1fc7bb
Create Date: 2022-06-14 19:22:19.927479

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9f9d0b6ece8b'
down_revision = 'e05bdd1fc7bb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_inboxes_id', table_name='inboxes')
    op.drop_index('ix_inboxes_request_code', table_name='inboxes')
    op.drop_table('inboxes')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inboxes',
    sa.Column('request_code', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('file_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('datetime', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['request_code'], ['requests.id'], name='inboxes_request_code_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('request_code', name='inboxes_pkey'),
    sa.UniqueConstraint('file_name', name='inboxes_file_name_key')
    )
    op.create_index('ix_inboxes_request_code', 'inboxes', ['request_code'], unique=False)
    op.create_index('ix_inboxes_id', 'inboxes', ['id'], unique=False)
    # ### end Alembic commands ###
