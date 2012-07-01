#!/usr/bin/env python

from __future__ import with_statement

import os
import base64

import config

positions = config.load_positions()

def load_votes(filePath):
    with open(filePath) as f:
        for line in f.readlines():
            yield line.split()

def load_all_votes(root):
    votes = {}
    for fn in os.listdir(root):
        fp = os.path.join(root, fn)
        for posid, cand in load_votes(fp):
            if not posid in votes:
                votes[posid] = {}
            if not cand in votes[posid]:
                votes[posid][cand] = 0

            votes[posid][cand] += 1

    return votes

all_votes = load_all_votes(config.VOTES_DIR)

for pos in positions:
    print "%s:" % pos['name']
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
    candidates.append(dict(name='RON'))

    for cand in candidates:
        name = cand['name']
        count = votes.get(name, 0)
        if name in winners:
            extra = '*'
        else:
            extra = ''
        print " %s: %s %s" % (name.rjust(15), str(count).rjust(2), extra)
