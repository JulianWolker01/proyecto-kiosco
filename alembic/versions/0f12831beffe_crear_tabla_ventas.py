"""crear_tabla_ventas

Revision ID: 0f12831beffe
Revises: 79548fc57c23
Create Date: 2026-07-21 20:59:33.660518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f12831beffe'
down_revision: Union[str, Sequence[str], None] = '79548fc57c23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'ventas',
        sa.Column("venta_id",sa.Integer, primary_key=True, nullable=False),
        sa.Column("fecha",sa.DateTime(), nullable=False),
        sa.Column("metodo_pago", sa.String(length=50), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('ventas')
