# Namecheap DDNS
[Docker Hub Page](https://hub.docker.com/repository/docker/edchamberlain/namecheap_ddns/general)

This container is available on unRAID community Applications

This simple container will automatically update a namecheap dynamic dns domain through GET requests. This container checks your public IP every 3 seconds and sends an update if a change is detected. 

You MUST provide the required enviroment variables: `APP_HOST`, `APP_DOMAIN`, and `APP_PASSWORD`. You MUST create an 'A + Dynamic DNS' record for the host which you wish to update and enable Dynamic DNS in the manage page of your domain. Your APP_PASSWORD must be your Dynamic DNS password from namecheap and NOT your Namecheap password.

For more info see the [Namecheap help page](https://www.namecheap.com/support/knowledgebase/article.aspx/29/11/how-do-i-use-a-browser-to-dynamically-update-the-hosts-ip/).

Usage:
```
docker run \
-e APP_HOST='your host' \
-e APP_DOMAIN='your domain' \
-e APP_PASSWORD='your ddns password' \
edchamberlain/namecheap_ddns:latest
```

Usage (optional args):
```
docker run \
-e APP_HOST='your host' \
-e APP_DOMAIN='your domain' \
-e APP_PASSWORD='your ddns password' \
-e APP_UPDATE_TIME='time between updates, e.g: '60'' \
-e APP_LOG_LEVEL='Log Level'
edchamberlain/namecheap_ddns:latest
```

To pass multiple domains, hosts, or passwords you can use a semi-colon seperated list. For example to update `host1` and `host2` of `myDomain` you would need to pass:

```
...
-e APP_HOST='host1;host2' \
-e APP_DOMAIN='myDomain;myDomain' \
-e APP_PASSWORD='myPassword;myPassword' \
...
```

**Note:** the repetition of both `myDomain` and `myPassword`. You __must__ include the same number of each parameter - repetition is allowed.

