#!/usr/bin/env python

"""Generate stunnel configs from templates"""

import os, json

def main():
    # Load dotCloud environment
    env = {}
    home_path = os.environ.get('HOME', '/home/dotcloud')
    with open(os.path.join(home_path,'environment.json'),'r') as rf:
        env = json.loads(rf.read())

    # Write s3cmd config
    with open('s3cmd.tpl','r') as rf:  # TODO: path
        s3cmd_template = rf.read()
        s3cmd_cfg = s3cmd_template.format(**env)
        with open('s3cmd.cfg','w+') as wf: # TODO: path
            wf.write(s3cmd_cfg)
        os.chmod('s3cmd.cfg', 0600)


if __name__ == '__main__':
    main()

