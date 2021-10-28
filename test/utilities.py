from src.pdf.event import event


class TestEventListener(event.BaseEventListener):
    """event recorder & event history verifier"""

    def __init__(self):
        super().__init__()
        self.__eventhistory: list[event.PDFEvent] = []

    def update(self, event_: event.PDFEvent) -> None:
        self.__eventhistory.append(event_)

    @property
    def event_history(self) -> list[event.PDFEvent]:
        return self.__eventhistory

    def verify_history(self, eventlist: list[event.PDFEvent]):
        """verifies event history"""
        if len(self.__eventhistory) != len(eventlist):
            return False
        for (ev, e_ev) in zip(self.__eventhistory, eventlist):
            if type(ev) != type(e_ev) or ev.__dict__ != e_ev.__dict__:
                return False
        return True


def verify_error(error: Exception, v_error: Exception):
    """error verifier"""
    return isinstance(error, v_error.__class__)\
        and error.__dict__ == v_error.__dict__
