# -*- coding: utf-8 -*-

"""
resources.core
~~~~~~~~~~~~~~

This omdule provides the core resources system.

"""

from uuid import uuid4


class Resource(object):
    """docstring for Resource"""
    def __init__(self, name=None, interface=None):

        self.name = name
        self.interface = interface
        self.uuid = uuid4().hex

        super(Resource, self).__init__()

    def __repr__(self):
        return '<resource \'{0}\'>'.format(self.name)



class Interface(object):
    """docstring for API"""

    resource = Resource()

    def __init__(self):
        self.resources = dict()

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


    def map(self, resource, key):
        self.resources[key] = resource(interface=self, name=key)







