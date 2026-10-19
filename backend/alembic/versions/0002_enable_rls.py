"""enable row level security (Supabase)

Supabase exposes every table in `public` through its REST API using the public
anon key. Enabling RLS with no policies blocks that path entirely, while the
backend (which connects as the `postgres` role and bypasses RLS) keeps working.

Revision ID: 0002_enable_rls
Revises: 0001_baseline
"""
from typing import Sequence, Union

from alembic import op

revision: str = "0002_enable_rls"
down_revision: Union[str, Sequence[str], None] = "0001_baseline"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

TABLES = ["users", "body_analysis", "transformation_plan", "timeline", "dietary_plan"]


def upgrade() -> None:
    if op.get_bind().dialect.name != "postgresql":
        return
    for t in TABLES:
        op.execute(f'ALTER TABLE public."{t}" ENABLE ROW LEVEL SECURITY')


def downgrade() -> None:
    if op.get_bind().dialect.name != "postgresql":
        return
    for t in TABLES:
        op.execute(f'ALTER TABLE public."{t}" DISABLE ROW LEVEL SECURITY')
