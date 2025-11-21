# Employés malveillants d’une entreprise

## Challenge

Vous travaillez dans le SI d’une entreprise. Apparament, deux employés échangent des flags. On a pu capturer une partie de leur trafic réseau (capture exercice2.pcap). Cette capture contient plusieurs flags, trouvez-en au moins 2.

## Solution

J'ai commencé à filtrer par communication http avec wireshark pour obtenir des infos rapidement.
Aux paquets 57675 et 57686, on peut voir une requete/réponse d'image PNG. En faisant file-->export Object-->http, on peut obtenir l'image transférée (https://osqa-ask.wireshark.org/questions/35123/fastest-way-to-display-a-png-file/)
![flag image](images/something.png)

Au paquet 57065, on a une clé privée :
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDOa3TY8p0PxshW
6PdNBWad17k+4nlZ8CcaNZSs3quXOeiWUSi34AEO9RufAXiSfMn7aSRd4Q0eNv17
NfyuaYlZIEcoThPCL+kfhB3cdnGjs+aSZb2pwVhwBkftC/BPqYOeepguAO8a5roS
RuTdUyGO+g+exGkjTc8rDY5aODB0Uo2d9CoRoz/gEk+oqQc9nQCxB3dEHtadVhhz
E8PMePeUtvaBG2mXwJ5psHuPY4JwSCGXFuqf1CX3is+z/stfaMHtaghCYkPfprRm
yF/3fm8nEz3LdSuNf2zPnZMR1W5hvLPaI7ttsoOq4Gv3sVe9NxPan/4K18Gvbf2y
MqKQvE0bAgMBAAECggEAGm6YH8+xXPvPW5GpWSt/4GZnSi4l6+Zcm3aQ+zHoNw0r
Q1RRKnp8qDWqu8msbtWb552nEn5m95+DBev71zmcZNVFR1v4G72W1HpOeJSSKKw4
sjZk+v/PG0kynKASvaCvQfPg2MM12vQAj6aUV+L1QSG0LlhoPiUQiirKN7NKQRq2
MFGeXiRca5TpLGmGn0JJ55xZox8YgJ2Q3RTuyK4bItjkNicy6/bIwSCmhdttT2ND
uKCLM/zbE6Hbjwbo38Va7gviH+5btDwaj/POK2fY6+5Yhf/J3t9OCEWvHHAiQQnm
6VbNudJZi1jV/8aAX7u4AhguWb8FRxl1HfegwwmKAQKBgQDtgiqKmSNACZ0U/eTz
eoJd+qzb1gzI2Nmzid5jTNq8st8YECq+xjKquZkxJv1MHHBZvPz3J0dTYOWmiL80
/FbnD1f5GBJJYfssFGsH1FVmVgH5IN3URDReQny1fydQdmGBewPT+kTUeDhKzzMk
4yBspDaqSrK6c9IEtE/IJWNLuwKBgQDefad/Q7QlbAPZQQNvf3oFP1CQOFvjUCMH
my6rfgEx0tV1C1CK/yNn2sFmB7L9IsXe6s9mw7aVEzM3yNL95qmRECKmHGMlm3Lz
k5LYxYI4xxWGbNbLvDN6rL2PK7espevqR8QsQGvflqQvDMdoG13r2uPSl/U5zo+k
U6TnwqT+IQKBgBpoicBlbKT3LK8j1+w2p/45HDVJZJyEeBhdcQvLhNrMbL/pNEeI
FCQlhOIROsLWuqtPtzTn+idMM9zDgbcrg6Inc5mv0oC0U1BAaPIy6tf5IjkILYIn
n0cHz4QCwmVQ9GCIRBGy1ypkv6WZyk8ErhtGWwmuSpcuv6BkSCax+Yt3AoGAUXzO
EwN2AFq+UhzIqFaVF0ToOdoadXfNTKTeg/rjbx8cBQE+35mwmwH44Wiieqn4tLtl
eOrnfVQJ5z2LYWjQ5At31UUCXyy+/k0ndHNqTWdFD/Xe+cGVTTHlP4GwhPBEJotg
YyC5IavnuD/C7PNRA+goluIG88Qewf3MoQGeMmECgYAt0cNqtXdDPsw6U9Oc+PYb
hc9QS9jJhYJhE5aykZlPM4efPZXCtCRra5N0HKVnuf8qxq1n1nszw9ct06p7hwVM
W/Z+1AS4/+9m9wVEqAwC+coWPFk1I9no/aB3+PHT2/XTRtO9bCZpMDorrPV2BHnz
jqHQqkkIudjiZb3loDeBcg==
-----END PRIVATE KEY-----

Mais on n'a pas grand chose d'autre pour l'utiliser

## Flags

dc3c3497d445ff873ae51fc550f5b0b5
