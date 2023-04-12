# Singularity + MySQL

Case: work on an isolated Linux machine to run mysql queries using mysql-workbench. No internet connection on the machine, no easy way to install custom software.

Solution: two singularity containers, one that runs the mysql server and one that runs mysql-workbench to query the server.

## 1. Create containers

### 1.1 Create singularity container for mysql

```
singularity pull docker://library/mysql:latest
```
This generates the file `mysql_latest.sif` (pre-built available at https://drive.google.com/file/d/1dQEzCUDuwzWX-Bfjqjb_yGrs7VdgMwi9/view?usp=share_link)

### 1.2 Create singularity container for mysql-workbench

```
singularity build mysql-workbench.simg
```

This generates the file `mysql-workbench.sif` (prebuilt available at https://drive.google.com/file/d/1IHeRKDcqpS49r7Rm58bCAeUwtVrwt04B/view?usp=share_link)

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


These are also needed to solve connection issues. Here we create a user called "demo" identified with password "password". This is the user that we can set to mysql-workbench to use for connecting to the database. 

```
CREATE USER 'demo'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'demo'@'%';
```



The file `fake_individuals.csv` was created with `generate_fake_individuals.py`


### 4. Query the database via mysql-workbench

#### First time

Run `singularity exec  mysql-workbench.sif mysql-workbench`. Quit workbench and edit the file in `~/.mysql/workbench/connections.xml` to set the user "demo" and the password "password" for the connection to the database.

Then run it again and query the test database e.g. with `SELECT * FROM people LIMIT 10;`.



