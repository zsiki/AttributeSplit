# AttributeSplit
QGIS Python plugin to split a layer by attribute values

The _Attribute Split_ plugin splits a loaded vector layer into several
shape files by a string or integer attribute column. Those features will be written to 
the same shape file what has the same attribute value in the selected column.
A target directory and a name prefix can be set, too. A name of the created 
shape files are set by the targer directory, the name prefix and the attribute
value. For example if the target directory is _/home/user/split_, the prefix is 
_abc-_ and the actual attribute value is _budapest_ then the output shape file
will be _/home/user/split/abc-budapest.shp_.

