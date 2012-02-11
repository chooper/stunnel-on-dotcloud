#!/usr/bin/stunnel4
#setuid = stunnel4
#setgid = stunnel4
foreground = yes
pid = /home/dotcloud/stunnel/stunnel4.pid
[clientside]
accept=127.0.0.1:10000
CAfile=/home/dotcloud/stunnel/cert.pem
cert=/home/dotcloud/stunnel/cert.pem
key=/home/dotcloud/stunnel/key.pem
client=yes
verify=3
connect={client_connect}
; change the connect line to point to the remote server
