# Pyreusion
# Version 1.0

#%%
from pandas import DataFrame
import re
from typing import Optional
from pymysql.converters import escape_string
import logging


#%%
class DFTools:
    """Pandas DataFrame common tools
    """

    @classmethod
    def cols_lower(cls, df: DataFrame, inplace: bool = False):
        """Make DataFrame columns name lower & replace special characters
        """
        _df = df.copy()
        new_cols = [re.sub('[^\w]', '_', col.strip()).lower() for col in df.columns]
        _df.columns = new_cols
        if inplace:
            df.columns = new_cols
            return df.head()
        else:
            return _df.head()

    @classmethod
    def drop_unnamed_cols(cls, df: DataFrame, inplace: bool = False):
        """Drop Unnamed__XX cols for DF read from read_excel().
        """
        drop_cols = [col for col in df.columns.tolist() if 'unnamed__' in col.lower()]
        df.drop(columns=drop_cols, inplace=inplace)
        return df.head()
    
    @classmethod
    def get_duplicate_update_sql(cls, df: DataFrame, schema: str, table: str, update_cols: Optional[list] = None):
        """Help to get the 'INSERT ON DUPLICATE KEY UPDATE' sql string.
        """
        # get import cols
        db_import_cols = ', '.join([f'`{col}`' for col in df.columns.tolist()])
        db_import_cols = f'({db_import_cols})'
        # get import datas
        db_import_values = []
        for i in df.index:
            temp_values = ', '.join([f'"{escape_string(str(value))}"' for value in df.loc[i].tolist()])
            temp_values = f'({temp_values})'
            db_import_values.append(temp_values)
        db_import_values = ', '.join(db_import_values)
        # set update cols
        aliased = 'temp'
        if update_cols is None:
            update_cols = df.columns
        db_update_cols = ",".join([f'`{col}` = {aliased}.`{col}`' for col in update_cols])
        # concat SQL
        sql = f"""
        INSERT INTO `{schema}`.`{table}` {db_import_cols}
        VALUES {db_import_values} AS {aliased}
        ON DUPLICATE KEY UPDATE {db_update_cols};
        """
        return sql
        


