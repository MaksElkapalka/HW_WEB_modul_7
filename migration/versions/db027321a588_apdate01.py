"""apdate01

Revision ID: db027321a588
Revises: d8b7fa9398fc
Create Date: 2024-04-14 19:25:09.896776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db027321a588'
down_revision: Union[str, None] = 'd8b7fa9398fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.Column('date_of', sa.Date(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('grages')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grages',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('grade', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date_of', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('subject_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], name='grages_student_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], name='grages_subject_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='grages_pkey')
    )
    op.drop_table('grades')
    # ### end Alembic commands ###
