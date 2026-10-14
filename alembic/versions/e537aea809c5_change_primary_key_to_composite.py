"""change_primary_key_to_composite

Revision ID: e537aea809c5
Revises: 
Create Date: 2026-10-13 11:00:52.953755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e537aea809c5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Обязательно используем batch_alter_table для SQLite
    # recreate='always' заставит Alembic пересоздать таблицу с новым ключом
    with op.batch_alter_table('messages', recreate='always') as batch_op:
        # 1. Сначала удаляем старый одиночный первичный ключ (если он был)
        # Если старого ключа не было, эту строку можно опустить
        # batch_op.drop_constraint(None, type_='primary')

        # 2. Явно меняем тип колонок на BigInteger.
        # В SQLite это подстраховка, но для Alembic это критично, чтобы зафиксировать изменения структуры.
        batch_op.alter_column('id', type_=sa.BigInteger(), primary_key=False)
        batch_op.alter_column('channel_id', type_=sa.BigInteger(), primary_key=False)

        # 3. Назначаем новый составной первичный ключ
        batch_op.create_primary_key('pk_messages', columns=['id', 'channel_id'])


def downgrade() -> None:
    with op.batch_alter_table('messages', recreate='always') as batch_op:
        # batch_op.drop_constraint(None, type_='primary')

        # Возвращаем типы обратно (например, к обычному Integer), если это необходимо
        batch_op.alter_column('id', type_=sa.Integer(), primary_key=False)
        batch_op.alter_column('channel_id', type_=sa.Integer(), primary_key=False)

        # Возвращаем старый одиночный ключ
        batch_op.create_primary_key('pk_messages', columns=['id'])
