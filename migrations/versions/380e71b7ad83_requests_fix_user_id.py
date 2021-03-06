"""requests fix user_id

Revision ID: 380e71b7ad83
Revises: 3fe29dad938a
Create Date: 2022-06-15 14:26:03.656637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '380e71b7ad83'
down_revision = '3fe29dad938a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('requests_user_id_fkey', 'requests', type_='foreignkey')
    op.create_foreign_key(None, 'requests', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'requests', type_='foreignkey')
    op.create_foreign_key('requests_user_id_fkey', 'requests', 'requests', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
