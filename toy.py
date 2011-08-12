# -*- coding: utf-8 -*-

import resources
from resources import Interface, Resource


# built in verbs
#

api = Interface()


class Bookmarks(Resource):
    """docstring for Bookmarks"""
    pass


api.map(Bookmarks, 'bookmarks')

# print api
print api.bookmarks
# print api.resources