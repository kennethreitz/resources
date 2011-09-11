# -*- coding: utf-8 -*-

import resources
from resources import Interface


# built in verbs
#

api = Interface()


@api.collection('bookmarks')
class Bookmarks(object):
    """Haystack's Bookmarks Resource."""

    # __bookmarks = {'test': 'hi'}
    __bookmarks = {}

    # get(*args, **kwargs) <-- automatic
    # ri = resource identifier

    def element_head(self, ri):
        return ri in self.__bookmarks

    def element_get(self, ri):
        return self.__bookmarks.get(ri)

    def element_put(self, ri, data):
        pass

    def element_patch(self, ri, data):
        pass

    def element_post(self, ri, data):
        pass

    def element_delete(self, ri):
        pass

    def collection_get(self, **options):
        return self.__bookmarks.values()

    def collection_put(self, ri, data):
        pass

    def collection_patch(self, ri, data):
        pass

    def collection_post(self, ri, data):
        pass

    def collection_delete(self, ri):
        pass


    def __from_json(ri):
        pass



# api.map('bookmarks', Bookmarks)


# @api.when.bookmarks.post
def test(x):
    print 'hi'


#api.before_get
#api.before_put
#api.before_post
#api.before_delete
#api.before_patch

#api.after_get
#api.after_put
#api.after_post
#api.after_delete
#api.after_patch


# print api
print api.bookmarks
# print api.resources
print api.bookmarks.get()

# print api.bookmarks.get(id='0')

# api.bookmarks.get()
# print api.bookmarks['test2']


# >>> print api.bookmarks[00001]
# <element <bookmarks:00001>
# You'll be able to use this as a reference in other objects

# >>> print api.bookmarks[00001].get()
# <bookmark 000001>


# >>> api.bookmarks[00001].content('json').get()
# <bookmark 000001>


# print test('x')
# print api.resources