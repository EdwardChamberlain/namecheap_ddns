# Namecheap DDNS
[Docker Hub Page](https://hub.docker.com/repository/docker/edchamberlain/namecheap_ddns/general)

~~This container is available on unRAID community Applications~~ Not yet!

This simple docker will automatically update a namecheap dynamic dns domain through GET requests. You MUST provide the required enviroment variables: APP_HOST, APP_DOMAIN, and APP_PASSWORD. You MUST create an 'A + Dynamic DNS' record for the host which you wish to update and enable Dynamic DNS in the manage page of your domain. Your APP_PASSWORD must be your Dynamic DNS password from namecheap and NOT your Namecheap password.

For more info see the [Namecheap help page](https://www.namecheap.com/support/knowledgebase/article.aspx/29/11/how-do-i-use-a-browser-to-dynamically-update-the-hosts-ip/).

Usage:
```
docker run \
-e APP_HOST='your host' \
-e APP_DOMAIN='your domain' \
-e APP_PASSWORD='your ddns password' \
edchamberlain/namecheap_ddns:latest
```
