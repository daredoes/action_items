from action_items import *


@all_renderable(c.TASKS)
class Root:
    def index(self, session, message=''):

        return {
            'message': message,
            'items': session.query(Action).all()
        }

    def should(self, session=None, message='', **params):
        item = session.action(params)
        items = session.query(Action).filter(Action.state == c.SHOULD_ACTION).all()
        if item.is_new:
            pass
        if 'name' in params:
            pass
        return {
            'message': message,
            'item': item,
            'items': items
        }

    def will(self, id=None, session=None, message='', **params):
        item = None
        items = session.query(Action).filter(Action.state == c.WILL_ACTION).all()
        if id:
            item = session.action(id)
        return {
            'message': message,
            'item': item,
            'items': items
        }

    def am(self, id=None, session=None, message='', **params):
        item = None
        items = session.query(Action).filter(Action.state == c.AM_ACTION).all()
        if id:
            item = session.action(params)
        return {
            'message': message,
            'item': item,
            'items': items
        }

    def have(self, id=None, session=None, message='', **params):
        item = None
        items = session.query(Action).filter(Action.state == c.HAVE_ACTION).all()
        if id:
            item = session.action(id)
        return {
            'message': message,
            'item': item,
            'items': items
        }



    @unrestricted
    def signup(self, session,  password='', message='', **params):
        user = session.user(params, checkgroups=User.all_checkgroups, bools=User.all_bools)
        if user.is_new:
            message = check(user)
            if not message and 'first_name' in params:
                session.add(user)
                session.commit()
                password = password if password else genpasswd()
                admin_params = {
                    'access': '{}'.format(c.TASKS),
                    'user_id': user.id,
                    'password': password
                }
                account = session.admin_account(admin_params, checkgroups=['access'])
                account.hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                message = check(account)
                if not message:
                    message = 'Account Created'
                    account.user = user
                    session.add(account)
                raise HTTPRedirect('index?message={}', message)
            return {
                'user': user
            }
        raise HTTPRedirect('index?message={}', message)
