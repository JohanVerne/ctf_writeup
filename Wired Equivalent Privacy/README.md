# Wired Equivalent Privacy

## Challenge

Find back the key used to secure the channel. This challenge comes from greHack CTF 2012.

## Solution

Testés : $ aircrack-ng -z ch10.cap

$ aircrack-ng -K -f 3 -b 00:0f:b5:56:e0:9e ch10.cap # en laissant tourner pendant ~ 2 heures

Encore une fois, brute force pas suffisant

## Flag
