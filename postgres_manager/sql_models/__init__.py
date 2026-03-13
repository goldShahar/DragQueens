import datetime

from geoalchemy2 import Geometry, WKBElement
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy import ARRAY, String, create_engine
from sqlalchemy import MetaData, DateTime
postgres_con_url = "postgresql://{}:{}@{}/{}"


def get_db_engine():
    return create_engine(postgres_con_url.format('postgres', 'postgres', '51.4.105.247:5432', "deployments"))


engine = get_db_engine()
metadata = MetaData()



class Base(DeclarativeBase):
    pass

class Type(Base):
    __tablename__ = "Types"
    type_name: Mapped[str] = mapped_column(primary_key=True)
    importance: Mapped[int] = mapped_column()
    Min_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    Min_area: Mapped[float] = mapped_column()


class Hazard(Base):
    __tablename__ = "Hazards"
    type_name: Mapped[str] = mapped_column()
    id: Mapped[str] = mapped_column(primary_key=True)
    geo_polygon: Mapped[WKBElement] = mapped_column(Geometry(geometry_type="POLYGON", srid=4326))
    start_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    people_ids: Mapped[list[str]] = mapped_column(ARRAY(String))
    buildings_ids: Mapped[list[str]] = mapped_column(ARRAY(String))



Base.metadata.create_all(engine)