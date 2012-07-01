
from __future__ import with_statement

import yaml

__all__ = [ 'VOTES_DIR', 'load', 'load_positions' ]

VOTES_DIR = "/home/rbot/public_html/voting/votes"

_YAML_FILE = "config.yaml"

def load():
	with open(_YAML_FILE, 'r') as f:
		return yaml.load( f )

def load_positions():
	return load()['positions']
