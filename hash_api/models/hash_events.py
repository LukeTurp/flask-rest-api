#!/usr/bin/env python3

import datetime

from hash_api.base import db


class HashEvent(db.Document):
    abspath = db.StringField(max_length=255)
    filename = db.StringField(max_length=50)
    hashvalue = db.StringField(max_length=100)
    rundate = db.DateTimeField(default=datetime.datetime.now)
