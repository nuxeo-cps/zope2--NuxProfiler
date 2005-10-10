NuxProfiler
===========

NuxProfiler is a simple profiler using the python hotshot profiler

It will create an object called "NuxProfiler" in the control panel.

When the profiler is enabled (from the object properties tab), it will log
profile data to a file called "hotshot.data". These data can then be analysed
using the standard librairy (hotshot.stats module) or using hotshot2cachegrind
or hotshot2calltree to use the insanely great kcachegrind interactive graphical
visualisation tool.

Credits
-------

Main developer: S. Fermigier

Based on code borrowed from Dieter Maurer's ZopeProfiler

