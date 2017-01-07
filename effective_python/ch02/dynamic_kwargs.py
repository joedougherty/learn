"""

Be careful when using optional keyword args that can
take dynamic values.

"""

import datetime

def note_event(evt, severity, timestamp=datetime.datetime.now()):
    return 'Event [{}] of severity level [{}] occurred at [{}].'.format(evt, severity, timestamp)

"""

The timestamp argument is calculated once at the time the
function definition is processed.

If you want timestamp to be computed at call time, 
do this...

"""

def note_event(evt, severity, timestamp=None):
    """
    Notes the occurrence of an event.

    Args:
        evt [str]: Name of the event
        severity [str]: Severity of the event. Can be one of ('SEVERE', 'NO WORRIES')
        timestamp [datetime obj]: When it occurred. Will default to datetime.datetime.now()
    """
    if not timestamp:
        timestamp = datetime.datetime.now()

    return 'Event [{}] of severity level [{}] occurred at [{}].'.format(evt, severity, timestamp)

