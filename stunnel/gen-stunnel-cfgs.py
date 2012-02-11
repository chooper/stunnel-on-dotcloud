#!/usr/bin/env python

"""Generate stunnel configs from templates"""

import os

def main(server_connect, server_local_port, client_connect):
    # Write clientside config
    with open('stunnel-clientside.tpl','r') as rf:  # TODO: path
        clientside_template = rf.read()
        clientside_cfg = clientside_template.format(**locals())
        with open('stunnel-clientside','w+') as wf: # TODO: path
            wf.write(clientside_cfg)
        os.chmod('stunnel-clientside', 0755)

    # Write serverside config
    with open('stunnel-serverside.tpl','r') as rf:  # TODO: path
        serverside_template = rf.read()
        serverside_cfg = serverside_template.format(**locals())
        with open('stunnel-serverside','w+') as wf: # TODO: path
            wf.write(serverside_cfg)
        os.chmod('stunnel-serverside', 0755)


if __name__ == '__main__':
    import sys

    def usage(exit=True, exit_status=1):
        print
        print 'Usage: {0} <server_connect> <server_local_port> <client_connect>' \
            .format(sys.argv[0])
        print

        if exit:
            sys.exit(exit_status)

    if len(sys.argv) < 4:
        usage()

    server_connect = sys.argv[1]
    server_local_port = sys.argv[2]
    client_connect = sys.argv[3]

    main(server_connect, server_local_port, client_connect)

