from darecms.common import *

from ._version import __version__
from .config import *
from .models import *
from .model_checks import *

static_overrides(join(config['module_root'], 'static'))
template_overrides(join(config['module_root'], 'templates'))
mount_site_sections(config['module_root'])

admin_menu = MenuItem(name='Action Items', access=[c.TASKS], submenu=[
    MenuItem(name='Tasks',  href='{{ c.PATH }}/tasks'),

])

c.MENU.append_menu_item(admin_menu)
