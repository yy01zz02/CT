    proc = tablet_master.init_mysql()
    if use_mysqlctld:
      tablet_master.wait_for_mysqlctl_socket()
    else:
      utils.wait_procs([proc])
    try:
      tablet_master.mquery('mysql', 'select password from mysql.user limit 0',
                           user='root')
      password_col = 'password'
    except MySQLdb.DatabaseError:
      password_col = 'authentication_string'
    utils.wait_procs([tablet_master.teardown_mysql()])
    tablet_master.remove_tree(ignore_options=True)

    # Create a new init_db.sql file that sets up passwords for all users.
    # Then we use a db-credentials-file with the passwords.
    new_init_db = environment.tmproot + '/init_db_with_passwords.sql'
    with open(environment.vttop + '/config/init_db.sql') as fd:
      init_db = fd.read()
    with open(new_init_db, 'w') as fd: