import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """创建数据库连接"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"成功连接到SQLite数据库，版本号: {sqlite3.version}")
        return conn
    except Error as e:
        print(f"连接错误: {e}")
    return conn

def create_table(conn, create_table_sql):
    """根据SQL语句创建表"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("表创建成功")
    except Error as e:
        print(f"创建表错误: {e}")

def insert_user(conn, user):
    """插入新用户"""
    sql = ''' INSERT INTO users(name, email, age)
              VALUES(?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

def select_all_users(conn):
    """查询所有用户"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    return rows

def select_user_by_id(conn, user_id):
    """根据ID查询用户"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
    row = cur.fetchone()
    return row

def update_user_age(conn, user):
    """更新用户年龄"""
    sql = ''' UPDATE users
              SET age = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()

def delete_user(conn, user_id):
    """删除用户"""
    sql = 'DELETE FROM users WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (user_id,))
    conn.commit()

def main():
    database = "example.db"  # 数据库文件名

    # 创建用户表的SQL语句
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL UNIQUE,
                                        age integer
                                    ); """

    # 创建数据库连接
    conn = create_connection(database)

    if conn is not None:
        # 创建用户表
        create_table(conn, sql_create_users_table)
        
        # 插入用户
        user1 = ("张三", "zhangsan@example.com", 30)
        user1_id = insert_user(conn, user1)
        print(f"插入用户ID: {user1_id}")
        
        user2 = ("李四", "lisi@example.com", 25)
        user2_id = insert_user(conn, user2)
        print(f"插入用户ID: {user2_id}")
        
        # 查询所有用户
        print("\n所有用户:")
        for user in select_all_users(conn):
            print(user)
        
        # 根据ID查询用户
        print(f"\nID为{user1_id}的用户:")
        print(select_user_by_id(conn, user1_id))
        
        # 更新用户年龄
        update_user_age(conn, (31, user1_id))
        print(f"\n更新后ID为{user1_id}的用户:")
        print(select_user_by_id(conn, user1_id))
        
        # 删除用户
        delete_user(conn, user2_id)
        print("\n删除用户后所有用户:")
        for user in select_all_users(conn):
            print(user)
        
        # 关闭连接
        conn.close()
    else:
        print("无法创建数据库连接")

if __name__ == '__main__':
    main()
