For Taipy to instantiate a [Data node](../concepts/data-node.md), a data node configuration must be provided. The
[`DataNodeConfig`](../../../reference/#taipy.core.config.data_node_config.DataNodeConfig) is
used to configure the various data nodes Taipy will manipulate. To configure a new `DataNodeConfig`, you can use
the `taipy.configure_data_node()` method.

```python linenums="1"
    import taipy as tp
    data_node_cfg = tp.configure_data_node(name="data_node_cfg")
```

On the previous code, we configure a simple data node just providing a name identifier as a string "data_node_cfg".

More optional attributes are available on data nodes. Here is the list of attributes:

- The config `name` corresponds to the identifier of the data node config. It is a **mandatory** parameter
that must be unique. We strongly recommend using lowercase alphanumeric characters, dash character '-', or
underscore character '\_' (a name compatible with a python variable name).

- The `scope` attribute is from type [`Taipy.Scope`](../../../reference/#taipy.core.data.scope.Scope).
It corresponds to the [scope](../concepts/scope.md) of the data node that will be instantiated from the data node
configuration. The **default value** is `Scope.SCENARIO`.

- The storage `storage_type` is a parameter that corresponds to the type of storage of the data node. The possible
string values are ["pickle"](#pickle) (**the default value**), ["csv"](#csv), ["excel"](#excel), ["sql"](#sql).
["in_memory"](#in-memory), ["generic"](#generic).
As explained in the following subsections, depending on the `storage_type`, other configuration attributes
will need to be provided in the `properties` parameter.

- Any other custom attribute can be provided through the `properties` dictionary (a description, a tag, etc.)
All the properties will be given to the data nodes instantiated from this data node configuration.
This `properties` dictionary is also used to configure the parameters specific to each storage type.


Below two examples of data node configurations.

```python linenums="1"
import taipy as tp
from taipy import Scope

date_cfg = tp.configure_data_node(name="date_cfg", description="The current date of the scenario")

model_cfg = tp.configure_data_node(name="model_cfg",
                                   scope=Scope.CYCLE,
                                   storage_type="pickle",
                                   description="The trained model shared by all scenarios",
                                   code=54
                                   )
```
In line 4, we configure a simple data node. The `name` identifier is "date_cfg". Its `scope` is the default
value `SCENARIO`. The `storage_type` is also the default value "pickle". We also add an optional custom
`description`. This property will be passed to the data nodes instantiated from this config.

Then in line 6, we add another data node configuration. The `name` identifier is "model_cfg". Its `scope` is
`CYCLE`, so the corresponding data nodes will be shared by all the scenarios from the same cycle. The
`storage_type` is "pickle" as well, and two optional custom properties are added; a string `description` and
an integer `code`. These two properties will be passed to the data nodes instantiated from this config.


# Storage type
Taipy proposes various predefined _data nodes_ corresponding to the most popular _storage types_. Thanks to predefined
_data nodes_, the data scientist developer does not need to spend much time configuring the _storage types_ or the
_query system_. Most of the time, a predefined _data node_ corresponding to a basic and standard use case satisfies
the user's need like pickle file, csv file, sql table, Excel sheet, etc.

The various predefined _storage types_ are mainly used for input data. Indeed, the input data is usually provided by an
external component, and the data scientist user does not control the format.

However, in most cases, particularly for intermediate or output _data nodes_, it is not relevant to prefer one _storage
type_. The end-user wants to manipulate the corresponding data within the Taipy application. Still, the user does not
have any particular specifications regarding the _storage type_. In such a case, the data scientist developer does not
need to spend time configuring the _storage type_. Taipy recommends using the default _storage type_ pickle that does
not require any configuration.

In case a more specific method to store, read and write the data is needed by the user, Taipy proposes a _Generic data
node_ that can be used for any _storage type_ or any kind of _query system_. The user only needs to provide two python
functions, one for reading and one for writing the data.

Each predefined data node is describe in a subsequent section.

# Pickle

A [PickleDataNode](../../../reference/#taipy.core.data.pickle.PickleDataNode) is a specific data node used to model
pickle data.
To add a new _pickle_ data node configuration, the `taipy.configure_pickle_data_node` method can be used. In
addition to the generic parameters described in the previous section
[Data node configuration](data-node-config.md), two optional parameters can be provided.

-   The `path` parameter represents the file path used by Taipy to read and write the data.
    If the pickle file already exists (in the case of a shared input data node, for instance), it is necessary
    to provide the file path as the _path_ parameter. If no value is provided, Taipy will use an internal path
    in the Taipy storage folder (more details on the Taipy storage folder configuration available on the
    [Global configuration](global-config.md) documentation).

-   If the `default_data` is provided, the data node is automatically written with the corresponding
    value. Any serializable Python object can be used.

```python linenums="1"
   import taipy as tp
   from taipy import Scope

   date_cfg = tp.configure_pickle_data_node(name="date_cfg", default_data=datetime(2022, 1, 25))

   model_cfg = tp.configure_pickle_data_node(name="model_cfg",
                                             path="path/to/my/model.p",
                                             description="The trained model")
```
In line 4, we configure a simple pickle data node. The name identifier is "date_cfg". The scope is `SCENARIO`
(default value), and a default data is provided.

In lines 6, 7, and 8, we add another pickle data node configuration. The name identifier is "model_cfg". The default
`SCENARIO` scope is used. Since the data node config corresponds to a pre-existing pickle file, a path
"path/to/my/model.p" is provided. We also added an optional custom description.

!!! Note

    To configure a pickle data node, it is equivalent to use the method `taipy.configure_pickle_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="pickle"`.

# Csv

A [CSVDataNode](../../../reference/#taipy.core.data.csv.CSVDataNode) data node is a specific data node used to
model csv file data. To add a new _csv_ data node
configuration, the `taipy.configure_csv_data_node` method can be used. In addition to the generic
parameters described in the previous section
[Data node configuration](data-node-config.md), one mandatory and
two optional parameters can be provided.

- The `path` parameter is a mandatory parameter and represents the csv file path used by Taipy to read and write
the data.

- The `has_header` parameter represents if the file has a header of not. If `has_header` is `True`,
Taipy will use the 1st row in the csv file as the header. By default, `has_header` is `True`.

- When the `exposed_type` is given as parameter, if the `exposed_type` value provided is `numpy`, the
data node will read the csv file to a numpy array. If the provided value is a custom class, data node
will create a list of custom object with the given custom class, each object will represent a row in the csv
file.If `exposed_type` is not provided, the data node will read the csv file as a pandas DataFrame.

```python linenums="1"
import taipy as tp
from taipy import Scope

date_cfg = tp.configure_csv_data_node(name="historical_temperature", path="path/hist_temp.csv", has_header=True, exposed_type="numpy")

model_cfg = tp.configure_pickle_data_node(name="sale_history",
                                          path="path/sale_history.csv",
                                          exposed_type=SaleRow)
```
In line 4, we configure a basic csv data node. The `name` identifier is "historical_temperature". Its `scope` is by
default `SCENARIO`. The path corresponds to the file _hist_temp.csv_. The property `has_header` being True,
representing the csv file has a header.

In lines 6, 7, and 8, we then add another csv data node configuration. The `name` identifier is "sale_history". The
default `SCENARIO` scope is used again. Since we have a custom class pre-defined for this csv file (SaleRow), we
provide it as the `exposed_type` parameter.

!!! Note

    To configure a csv data node, it is equivalent to use the method `taipy.configure_csv_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="csv"`.

# Excel

An [ExcelDataNode](../../../reference/#taipy.core.data.excel.ExcelDataNode) is a specific data node used to model xlsx
file data. To add a new _Excel_ data node configuration, the `taipy.configure_excel_data_node` method can be used.
In addition to the generic parameters described in the previous section
[Data node configuration](data-node-config.md), a mandatory and three optional parameters can be provided.

- The `path` is a mandatory parameter that represents the Excel file path used by Taipy to read and write the data.

- The `has_header` parameter represents if the file has a header of not. If `has_header` is `True`,
Taipy will use the 1st row in the Excel file as the header. By default, `has_header` is `True`.

- The `sheet_name` parameter represents which specific sheet in the Excel file to read. If `sheet_name`
is provided with a list of sheet names, it will return a dictionary with the key being the sheet name and
the value being the data of the corresponding sheet. If a string is provided, data node will read only the
data of the corresponding sheet. The default value of `sheet_name` is "Sheet1".

- When the `exposed_type` is given as parameter, if the `exposed_type` value provided is `numpy`, the data
node will read the Excel file to a numpy array. If the provided value is a custom class, data node will
create a list of custom object with the given custom class, each object will represent a row in the Excel
file. If `exposed_type` is not provided, the data node will read the Excel file as a pandas DataFrame.

```python linenums="1"
   import taipy as tp
   from taipy import Scope

   date_cfg = tp.configure_excel_data_node(name="historical_temperature", path="path/hist_temp.xlsx", has_header=True, exposed_type="numpy")

   model_cfg = tp.configure_excel_data_node(name="sale_history",
                                             path="path/sale_history.xlsx",
                                             sheet_name=["January", "February"]
                                             exposed_type=SaleRow)
```

In line 4, we configure an Excel data node. The `name` identifier is "historical_temperature". Its `scope` is
`SCENARIO` (default value), and the path is the file hist_temp.xlsx. With `has_header` being True, the
Excel file must have a header. The `sheet_name` is not provided so Taipy will use the default value "Sheet1".

In lines 6, 7, 8, and 9, we then add another csv data node configuration. The `name` identifier is "sale_history", the
default `SCENARIO` scope is used. Since we have a custom class pre-defined for this Excel file, we will provide it in
the `exposed_type`. We also provide the list of specific sheets we want to use as the `sheet_name` parameter.

!!! Note

    To configure an Excel data node, it is equivalent to use the method `taipy.configure_excel_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="excel"`.

# Sql

A [SqlDataNode](../../../reference/#taipy.core.data.sql.SQLDataNode) is a specific data node used to model Sql
data. To add a new _sql_ data node configuration, the `taipy.configure_sql_data_node` method can be used. In
addition to the generic parameters described in the previous section
[Data node configuration](data-node-config.md), multiple
parameters can be provided.

- The `db_username` parameter represents the database username that will be used by Taipy to access the database.
- The `db_password` parameter represents the database user's password that will be used by Taipy to access the database.
- The `db_name` parameter represents the name of the database.
- The `db_engine` parameter represents the engine of the database.
- The `read_query` parameter represents the SQL query that will be used by Taipy to read the data from the database.
- The `write_table` parameter represents the name of the table in the database that Taipy will be writing the data to.
- The `db_port` parameter represents the database port that will be used by Taipy to access the database. The
  default value of `db_port` is 1433

```python linenums="1"
import taipy as tp
from taipy import Scope

date_cfg = tp.configure_sql_data_node(name="forecasts",
                                      db_username="admin",
                                      db_password="password",
                                      db_name="taipy",
                                      db_engine="mssql",
                                      read_query="SELECT * from forecast_table",
                                      write_table= "forecast_table")
```
In the previous example, we configure a _sql_ data node. The `name` identifier is "forecasts". Its scope is the
default value `SCENARIO`. The database username is "admin", the user's password is "password", the database name
is "taipy", and the database engine is `mssql` (short for Microsoft SQL). The read query will be "SELECT * from
forecast_table", and the table the data will be written to is "forecast_table".


!!! Note

    To configure a sql data node, it is equivalent to use the method `taipy.configure_sql_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="sql"`.

# Generic

An [GenericDataNode](../../../reference/#taipy.core.data.generic.GenericDataNode) is a specific data node used to model
generic data type where the read and the write functions are defined by the user. To add a new _generic_ data node
configuration, the `taipy.configure_generic_data_node` method can be used. In addition to the parameters
described in the previous section [Data node configuration](data-node-config.md), two optional parameters can be
provided.

- The `read_fct` is a mandatory parameter that represents a python function provided by the user. It will
be used to read the data.

- The `write_fct` is a mandatory parameter that represents a python function provided by the user. It will
be used to write the data.

```python linenums="1"
    import taipy as tp
    from taipy import Scope

    date_cfg = tp.configure_generic_data_node(name="historical_data", read_fct=read_data, write_fct=write_data)
```
In this small example, we configure a generic data node. The `name` identifier is "historical_data". We provide two
python functions as `read_fct` and `write_fct` parameters to read and write the data.


!!! Note

    To configure a generic data node, it is equivalent to use the method `taipy.configure_generic_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="generic"`.

# In memory

An [InMemoryDataNode](../../../reference/#taipy.core.data.in_memory.InMemoryDataNode) is a specific data node used to
model any data in the RAM. To add a new in_memory data node configuration, the `taipy.configure_in_memory_data_node`
method can be used. In addition to the generic parameters described in the previous section
[Data node configuration](data-node-config.md), an optional parameter can be provided.

-   If the `default_data` is given as parameter, the data node is automatically written with the corresponding
    value. Any python object can be used.

```python linenums="1"
import taipy as tp
from taipy import Scope

date_cfg = tp.configure_in_memory_data_node(name="date_cfg", default_data=datetime(2022, 1, 25))
```

In this example, we configure an in_memory data node. The `name` identifier is "date_cfg", the scope is `SCENARIO`
(default value)., and a default data is provided.

!!! Warning

    Since the data is stored in memory, it cannot be used in a multiprocess environment. (See
    [Job configuration](job-config.md#standalone) for more details).

!!! Note

    To configure an in_memory data node, it is equivalent to use the method `taipy.configure_in_memory_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="in_memory"`.


[:material-arrow-right: Next section introduces the task configuration](task-config.md).