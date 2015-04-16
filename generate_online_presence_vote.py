from __future__ import print_function, division

import argparse
import time
import yaml

description = """\
Turn a copy of teams.json from srweb into YAML suitable for SRAVES.
"""

parser = argparse.ArgumentParser(description=description)
parser.add_argument('teams_json', type=argparse.FileType('r'),
        help="The teams.json file to read from")
args = parser.parse_args()

teams = yaml.load(args.teams_json)

def team_to_candidate(tla, team):
    return { 'name': "{name} ({tla})".format(tla=tla, name=team['name']) }

candidates = [team_to_candidate(tla, team) for tla, team in teams.items()]

output = {
    'positions': [
        {
            'name': "Online Presence Award {}".format(time.localtime().tm_year),
            'desc': "Choose the team which you think has the best online presence:",
            'candidates': candidates,
        },
    ],
}

print(yaml.dump(output))
