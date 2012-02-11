stunnel recipe for dotCloud custom services
===========================================

As the title states, this is a recipe for adding SSL tunnels between your dotCloud services.
It uses the Ubuntu "stunnel4" package and automates the tunnel configuration as well as the
key download. Out of the box, this package sets up two services. One is the server, which
is a very simple use of "netcat" that will execute and output the "id" command upon the first
connection. The second is a client which will connect to the netcat "server" over SSL.

In order to use it, use this package as the base of your custom services. If you have existing
packages already, or are trying to use a different base, you will need to merge the
systempackages, ports, and processes sections of the dotcloud.yml

Additionally, you will need to append the contents of the provided builder script with your own,
as well as the postinstall. When editing the postinstall script, please take note of the following
usage:

./gen-stunnel-cfgs.py <server_connect> <server_local_port> <client_connect> <client_local_port>

Please edit the builder script accordingly, paying particular attention to client_local_port.

Finally, you will need to put your keys in Amazon S3 and set some dotCloud environment variables
so we can deploy your keys automatically. Please take care to configure a private ACL on these
keys. Additionally, we highly recommend you use Amazon IAM to give this script its own API keys.
In order to configure these containers to use these settings, you will need to run the following
command:

dotcloud var set stunnel STUNNEL_S3_ACCESSKEY=<your aws access key> \
    STUNNEL_S3_SECRETKEY=<your aws secret key> \
    STUNNEL_S3_PRIVKEYPATH=<the path on s3 to your private key> \
    STUNNEL_S3_PUBKEYPATH=<the path on s3 to your public key>

For the S3 paths mentioned above, these are typically in the form of s3://bucketname/path/to/key.pem.

