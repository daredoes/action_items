from action_items import *

config = parse_config(__file__)
c.include_plugin_config(config)

c.ACCESS.update(c.ACTION_ACCESS_LEVELS)
c.ACCESS_OPTS.extend(c.ACTION_ACCESS_LEVEL_OPTS)
c.ACCESS_VARS.extend(c.ACTION_ACCESS_LEVEL_VARS)
