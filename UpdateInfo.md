# UpdateInfo
* 1.1.0.0
    * Add Operations
        * Add Operations.unzip_file()
        * Add Operations.chk_file()
        * Add Operations.ls()
        * Add Operations.get_encoding()
    * Add Converters.turn_docstr_dict()

* 1.0.9.0
    * Refine DFTools.to_decimal() logic
        * Default return type Decimal
        * add to_str arg for return type str

* 1.0.8.0
    * Update DFTools.to_datetime()
    * Daprecate DFTools.str_datetime()

* 1.0.7.0
    * Add Converters.utc_to_datetime()
    * DFTools.str_datetime() support utc format
        * e.g. '2021-09-30T07:05:28+07:00'
        * use format like '%Y-%m-%dT%H:%M:%S%z'

* 1.0.6.0
    * Add DFTools.str_datetime()
    * Add DFTools.str_datetime_cols()
    * Add DFTools.str_string_cols()
    * Add DFTools.str_int_cols()
    * Add DFTools.str_decimal_cols()
    * Add DFTools.str_bool_cols()
    * Add DFTools.to_decimal()
    * Add DFTools.to_int()

* 1.0.5
    * Add DFTools.to_string()

* 1.0.4
    * Add DFTools.to_datetime()
    * Add DFTools.to_bool()
    * Add DFTools.enhance_replace()

* 1.0.3
    * Fix import error
    * Refine setup.bat logic

* 1.0.2.3
    * Add DFTools.cols_lower()
    * Add DFTools.drop_unnamed_cols()
    * Add DFTools.get_duplicate_update_sql()
