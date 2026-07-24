"""crear_tabla_productos

Revision ID: 79548fc57c23
Revises: 
Create Date: 2026-07-21 12:30:32.780229

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79548fc57c23'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'productos',
        sa.Column("producto_id",sa.Integer, primary_key=True, nullable=False),
        sa.Column("nombre",sa.String(length=50), nullable=False),
        sa.Column("costo",sa.Float(),nullable=False),
        sa.Column("Precio_Venta",sa.Float(),nullable=False),
        sa.Column("Stock",sa.Integer(),nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('productos')
