#!/usr/bin/stunnel4
#setuid = stunnel4
#setgid = stunnel4
foreground = yes
pid = /home/dotcloud/stunnel/stunnel4.pid
[serverside]
accept=0.0.0.0:{server_local_port}
CAfile=/home/dotcloud/stunnel/cert.pem
cert=/home/dotcloud/stunnel/cert.pem
key=/home/dotcloud/stunnel/key.pem
client=no
verify=3
connect={server_connect}
; change the connect line to point to the local secured server
