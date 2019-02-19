# Blob Plotter
### Trevor Nierman
##### 02/11/2019

This program queries an SQL database, retrieves tracer data, and graphs it, according to the specifications of the 2019 LP Technologies Junior Software Engineering Test.

## Execution

To execute this program, simply use 
```
python blobPlotter.py
```

## Requirements
This program was written in python 2.7, and has the following dependencies:

|pip packages|Description|pip installation|
|------|-----|-----|
|matplotlib|Draws and plots data onto a GUI|pip install matplotlib|

In addition to pip packages, additional packages may have to be installed via the package manager:

|System Packages|Description|System command|
|-----|-----|-----|
|Python-MySQLDB| Connects to a mySQL database|[Debian] apt-get install python-mysqldb \n[RHEL] yum install MySQL-python|
|Python-tk|A tool to draw windows and GUI systems with python|[Debian] apt-get install python-tk \n[RHEL] yum install python-tk| 

## Database Credentials
The database credentials for this program also need to be specified under the *database variables* subsection of the *variables* section.

|Variable|Definition|Default|
|-----|-----|-----|
|dbUser|Database user|"root"|
|dbPassword|User password for the database| "changeme"|
|dbHost|Database host address|"localhost|
|dbName|Name of the database|"lpTechTest"|

## Graph stylization
The graph can be stylized using the following variables located in the *Graph variables* subsection of the *variables* section.

|Variable|Definition|Default|
|-----|-----|-----|
|graphDelay|Time in seconds between loading next data set into graph|1|
|graphBackgroundColor|Color of the graph background| "black"|
|graphLineColor|Color of the line in the graph|"yellow"|
|graphLineWidth|Controls the width of the line on the graph|0.5|
|gridColor|Color of the dashed grid on the graph|"grey"|

## Issues
This was developed on a Ubuntu Budgie development VM, and due to mySQL's permission set on that platform (and my own inexperience as a DBA), some errors arose with permissions when testing. 

If the connection to the database fails, try running again as `sudo`.

