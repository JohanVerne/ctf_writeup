# CISCO - mot de passe

## Challenge

Find the "Enable" password.

## Solution

On extrait le mot de passe encrypté avec un algorithme MD5 : $1$p8Y6$MCdRLBzuGlfOs9S.hXOp0
Sur Kali, on utilise John pour le décrypter avec la commande $john --format=md5crypt passwd.txt

## Flag
