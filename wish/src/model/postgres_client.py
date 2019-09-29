from config import config
import psycopg2
import uuid

##
#
#     - *dbname*: the database name
#     - *database*: the database name (only as keyword argument)
#     - *user*: user name used to authenticate
#     - *password*: password used to authenticate
#     - *host*: database host address (defaults to UNIX socket if not provided)
#     - *port*: connection port number (defaults to 5432 if not provided)
##
from model.wish import Wish

conn = psycopg2.connect(dbname=config.db_name, user=config.user_name,
                        password=config.user_pass, host=config.db_host,
                        port=config.db_port)
_cursor = conn.cursor()


def close_connections():
    _cursor.close()
    conn.close()


def get_all_wishes(limit=10):
    _cursor.execute("select * from userWishcontext limit 10")
    records = _cursor.fetchall()
    close_connections()
    return records


def get_wishes_by_name(name) -> str:
    _cursor.execute(format("select * from userWishcontext where name = '%s' ") % str(name))
    records = _cursor.fetchall()
    close_connections()
    return records


def set_wish(wish: Wish) -> str:
    _cursor.execute("insert into userWishcontext (wish_uid, name, start_ts, end_ts, price, context)"
                    " values({wish_uid}, {name},{date_start}, "
                    "{date_end}, {price}, {description});".format(wish_uid=wish.uid, name=wish.name,
                                                                  date_start=wish.dt_start,
                                                                  date_end=wish.dt_end, price=wish.price,
                                                                  description=wish.description))
    try:
        _cursor.fetchall()
    except:
        return "not ok"

    return 'ok'


def get_wish_by_field(field) -> str:
    pass


def get_wish_by_timezone(start_date, end_date) -> str:
    pass

