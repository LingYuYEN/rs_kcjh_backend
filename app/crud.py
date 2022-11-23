import sqlite3
from sqlite3 import Error


# 定義資料庫位置
fastapi_db = 'fastapi_db.db'

repair_info_key_list = ['id', 'school', 'name', 'tel', 'device_type', 'repair_description', 'start_time', 'end_time', 'status', 'repair_record']

create_repair_infos_table = """ CREATE TABLE IF NOT EXISTS repair_infos (
                                        id integer PRIMARY KEY,
                                        school text NOT NULL,
                                        name text NOT NULL,
                                        tel text,
                                        device_type text,
                                        repair_description text,
                                        start_time text,
                                        end_time text,
                                        status text,
                                        repair_record text
                                    ); """


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def crud_get_repair_info_db():
    # 與 db_file 建立連結
    conn = sqlite3.connect(fastapi_db)
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    db = conn.cursor()
    cursor_arr = conn.execute('select * from repair_info;').fetchall()
    # rows = db.execute('''
    #     SELECT * from repair_info
    #     ''').fetchall()
    conn.commit()
    conn.close()
    return cursor_arr


def crud_post_repair_info_db(post_id, post_school, post_name, post_tel, post_device_type, post_repair_description, post_start_time):
    # conn = sqlite3.connect(fastapi_db)
    conn = create_connection(fastapi_db)
    if conn is not None:
        create_table(conn, create_repair_infos_table)
    else:
        print('Error! cannot create the db connection.')
    id = post_id
    school = post_school
    name = post_name
    tel = post_tel
    device_type = post_device_type
    repair_description = post_repair_description
    start_time = post_start_time
    sql_str = "insert into repair_info(id, school, name, tel, device_type, repair_description, start_time) values('{}','{}','{}','{}','{}','{}','{}');".format(id, school, name, tel, device_type, repair_description, start_time)
    conn.execute(sql_str)
    conn.commit()
    conn.close()
