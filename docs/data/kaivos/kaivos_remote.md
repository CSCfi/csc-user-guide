# 5. Using kaivos.csc.fi directly from your local computer

The MySQL databases in kaivos.csc.fi can be directly accessed only from the computing servers of CSC. However, you can make the database visible to your own computer using your CSC user account and port forwarding through an _ssh tunnel_.

In linux and MacOSX machines an ssh tunnel from your local computer to kaivos.csc.fi via puhti.csc.fi can be done for example with the command:

<pre>ssh -l <i>csc_username</i> -L 3306:kaivos.csc.fi:3306 puhti.csc.fi -N</pre>
The `-N` option in the end of the connection command blocks the command shell after the connection is established. Once the connection is closed also the port forwarding becomes disabled. Note that the ssh command above uses your CSC user account and password, not the database user account.

In Windows machines you can use e.g. plink program to open the tunnel. [Plink](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) can only be used through the command prompt. Below is a sample command for using plink:

<pre>plink -L 3306:kaivos.csc.fi:3306 <i>taito_username</i>@puhti.csc.fi</pre>

The tunneling commands above define that the communication to port 3306 (the default port of MySQL) in you local computer is transported to the MySQL port of _kaivos.csc.fi_ through _puhti.csc.fi_ server. As long as the connection to puhti.csc.fi is active the database in kaivos.csc.fi can be accessed from your local computer using the same MySQL commands as described above for Puhti (assuming that you have the MySQL client program installed in your local computer). The only difference compared to previous command examples is that the host section (-h) should now point to host `127.0.0.1` that refers to your local host, instead of kaivos.csc.fi.

So for example the syntax to open an interactive MySQL session would now be:
<pre>mysql -u <i>db_user_account</i> -p -h 127.0.0.1 --local <i>database_name</i></pre>

And the syntax for mysqlimport:

<pre>mysqlimport -h 127.0.0.1 -u <i>db_user_account</i> --local --compress --password <i>database_name</i> <i>input_file.table</i></pre>

In the same way, you can make your databases visible in your local computer using locally installed graphical MySQL interfaces, like [MySQL Workbench](https://www.mysql.com/products/workbench/). The only major limitation with the port forwarding is that normally ssh tunnels are not very stable. You may need to reopen the ssh connection every now and then and you should not trust that the tunnel remains usable for several hours.

For the security reasons we recommend that you always close the ssh connection when you stop using the database.
