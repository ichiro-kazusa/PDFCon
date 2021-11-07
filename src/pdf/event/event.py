from abc import ABC


class PDFEvent(ABC):
    pass


#################
# Event Objects
#################
class EventFileRead(PDFEvent):
    def __init__(self, path) -> None:
        self.path = path


class EventFileWrite(PDFEvent):
    def __init__(self, path) -> None:
        self.path = path


class EventConcatComplete(PDFEvent):
    pass


class EventDecryptComplete(PDFEvent):
    pass


class EventEncryptComplete(PDFEvent):
    pass


class EventExtractComplete(PDFEvent):
    pass


##################################################
# Observer Pattern for Event Subject/Listener
##################################################
class BaseEventListener(ABC):
    def __init__(self):
        get_event_subject().register(self)

    def update(self, event: PDFEvent):
        pass  # override to do something


class __EventSubject:
    """__EventSubject class must have SINGLE instance. """

    def __init__(self):
        self.listeners = []

    def register(self, listener):
        self.listeners.append(listener)

    def unregister(self, listener):
        self.listeners.remove(listener)

    def notify(self, event: PDFEvent):
        for listener in self.listeners:
            listener.update(event)


__EVENT_SUBJECT: __EventSubject = __EventSubject()  # this is the only instance


def get_event_subject() -> __EventSubject:
    """interface to get the single instance of EventSubject"""
    return __EVENT_SUBJECT
