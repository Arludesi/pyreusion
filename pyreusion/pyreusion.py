#%%
# Pyreusion
from datetime import datetime
import logging
import numpy as np
from pandas import DataFrame
from pandas.core.series import Series
from pymysql.converters import escape_string
import re
from typing import Optional, Union


#%%
class DFTools:
    """Pandas DataFrame common tools
    """

    @classmethod
    def cols_lower(cls, df: DataFrame, del_str: str = '', inplace: bool = False) -> DataFrame:
        """Make DataFrame columns name lower & replace special characters
        """
        new_cols = {col: (re.sub('[^\w]', '_', col.strip().replace(del_str, '')).lower()) for col in df.columns}
        logging.debug(f'{new_cols}')
        return df.rename(columns=new_cols, inplace=inplace)

    @classmethod
    def drop_unnamed_cols(cls, df: DataFrame, inplace: bool = False) -> DataFrame:
        """Drop Unnamed__XX cols for DF read from read_excel().
        """
        drop_cols = [col for col in df.columns.tolist() if 'unnamed__' in col.lower()]
        logging.debug(f'{drop_cols}')
        return df.drop(columns=drop_cols, inplace=inplace)

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

    @classmethod
    def to_datetime(cls, series: Series, format: str = '%Y-%m-%d %H:%M:%S', fillna: Optional[str] = None):
        """Turn 
        """
        series = series.astype('str')
        if fillna is not None:
            series.fillna(fillna, inplace=True)
        series = series.apply(lambda x: datetime.strptime(x, format) if x is not np.nan else x)
        return series
    
    @classmethod
    def to_bool(cls, series: Series, na_value: Union[str, int, bool] = False, to_num: bool = False):
        series = series.astype('str')
        if na_value in ['0', 0, False]:
            series.fillna('false', inplace=True)
        else:
            series.fillna('true', inplace=True)
        series = series.apply(lambda x: x.lower() if x is not np.nan else x)
        false_value = ['false', 'no', '0']
        series = series.apply(lambda x: False if x in false_value else True)
        if to_num:
            series = series.apply(lambda x: 0 if x is False else 1)
        return series
    
    @classmethod
    def enhance_replace(series: Series, dict: dict, regex: bool = False):
        series = series.astype('str')
        for new_value in dict:
            if regex:
                pattern = '|'.join([old_value.lower() for old_value in dict[new_value]])
                series = series.apply(lambda x: new_value if re.search(pattern, x.lower()) is not None else x)
            else:
                series = series.apply(lambda x: new_value if x in dict[new_value] else x)
        return series