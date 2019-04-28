"""empty message

Revision ID: 10f26afdf4d0
Revises: 64efacbe912f
Create Date: 2019-04-27 20:23:11.007284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10f26afdf4d0'
down_revision = '64efacbe912f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('_user_follower_uc', 'Follows', ['user_id', 'follower_id'])
    op.create_unique_constraint('_user_post_uc', 'Likes', ['user_id', 'post_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('_user_post_uc', 'Likes', type_='unique')
    op.drop_constraint('_user_follower_uc', 'Follows', type_='unique')
    # ### end Alembic commands ###