#!/usr/bin/env python

from __future__ import with_statement

import os
import base64
from collections import defaultdict

import config

def load_votes(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.split()

def load_all_votes(root):
    votes = defaultdict(lambda: defaultdict(lambda: 0))
    for fn in os.listdir(root):
        fp = os.path.join(root, fn)
        for posid, cand in load_votes(fp):
            votes[posid][cand] += 1

    return votes

POSITIONS = config.load_positions()
all_votes = load_all_votes(config.VOTES_DIR)

for pos in POSITIONS:
    print "{0}:".format(pos['name'])
    posname = config.position_id(pos['name'])
    raw_votes = all_votes[base64.b64encode(posname)]
    votes = {}
    winners = set()
    max_votes = 0
    for cand_b64, count in raw_votes.iteritems():
        cand_name = base64.b64decode(cand_b64)

        if count > max_votes:
            winners = set([cand_name])
            max_votes = count
        elif count == max_votes:
            winners.add(cand_name)

        votes[cand_name] = count

    candidates = pos['candidates']
    candidates.append({ 'name': 'RON' })

    for cand in candidates:
        name = cand['name']
        count = votes.get(name, 0)
        if name in winners:
            extra = '*'
        else:
            extra = ''
        print " {0:>30}: {1:>2} {2}".format(name, count, extra)
