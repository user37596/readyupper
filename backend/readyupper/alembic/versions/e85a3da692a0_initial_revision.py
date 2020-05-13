"""Initial revision

Revision ID: e85a3da692a0
Revises: 
Create Date: 2020-05-13 16:35:21.962568

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e85a3da692a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calendars',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('entries',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('calendar_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['calendar_id'], ['calendars.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('participants',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('calendar_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['calendar_id'], ['calendars.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participants')
    op.drop_table('entries')
    op.drop_table('calendars')
    # ### end Alembic commands ###
