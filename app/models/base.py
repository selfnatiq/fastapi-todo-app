from sqlalchemy import TIMESTAMP, Column, func, text
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    __name__: str

    id = Column(postgresql.UUID, server_default=text(
        "gen_random_uuid()"), primary_key=True, index=True)
    updated_at = Column(TIMESTAMP(timezone=True), default=func.now(),
                        onupdate=func.now())
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
