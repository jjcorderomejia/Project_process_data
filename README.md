# jobsity_challenge

Overview:

The project was developed using python for coding the automation and for database was choosen Mysql

Instructions.

First it is neccesary to create a database in phpmyadmin named "jobsity".  the user is root and the password is ""

Inside the api folder there are the next file:
    create_tables.sql
Please execute it on a phpadmin environment inside the jobsity database in order to create the tables `api_trips` and `api_trips_group`

The main code for the ingesting automation is inside the file views.py inside the api folfer.

The class load_trips_class contains the logic for loading the trips.csv file.  I tested versions of this file for about 2,000,000 records getting responde times lower that a minute.

Answers for questions:

There must be an automated process to ingest and store the data:
Answer:  Yes, the whole process is in the class load_trips_class inside the file views.py the solutions is a REST API develope in Visual Studio Code

Trips with similar origin, destination, and time of day should be grouped together
Answer.  Inside the class load_trips_class there is the logic that group the information in the table `api_trips_group` just as requested.

Develop a way to inform the user about the status of the data ingestion without using a polling solution
Answer:  The API returns ans answer '{"message": "Successful"}' if the loading process is successful.

The solution should be scalable to 100 million entries. It is encouraged to simplify the data by a data model. Please add proof that the solution is scalable.
Answer: The solution insert the informartion to the database in 10,000 rows blocks and performs commit.  this approach helps the process divide the csv in parts and load small parts to the database.  In case the CSV is about 100,000,000 rows the database or application is not going to collapse.  I tested this solution with a 2,000,000 csv file and executed in less that a minute.

Use a SQL database
Answer: I used MySql for this project.

Containerize your solution.
Answer:  I used devops techniques so the API can use classes for each solution.

Sketch up how you would set up the application using any cloud provider (AWS, GoogleCloud, etc).
Answer.  the python soliution is easy to migrate to a cloud solution and the MySql database can be replaced for a cloud database.

Include a .sql file with queries to answer these questions:
○ From the two most commonly appearing regions, which is the latest datasource?
    Answer:  Please check answer in two_regions_datasource.sql file inside api folder. Tested in MySQL database.
○ What regions has the "cheap_mobile" datasource appeared in?
    Answer: Please check answer in region_cheap_datasource.sql file inside api folder. Tested in MySQL database.
