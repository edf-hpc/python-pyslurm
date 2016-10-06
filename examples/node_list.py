#!/usr/bin/env python

from __future__ import print_function

def display(node_dict):

    if node_dict:

        date_fields = [ 'boot_time', 'slurmd_start_time', 'last_update', 'reason_time' ]

        print('{0:*^80}'.format(''))
        for key, value in node_dict.iteritems():

            print("{0} :".format(key))
            for part_key in sorted(value.iterkeys()):

                if part_key in date_fields:
                    ddate = value[part_key]
                    if ddate == 0:
                        print("\t{0:<17} : N/A".format(part_key))
                    else:
                        ddate = pyslurm.epoch2date(ddate)
                        print("\t{0:<17} : {1}".format(part_key, ddate))
                elif ('reason_uid' in part_key and value['reason'] is None):
                    print("\t{0:<17} : ".format(part_key))
                else:
                    print("\t{0:<17} : {1}".format(part_key, value[part_key]))

            print('{0:*^80}'.format(''))

if __name__ == "__main__":

    import pyslurm

    try:
        Nodes = pyslurm.node()
        node_dict = Nodes.get()

        if len(node_dict) > 0:

            display(node_dict)

            print()
            print("Node IDs - {0}".format(Nodes.ids()))

        else:
            print("No Nodes found !")

    except ValueError as e:
        print("Error - {0}".format(e.args[0]))
