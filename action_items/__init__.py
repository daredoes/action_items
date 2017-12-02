from darecms.common import *

from ._version import __version__
from .config import *
from .models import *
from .model_checks import *

static_overrides(join(config['module_root'], 'static'))
template_overrides(join(config['module_root'], 'templates'))
mount_site_sections(config['module_root'])

admin_menu = MenuItem(name='Action Items', access=[c.TASKS], submenu=[
    MenuItem(name='All',  href='{{ c.PATH }}/task', priority=1),
    MenuItem(name='Should',  href='{{ c.PATH }}/task/should', priority=2),
    MenuItem(name='Will',  href='{{ c.PATH }}/task/will', priority=3),
    MenuItem(name='Am',  href='{{ c.PATH }}/task/am', priority=4),
    MenuItem(name='Have',  href='{{ c.PATH }}/task/have', priority=5),

])

c.MENU.append_menu_item(admin_menu)
c.MENU.append_menu_item(MenuItem(name="New Task", access=[c.TASKS], href="{{ c.PATH }}/task/new"))