import snowflake.connector as sf

def get_rowcount(sql):
    conn = sf.connect(
        user="swarna",
        password="Password01",
        account="fs01479.west-europe.azure",
        warehouse="COMPUTE_WH",
        database="demo_db",
        schema="public"
    )

    try:
        cur = conn.cursor()
        cur.execute("Use Role SysAdmin")
        cur.execute(sql)
        rowCount = cur.rowcount
        cur.close()

    except Exception as e:
        print(e)
    finally:
        conn.close()

    return rowCount