from action_items import *

class Action(MainModel):
    name = Column(UnicodeText)
    description = Column(UnicodeText)
    date_started = Column(UTCDateTime, nullable=True)
    date_completed = Column(UTCDateTime, nullable=True)
    state = Column(Choice(c.ACTION_OPTS), default=c.SHOULD_ACTION)

    @presave_adjustment
    def _misc_adjustments(self):
        if self.state == c.HAVE_ACTION and self.orig_value_of('state') == c.AM_ACTION:
            self.date_completed = datetime.now(UTC)
