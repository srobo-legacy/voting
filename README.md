# sRAVEs

Student Robotics Awesome Voting and Election System is a simple web site
which enables voting for simple matters within Student Robotics.

## Setup

Positions and candidates can be set in the `config.yaml` file, other
customisations can be ffected by modifying the `config.py` file.

Votes are stored in files created (and thus owned) by the web server,
so a directory which it (and ideally only it) can read & write to must
be created for storing these.

Note that there is no automatic handling of old results, so to preserve
these you must first move the old directory out of the way.
