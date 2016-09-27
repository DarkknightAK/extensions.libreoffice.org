from plone import api
from Products.Five.browser import BrowserView
from collective.transmogrifier.transmogrifier import Transmogrifier
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides


class PloneorgMigrationMain(BrowserView):

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        portal = api.portal.get()
        transmogrifier = Transmogrifier(portal)
        transmogrifier('plone.org.main')


class DFMigrationMain(BrowserView):

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        portal = api.portal.get()
        transmogrifier = Transmogrifier(portal)
        transmogrifier('df.main')
        return 'DONE!'


class MagicDebug(BrowserView):

    def __call__(self):
        import ipdb; ipdb.set_trace()