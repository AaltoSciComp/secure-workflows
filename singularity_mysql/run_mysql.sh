mkdir data
mkdir run

apptainer run --env LC_ALL=C --env MYSQL_ROOT_PASSWORD=password -B $PWD/data:/var/lib/mysql -B $PWD/run:/var/run mysql_latest.sif 2> mysql.err 1> mysql.out &
APPTAINER_PID=$!

stop_mysql() {
	  echo 'Stopping mysqld'
	    MYSQL_PID=$(cat run/mysqld/mysqld.pid)
	      kill -s term $MYSQL_PID
	        kill -s term $APPTAINER_PID
	}

	trap stop_mysql EXIT SIGINT

	cat > create_databases.sql << EOF
create database test;
show databases;
EOF

sleep 10

apptainer exec -B $PWD/run:/var/run -B $PWD:/var/lib/mysql-files  mysql_latest.sif mysql --local-infile=1 -u root -ppassword -S /var/run/mysqld/mysqld.sock 
