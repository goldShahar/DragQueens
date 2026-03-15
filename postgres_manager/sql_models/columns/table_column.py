from abc import ABC, abstractmethod
from sqlalchemy.orm.attributes import InstrumentedAttribute

class TableColumn(ABC):

    @abstractmethod
    def read_value(cls, value_to_filter):
        pass
