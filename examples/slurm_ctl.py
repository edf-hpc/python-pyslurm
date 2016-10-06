#!/usr/bin/env python

from __future__ import print_function

import pyslurm
import sys

try:
    a = pyslurm.config()
    ctl_dict = a.get()
except ValueError as e:
    print("Error - {0}".format(e.args[0]))
    sys.exit(-1)

# Process the sorted Slurm configuration dictionary

date_fields = [ 'boot_time', 'last_update' ]
for key in sorted(ctl_dict.iterkeys()):

    if key in date_fields:

        if ctl_dict[key] == 0:
            print("\t{0:<35} : N/A".format(key))
        else:
            ddate = pyslurm.epoch2date(ctl_dict[key])
            print("\t{0:<35} : {1}".format(key, ddate))

    elif 'debug_flags' in key:
        print("\t{0:<35s} : {1}".format(key, pyslurm.get_debug_flags(ctl_dict[key])))
    else:
        if 'key_pairs' not in key:
            print("\t{0:<35} : {1}".format(key, ctl_dict[key]))

if ctl_dict.has_key('key_pairs'):

    print()
    print("Additional Information :")
    print("------------------------")
    print()

    for key in sorted(ctl_dict['key_pairs'].iterkeys()):
        print("\t{0:<35} : {1}".format(key, ctl_dict['key_pairs'][key]))
