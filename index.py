#!/usr/bin/env python

import cgi

import config

positions = config.load_positions()

print "Content-Type: text/html\n"

print """<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Student Robotics Awesome Voting and Election System</title>
    <style type="text/css">
        body {
            font-family: sans;
        }
        fieldset {
            margin-bottom: 10px;
        }
        legend {
            padding: 5px;
        }
        input {
            float: left;
            margin-right: 10px;
        }
        input[type="submit"] {
            width: 100%;
            margin: 10px auto;
            font-size: 4em;
            height: 2em;
        }
        .ron {
            color: orange;
        }
        .abs {
            color: blue;
        }
    </style>
</head>
<body>
<h1>sRAVEs (Student Robotics Awesome Voting and Election System)</h1>
<p>Please vote for every position. You can opt for nominations to be re-opened or abstain from a vote.</p>
<form method="POST" action="vote.py">"""

for pos in positions:
    posname = config.position_id(pos["name"])
    print """<fieldset><legend>%s</legend>
        <p>%s</p>""" % (cgi.escape(pos["name"]), pos["desc"])

    if "candidates" in pos:
        for person in pos["candidates"]:
            candid = config.position_id(person["name"])
            id = "%s_%s" % (pos["name"], person["name"])
            print """        <input required type="radio" name="vote_%(posname)s" id="%(posname)s_%(candid)s" value="%(candname)s" />
                <p><label for="%(posname)s_%(candid)s">%(candname)s</label> """ % \
                {"posname": posname, "candid": candid, "candname": person["name"]}

            if "url" in person:
                print """<a href="%s">About</a>""" % person["url"]

            print "</p>"


    print """        <input required type="radio" name="vote_%(posname)s" id="%(posname)s_ron" value="RON" />
                <p><label class="ron" for="%(posname)s_ron">RON (Re-open Nominations)</label></p>"""  % {"posname": posname}

#    print """               <input required type="radio" name="vote_%(posname)s" id="%(posname)s_abstain" value="Abstain" />
#                <p><label class="abs" for="%(posname)s_abstain">Abstain</label></p>""" % {"posname": posname}

    print """</fieldset>"""

print """<input type="submit" value="Vote!"/>
</form>
</body>
</html>"""
