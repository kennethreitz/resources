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
        self.ri = uuid4().hex
        self.contains = None

        super(Resource, self).__init__()

    def __repr__(self):
        return '<resource \'{0}\'>'.format(self.name)



class Collection(object):
    """A RESTful Collection."""

    def __init__(self, resource=None):
        self.resource = resource
        self.ri = uuid4().hex

        super(Collection, self).__init__()

    def __repr__(self):
        return '<collection \'{0}:{1}\'>'.format(self.resource.name, self.ri)

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

    def __init__(self, resource=None, collection=None):
        self.resource = resource
        self.collection = collection
        self.ri = uuid4().hex

        super(Element, self).__init__()

    def __repr__(self):
        return '<element \'{0}:{1}\'>'.format(self.resource.name, self.ri)


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

    def __init__(self):
        self.resources = dict()
        self.ri = uuid4().hex

    def __repr__(self):
        return '<interface [{0}]>'.format(', '.join(self.resources.keys()))

    def __getattribute__(self, key):
        if key not in ['resources']:
            try:
                return object.__getattribute__(self, key)
            except AttributeError:
                pass

            if key in self.resources:
                return self.resources.get(key).contains

        return object.__getattribute__(self, key)


    def map(self, key, resource=None, is_collection=True):
        """Maps a given resource to the given namespace."""

        new_resource = resource(interface=self, name=key)
        self.resources[key] = new_resource

        if is_collection:
            self.resources[key].contains = Collection(resource=new_resource)
        else:
            self.resources[key].contains = Element(resource=new_resource)


    def element(self, key):
        """API element route decorator."""

        def decorator(r):
            self.map(key, resource=r, is_collection=False)
            return r

        return decorator


    def collection(self, key):
        """API collection route decorator."""

        def decorator(r):
            self.map(key, resource=r, is_collection=True)
            return r

        return decorator









