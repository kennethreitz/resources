# -*- coding: utf-8 -*-

"""
resources.core
~~~~~~~~~~~~~~

This omdule provides the core resources system.

"""

import warnings
from uuid import uuid4


__all__ = ('Resource', 'Interface', 'Element')


def method_not_allowed(f):
    def decorator(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception, why:
            warnings.warn(str(why))
            return None

    return decorator



class Resource(object):
    """A RESTful Resource."""

    def __init__(self, name=None, interface=None):
        self.name = name
        self.interface = interface
        self.uuid = uuid4().hex

        super(Resource, self).__init__()

    def __repr__(self):
        return '<resource \'{0}\'>'.format(self.name)



class Collection(object):
    """A RESTful Collection."""

    def __init__(self, resource=None):
        self.resource = resource
        self.uuid = uuid4().hex
        self.ri = None

        super(Collection, self).__init__()

    def content(content_type):
        pass


    @method_not_allowed
    def get(self, **options):

        # fire pre get element get hook
        r = self.collection_get(self.ri, **options)
        # fire post get element get hook

        return r


    @method_not_allowed
    def put(self, data, **options):

        r = self.collection_put(self.ri, data, **options)

        return r


    @method_not_allowed
    def patch(self, data, **options):

        r = self.collection_patch(self.ri, data, **options)

        return r


    @method_not_allowed
    def post(self, data, **options):

        r = self.element_post(self.ri, data, **options)

        return r


    @method_not_allowed
    def delete(self, **options):

        r = self.element_delete(self.ri, **options)

        return r



class Element(object):
    """A RESTful Element."""

    def __init__(self, collection=None):
        self.collection = collection
        self.uuid = uuid4().hex
        self.ri = None

        super(Element, self).__init__()

    def content(content_type):
        pass

    @method_not_allowed
    def get(self, **options):

        # fire pre get element get hook
        r = self.element_get(self.ri, **options)
        # fire post get element get hook

        return r


    @method_not_allowed
    def put(self, data, **options):

        r = self.element_put(self.ri, data, **options)

        return r


    @method_not_allowed
    def patch(self, data, **options):

        r = self.element_patch(self.ri, data, **options)

        return r


    @method_not_allowed
    def post(self, data, **options):

        r = self.element_post(self.ri, data, **options)

        return r


    @method_not_allowed
    def delete(self, **options):

        r = self.element_delete(self.ri, **options)

        return r



class Interface(object):
    """The RESTful API Interface."""

    resource = Resource()

    def __init__(self):
        self.resources = dict()
        self.uuid = uuid4().hex

    def __repr__(self):
        return '<interface [{0}]>'.format(', '.join(self.resources.keys()))

    def __getattribute__(self, key):
        if key not in ['resources']:
            try:
                return object.__getattribute__(self, key)
            except AttributeError:
                pass

            if key in self.resources:
                return self.resources.get(key)

        return object.__getattribute__(self, key)

    def map(self, key, resource=None, collection=True):
        """Maps a given resource to the given namespace.

        If map is None (not provided), returns decorator.
        """

        if resource:
            self.resources[key] = resource(interface=self, name=key)
        else:
            # Assume decorator usage.

            def decorator(r):
                self.map(key, resource=r, collection=collection)
                return f

            return decorator









