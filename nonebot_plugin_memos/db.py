from sqlalchemy import ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime


from nonebot_plugin_orm import Model


class Memo(Model):
    __tablename__: str = "nonebot_plugin_memos_memo"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[str] = mapped_column(nullable=False)
    user_info: Mapped[str] = mapped_column(nullable=False)
    session_persist_id: Mapped[int] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    token: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class Setting(Model):
    __tablename__: str = "nonebot_plugin_memos_setting"

    user_id: Mapped[str] = mapped_column(primary_key=True)
    default_memo: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey(f"{str(Memo.__tablename__)}.{Memo.id.key}", ondelete="SET NULL"),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )