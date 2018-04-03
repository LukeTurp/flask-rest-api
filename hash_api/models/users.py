#!/usr/bin/env python3

import datetime

from hash_api.base import db

class User(db.Document):
    username = db.StringField(max_length=50)
    password = db.StringField(max_length=100)
    registerdate = db.DateTimeField(default=datetime.datetime.now)
