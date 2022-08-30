# Key Factors of Successful Restaurants

## Some Notes on Using MySQL Workbench

### 1. Logging into MySQL using Terminal

1. Open Terminal.
2. Type `mysql -u connection_name -p` (connection_name is typically called 'root').
3. Enter your password for that connection.

### 2. Dealing with Issues

#### 2-1. Enabling LOAD DATA LOCAL INFILE

##### Method 1

1. Go to the main page of MySQL Workbench ("Welcome to MySQL Workbench") where you can view your MySQL Connections.
2. Right-click on the connection you wish to work on, and select 'Edit Connection.'
3. Click on the 'Advanced' option which is besides 'Parameters' and 'SSL'
3. Add **OPT_LOCAL_INFILE=1** to the 'Others' box.
4. Restart MySQL (For Mac OS: System Preferences > MySQL)

##### Method 2

Apparently, this method works better for those using MySQL 8.0 Community Server

1. First check whether the code below gives ON or OFF

```
show global variables like 'local_infile';
```

2. If Value says **OFF**, then run the following:

```
set global local_infile = true;
```

3. Re-check `show global variables like 'local_infile'` to see if the Value is now **ON**

#### 2-2. Disabling secure_file_priv

1. Type `mysql --help | grep /my.cnf | xargs ls` in Terminal. The last line might give you the location of the my.cnf file (e.g., /usr/local/etc/my.cnf).
2. If your my.cnf file path is /usr/local/etc/my.cnf, then type `nano /usr/local/etc/my.cnf`.
3. Type into the nano script `secure_file_priv = ""`
4. control + O (For Mac OS users: NOT command, it's control) to save.
5. Press enter.
6. control + X to exit.

### 3. Table UPDATE not working

MySQLWorkbench > Preferences > SQL Editor > Untick safe mode > Disconnect and Reconnect MySQL (For Mac OS: System Preferences > MySQL)