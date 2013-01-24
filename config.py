
from __future__ import with_statement

import re
import yaml

__all__ = [ 'VOTES_DIR', 'load', 'load_positions', "position_id" ]

VOTES_DIR = "/home/rbot/public_html/voting/votes"

_YAML_FILE = "config.yaml"

def load():
    with open(_YAML_FILE, 'r') as f:
        return yaml.load( f )

def load_positions():
    return load()['positions']

def position_id(full_name):
    """
    Generates an html compatible id for the given position.
    """
    posname = re.sub(r'\W+', '', full_name).lower()
    return posname
