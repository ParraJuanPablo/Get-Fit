"""empty message

Revision ID: 9d4c8adad175
Revises: 4767fa2a8f6e
Create Date: 2023-05-18 15:39:00.496621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d4c8adad175'
down_revision = '4767fa2a8f6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('valores_diario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('calorias_ingeridas', sa.Integer(), nullable=False),
    sa.Column('calorias_gastadas', sa.Integer(), nullable=False),
    sa.Column('horas_ejercicio', sa.Integer(), nullable=False),
    sa.Column('horas_sueño', sa.Integer(), nullable=False),
    sa.Column('scoop_proteina', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('valores_mensual',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ptos_mes', sa.String(), nullable=False),
    sa.Column('hsue_mes', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('valores')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('valores',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('calorias_ingeridas', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('calorias_gastadas', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('horas_ejercicio', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('horas_sueño', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('scoop_proteina', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='valores_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='valores_pkey')
    )
    op.drop_table('valores_mensual')
    op.drop_table('valores_diario')
    # ### end Alembic commands ###