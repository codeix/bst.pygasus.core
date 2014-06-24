from zope.interface import Interface
from zope.interface import Attribute


class IApplicationContext(Interface):
    title = Attribute('title of application')
    resources = Attribute('fanstatic resources for all js and css')
    application = Attribute('classname of application entry point eg. "bielbienne.iptt.Application"')
    namespace = Attribute('Extjs name space eg: "bielbienne.iptt"')

