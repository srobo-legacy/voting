#!/usr/bin/python

import cgi
import cgitb
import re
import os
import base64
import yaml

cgitb.enable()
VOTES_DIR = "/home/rbot/public_html/voting/votes"

pos_yaml = yaml.load( open("config.yaml", "r") )["positions"]
positions = {}
for position in pos_yaml:
    posname = re.sub(r'\W+', '', (position["name"])).lower()
    positions[posname] = position["name"]

class VotingException(Exception):
    pass

print "Content-type: text/html"
print
print """<!DOCTYPE html>
<html><head><title>sRAVEs -- Voting Complete</title>
<script src="jquery-1.5.2.min.js"></script>
<script src="jquery.easing.1.3.js"></script>
<script src="jeremy.js"></script>
<style>
body {
	background-color: #DE6400;
	font-family: sans;
	font-size: 150%;
	color: white;
	margin-right: 450px;
}
p {
	z-index: -1;
}

#jeremy {
	z-index: -2;
}

</style>
</head><body>"""

form = cgi.FieldStorage()

try:
    votes = {}
    # Discover the user:
    username = os.environ["REMOTE_USER"]
    # Load their file
    os.umask( 0077 )
    fname = os.path.join( VOTES_DIR, username )
    user_f = open( fname, "w" )

    r = re.compile( "^vote_([a-zA-Z0-9]+)$" )

    for k in form.keys():
        v = form[k]
        if isinstance(v, list):
            raise VotingException, "%s variable was specified twice" % (k)
        v = v.value

        m = r.match(k)
        if m != None:
            role = m.groups()[0]
            print >>user_f, "%s %s" % (base64.b64encode(role), base64.b64encode(v))
            votes[role] = v

except Exception as e:
    print "<p><b>Error</b>: %s.</p><p>Sorry, your vote has not been counted.  Please contact an admin.</p>" % e
else:
    print """<p>
<strong>Thanks.  Your vote has been registered.</strong>
</p>
<p>
Please check your votes are correct:
<ul>
"""
for role, person in votes.iteritems():
    if role in positions:
        print """<li>%s: <strong>%s</strong></li>""" % (positions[role], person)
    else:
        print """<li>Warning: Invalid role specified in input.</li>"""

if len(votes) == 0:
    print "<li>No votes!</li>"

print """</ul>
</p>
<p>
If you wish to change your vote before voting closes, just fill out the form again
and your vote will be superseded by the new vote.
</p>
<div id="jeremy" style="overflow:hidden;width:100%;height:0px;position:absolute;bottom:0;left:0;">
<img src="jeremy.png" style="float:right;"/>
</div>
"""

print """</body></html>"""

