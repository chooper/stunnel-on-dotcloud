#!/usr/bin/env python

"""Generate stunnel configs from templates"""

import os

def main(config_prefix, server_connect, server_local_port,
    client_connect, client_local_port):

    # Write clientside config
    with open('stunnel-clientside.tpl','r') as rf:  # TODO: path
        clientside_template = rf.read()
        clientside_cfg = clientside_template.format(**locals())
        config_file = config_prefix+'-client.stunnel'

        with open(config_file,'w+') as wf: # TODO: path
            wf.write(clientside_cfg)
        os.chmod(config_file, 0755)

    # Write serverside config
    with open('stunnel-serverside.tpl','r') as rf:  # TODO: path
        serverside_template = rf.read()
        serverside_cfg = serverside_template.format(**locals())
        config_file = config_prefix+'-server.stunnel'

        with open(config_file,'w+') as wf: # TODO: path
            wf.write(serverside_cfg)
        os.chmod(config_file, 0755)


if __name__ == '__main__':
    import sys

    def usage():
        print
        print ' '.join(['Usage: {0}', '<config_prefix>',
                '<server_connect>', '<server_local_port>',
                '<client_connect>', '<client_local_port>', ]) \
                .format(sys.argv[0])
        print

    if len(sys.argv) < 6:
        usage()
        sys.exit(1)

    config_prefix = sys.argv[1]
    server_connect = sys.argv[2]
    server_local_port = sys.argv[3]
    client_connect = sys.argv[4]
    client_local_port = sys.argv[5]

    main(config_prefix, server_connect, server_local_port,
        client_connect, client_local_port)

