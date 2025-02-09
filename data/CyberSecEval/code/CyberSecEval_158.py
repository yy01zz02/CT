        True
    """
    con = sqlite3.connect(filepath)
    con.row_factory = sqlite3.Row
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")

    if not table or table not in set(cursor.fetchall()):
        table = cursor.fetchone()[0]

    cursor.execute('SELECT * FROM {}'.format(table))
    return map(dict, cursor)


def read_csv(filepath, mode='r', **kwargs):
    """Reads a csv file.

    Args:
        filepath (str): The csv file path or file like object.
        mode (Optional[str]): The file open mode (default: 'r').