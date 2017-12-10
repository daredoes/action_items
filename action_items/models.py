from action_items import *

@Session.model_mixin
class User:
    actions = relationship('Action', backref='user')


class Action(MainModel):
    name = Column(UnicodeText)
    description = Column(UnicodeText)
    date_started = Column(Date, nullable=True)
    date_completed = Column(Date, nullable=True)
    priority = Column(Integer, default=0)
    state = Column(Choice(c.ACTION_OPTS), default=c.SHOULD_ACTION)
    user_id = Column(UUID, ForeignKey('user.id'))

    @presave_adjustment
    def _misc_adjustments(self):
        if self.state == c.HAVE_ACTION and self.orig_value_of('state') == c.AM_ACTION:
            self.date_completed = datetime.now(UTC)