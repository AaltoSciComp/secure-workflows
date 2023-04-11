# Singularity + MySQL

Case: work on an isolated Linux machine to run mysql queries using mysql-workbench. No internet connection on the machine, no easy way to install custom software.

Solution: two singularity containers, one that runs the mysql server and one that runs mysql-workbench to query the server.

## 1. Create containers

### 1.1 Create singularity container for mysql

```
apptainer pull docker://library/mysql:latest
```
This generates the file `mysql_latest.sif` (already available in the repository)

### 1.2 Create singularity container for mysql-workbench

```
apptainer build mysql-workbench.simg
```

This generates the file `mysql-workbench.sif` (already available in the repository)

### 2. Run the database

- Open a terminal and navigate to the right folder 
- `bash run_mysql.sh`

### 3. Test the database via command line

Run the following queries to create a test database.

```
create database test;
use test;
create table people (
    id BIGINT NOT NULL,
    name varchar(30),
    surname varchar(30),
    PRIMARY KEY (id)
) ENGINE = INNODB; 

SET GLOBAL local_infile=1;
LOAD DATA LOCAL INFILE "/var/lib/mysql-files/fake_individuals.csv" INTO TABLE people FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;
SELECT * FROM people LIMIT 10;  
```

The file `fake_individuals.csv` was created with `generate_fake_individuals.py`


### 4. Query the database via mysql-workbench

#### First time

Run `apptainer exec  mysql_workbench.sif mysql-workbench`. Quit workbench and edit the file in `~/.mysql/workbench/connections.xml` to set the root password for the connection to the database.

Then run it again and query the test database e.g. with `SELECT * FROM people LIMIT 10;`.



