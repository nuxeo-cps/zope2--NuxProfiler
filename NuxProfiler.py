from Globals import InitializeClass, DTMLFile
from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from OFS.PropertyManager import PropertyManager
from MonkeyPatcher import patchModuleFunction

import hotshot, sys, os

LOGFILE = "hotshot.data"

profiler = None

class NuxProfiler(SimpleItem, PropertyManager):
    "Nuxeo Profiler"

    title = id = "NuxProfiler"
    meta_type = "NuxProfiler"

    enabled = False

    security= ClassSecurityInfo()

    _properties = (
        {'id': 'enabled', 'type': 'boolean', 'mode': 'w'},
    )
    manage_options = PropertyManager.manage_options + SimpleItem.manage_options

    def manage_editProperties(self, REQUEST=None, **kw):
        "Edit properties"

        enabled_old = self.enabled
        res = PropertyManager.manage_editProperties(self, REQUEST, **kw)
        if not enabled_old and self.enabled:
           self.enableProfiler()
        elif enabled_old and not self.enabled:
           self.disableProfiler()
        return res

    def enableProfiler(self):
        global profiler
        profiler = hotshot.Profile(LOGFILE)

    def disableProfiler(self):
        global profiler
        profiler = None

InitializeClass(NuxProfiler)

def _profilePublishModule(module_name, stdin=sys.stdin, stdout=sys.stdout,
                          stderr=sys.stderr, environ=os.environ, debug=0,
                          request=None, response=None):

    if profiler:
        result = profiler.runcall(publish_module, module_name, stdin, stdout,
                                  stderr, environ, debug, request, response)
    else:
        result = publish_module(module_name, stdin, stdout,
                                stderr, environ, debug, request, response)

    return result

def _hookZServerPublisher():
    global publish_module
    import ZPublisher as module
    publish_module= patchModuleFunction(module, _profilePublishModule,
                                        funcName="publish_module")

