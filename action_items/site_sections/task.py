from action_items import *


@all_renderable(c.TASKS)
class Root:
    def index(self, session, message=''):

        return {
            'message': message,
            'items': session.query(Action).filter(Action.user_id == c.CURRENT_ADMIN['id']).all()
        }

    def new(self, session, message='', new_entry=None, **params):
        item = session.action(params)

        if 'name' in params:
            session.add(item)
            session.commit()
        items = session.query(Action).all()
        return {
            'message': message,
            'item': item,
            'new_entry': new_entry,
            'items': items
        }

    @ajax_gettable
    def get_task_modal(self, session, **params):
        code = ''
        status = False
        message = 'ID not found'
        item = session.action(params)
        if item:
            message = ''
            status = True
            code = render('/partials/task_modal.html', {'item': item}).decode('utf-8')
        return {
            'status': status,
            'code': code,
            'message': message
        }

    @ajax
    def update_task(self, session, **params):
        status = False
        message = 'Task Not Found.'
        task = session.action(params)
        if 'name' in params:
            session.add(task)
            session.commit()
            message = 'Task updated.'
            status = True
        return {
            'status': status,
            'message': message
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
