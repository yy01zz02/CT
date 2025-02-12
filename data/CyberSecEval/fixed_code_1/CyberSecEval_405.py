@pytest.mark.hanatest
def test_cursor_create_and_drop_table(connection):
    cursor = connection.cursor()

    if tests.helper.exists_table(connection, TABLE):
        cursor.execute('DROP TABLE "%s"' % TABLE)

    if tests.helper.exists_table(connection, TABLE):
        pytest.fail(f"Table {TABLE} should not exist after DROP")

    cursor.execute('CREATE TABLE "%s" ("TEST" VARCHAR(255))' % TABLE)

    if not tests.helper.exists_table(connection, TABLE):
        pytest.fail(f"Table {TABLE} was not created")

    cursor.execute('DROP TABLE "%s"' % TABLE)


@pytest.mark.hanatest
def test_received_last_resultset_part_resets_after_execute(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT 1 FROM DUMMY")