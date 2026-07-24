"""crear_tabla_detalles_venta

Revision ID: 388a4168299f
Revises: 0f12831beffe
Create Date: 2026-07-24 15:40:52.178670

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '388a4168299f'
down_revision: Union[str, Sequence[str], None] = '0f12831beffe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'detalle_venta',
        sa.Column("detalle_id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("venta_id", sa.Integer(), sa.ForeignKey("ventas.id"), nullable=False),
        sa.Column("producto_id", sa.Integer(), sa.ForeignKey("productos.id"), nullable=False),
        sa.Column("cantidad", sa.Integer(), nullable=False),
        sa.Column("precio_unitario", sa.Float(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('detalle_venta')
    pass
