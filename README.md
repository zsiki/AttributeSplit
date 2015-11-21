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

The plugin was tested with Shape file, SpatiaLite and PostGIS.

## Install the plugin

Actually the plugin has a beta version and is not available in the plugins.qgis.org
repositora. You can install it manually.

### Install from zip file

Download the zip file from the http://github.com/zsiki/AttributeSplit page, find the link
at the lower right corner. Unzip the file to the personal plugin folder of your local
machine:

- ~/.qgis2/python/plugins (Linux)
- \users\\*user_name*\\.qgis2\python\plugins (Windows 7+)
- \Document ans Settings\\*user_name*\\.qgis2\python\plugins (Windows XP)

Rename the *AttributeSplit-master* folder to *AttributeSplit*

Start/restart QGIS and turn on the plugin in the *Manage and install plugins* dialog.

### Install from git

Clone the repository to your local QGIS  pesonal plugin folder.

- change your actual folder to your personal plugin folder (e.g. ~/.qgis2/python/plugins on Linux)
- *git clone https://github.com/zsiki/AttributeSplit.git*
