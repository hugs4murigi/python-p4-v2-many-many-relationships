"""add employee_meetings association table

Revision ID: dd5e8a124ab6
Revises: 03ce1f505764
Create Date: 2024-04-10 21:54:41.871889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd5e8a124ab6'
down_revision = '03ce1f505764'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee_meetings',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('metting_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_employee_meetings_employee_id_employees')),
    sa.ForeignKeyConstraint(['metting_id'], ['meetings.id'], name=op.f('fk_employee_meetings_metting_id_meetings')),
    sa.PrimaryKeyConstraint('employee_id', 'metting_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee_meetings')
    # ### end Alembic commands ###