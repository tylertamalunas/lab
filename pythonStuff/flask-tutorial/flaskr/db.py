import sqlite3
from datetime import datetime

import click
from flask import current_app, g 


# g is a special object that is unique for each request. It stores data that might be accessed by multiple functions during request. It is stored and reused instead of creating a new connection if this funciton is called a second time in the same request. 
# current_app is a special object that points to the Flask app handling the request. 
# sqlite3.connect() establishes a connection to the file pointed at by DATABASE
# sqlite3.Row tells connection to return rows that behave like dicts. Allows accessing columns by name.

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
                )
        g.db.row_factory = sqlite3.Row 

    return g.db 


# close_db checks if connection was created. If exists, it is closed. 
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# open_resource() opens file relative to flaskr package. (useful since you dont always know the location)
# get_db returns a database connection
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# click.command() defines a command line called init-db that calls init_db function and shows success message. 
@click.command('init.db')
def init_db_command():
    """Clear the existing data and create new tables"""
    init_db()
    click.echo('Initialized the database.')

# this tells Python how to interpret the timestamp values in database
sqlite3.register_converter(
        "timestamp", lambda v: datetime.fromisoformat(v.decode())
        )
