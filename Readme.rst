Resources
=========

**Work in progress.**

*RESTful != HTTP.*

This is a framework for bringing RESTful Resources to your Python applications. It can be used in a few ways:

- To add a RESTful interface to your existing codebase.
- To power the backbone of your entire application.


Features
--------

- Simple API — makes no assumptions
- 'hyperlink' support (Resource references)
- Event/Signaling System
- Custom Verb Support (HTTP verbs out of the box)
- Content Negotiation


Usage
-----

Potentially::

    from resources import Interface, Resource

    api = Interface()

    @api.map('bookmarks')
    class Bookmarks(Resource):
        """Haystack's Bookmarks Resource."""

        __bookmarks = {}

        def element_get(self, ri):
            return self.__bookmarks.get(ri)

        ... # json content, element/collection put, &c

Now we have an API w/ a single resource: ``bookmarks``. We can access it
like so::

    >>> api.bookmarks
    <resource 'bookmarks'>

    >>> api.bookmarks['00001']
    <element <bookmarks:00001>

    >>> api.bookmarks['00001'].get()
    <bookmark 000001>

    >>> api.bookmarks['00001'].content('json').get()
    '{"bookmark": {"id": "00001"}}'


Future
------

- Build a set of web framework plugins for serving Resources via HTTP (e.g. flask-resources, django-resources).
- Build a Resources-Client module for consuming RESTful web APIs (powered by Requests).


License
-------

ISC.