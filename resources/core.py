# -*- coding: utf-8 -*-

"""
resources.core
~~~~~~~~~~~~~~

This omdule provides the core resources system.

"""

import warnings
from uuid import uuid4


__all__ = ['Interface']


def method_not_allowed(f):
    def decorator(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception, why:
            warnings.warn(str(why))
            return None

    return decorator





class Collection(object):
    """A RESTful Collection."""

    def __init__(self, interface=None, resource=None):
        self.interface = interface
        self.resource = resource
        self.ri = uuid4().hex

        super(Collection, self).__init__()

    @property
    def name(self):
        return self.interface.name_for(self)

    def __repr__(self):
        return '<collection \'{0}:{1}\'>'.format(self.name, self.ri)

    def __getitem__(self, key):
        try:
            element_exists = self.resource.element_head(key)
        # Assume element exist if head isn't provided.
        except AttributeError:
            element_exists = True


        if element_exists:
            element = Element(resource=self.resource, collection=self)
            element.ri = key

            return element


    def content(content_type):
        pass


    @method_not_allowed
    def get(self, **options):

        # fire pre get element get hook
        r = self.resource.collection_get(**options)
        # fire post get element get hook

        return r


    @method_not_allowed
    def put(self, data, **options):

        r = self.resource.collection_put(self.resource, data, **options)

        return r


    @method_not_allowed
    def patch(self, data, **options):

        r = self.resource.collection_patch(self.ri, data, **options)

        return r


    @method_not_allowed
    def post(self, data, **options):

        r = self.resource.element_post(self.ri, data, **options)

        return r


    @method_not_allowed
    def delete(self, **options):

        r = self.resource.element_delete(self.ri, **options)

        return r



class Element(object):
    """A RESTful Element."""

    def __init__(self, interface=None, collection=None):
        self.interface = interface
        self.collection = collection
        self.resource = None
        self.ri = uuid4().hex

        super(Element, self).__init__()

    def __repr__(self):
        return '<element \'{0}:{1}\'>'.format(self.name, self.ri)


    def content(content_type):
        pass


    @method_not_allowed
    def get(self, **options):

        # fire pre get element get hook
        r = self.resource.element_get(self.ri, **options)
        # fire post get element get hook

        return r


    @method_not_allowed
    def put(self, data, **options):

        r = self.resource.element_put(self.ri, data, **options)

        return r


    @method_not_allowed
    def patch(self, data, **options):

        r = self.resource.element_patch(self.ri, data, **options)

        return r


    @method_not_allowed
    def post(self, data, **options):

        r = self.resource.element_post(self.ri, data, **options)

        return r


    @method_not_allowed
    def delete(self, **options):

        r = self.resource.element_delete(self.ri, **options)

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
                return self.resources.get(key)

        return object.__getattribute__(self, key)

    def name_for(self, instance):
        """Returns the resource name for the given element/collection."""

        for name, resource in self.resources.items():
            if resource == instance:
                return name


    def map(self, key, resource=None, is_collection=True):
        """Maps a given resource to the given namespace."""

        if is_collection:
            self.resources[key] = Collection(interface=self, resource=resource())
        else:
            self.resources[key] = Element(interface=self, resource=resource())


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









