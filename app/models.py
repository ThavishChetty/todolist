from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class List(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    listname: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)

    items: so.WriteOnlyMapped['Item'] = so.relationship(
        back_populates='todolist') 

    def __repr__(self):
        return '<User {}>'.format(self.listname)


class Item(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    itemname: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    list_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(List.id),
                                               index=True)

    todolist: so.Mapped[List] = so.relationship(back_populates='items')

    def __repr__(self):
        return '<Post {}>'.format(self.itemname)