from abc import ABC, abstractmethod
from sqlalchemy.orm.attributes import InstrumentedAttribute

class TableColumn(ABC):
    field_in_table: InstrumentedAttribute

    @abstractmethod
    def read_value(cls, value_to_filter):
        pass
