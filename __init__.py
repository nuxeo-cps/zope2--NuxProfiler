from NuxProfiler import NuxProfiler, _hookZServerPublisher

_hookZServerPublisher()

def initialize(context):
    control_panel = context._ProductContext__app.Control_Panel
    np = getattr(control_panel, "NuxProfiler", None)
    if np is None:
        np = NuxProfiler()
        control_panel._setObject("NuxProfiler", np)

