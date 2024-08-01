# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['type_map', 'Database', 'create_column']

# %% ../nbs/00_core.ipynb 4
from sqlalchemy import *
from fastcore.utils import *

__all__ = []

# %% ../nbs/00_core.ipynb 6
class Database:
    def __init__(self, conn_str):
        self.engine = create_engine(conn_str)
        self.metadata = MetaData()
        self.metadata.create_all(self.engine)

# %% ../nbs/00_core.ipynb 7
type_map = {
    int: Integer,
    str: String,
    float: Float,
    bool: Boolean
}
def create_column(name, typ, primary=False):
    return Column(name, type_map[typ], primary_key=primary)

# %% ../nbs/00_core.ipynb 8
@patch
def create_table(self: Database, tname, pk: str|None=None, **cols):
    pkcol = None
    # Set primary key, popping from cols
    if pk is not None: pkcol = create_column(pk, cols.pop(pk), primary=True)
    columns = [create_column(name, typ) for name, typ in cols.items()]
    # Insert primary key at the beginning
    if pkcol is not None: columns.insert(0, pkcol)
    return Table(tname, self.metadata, *columns)
