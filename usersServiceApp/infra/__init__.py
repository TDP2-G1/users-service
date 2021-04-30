from usersServiceApp import database
from flask import current_app

from usersServiceApp.errors.usersError import DataBaseError


def create_in_db(data_model):
    #try:
        # add to the database session
        database.db.session.add(data_model)

        # commit to persist into the database
        database.db.session.commit()
    #except:
    #    raise DataBaseError
