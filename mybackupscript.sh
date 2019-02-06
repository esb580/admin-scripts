#!/bin/bash
#Backs Up Laptop User Profile to Linux over SSH using rsync
#Uses cygwin installation laptop to get ssh and rsync from Windows
echo "---------Starting Backup of `hostname`----------"
cd /cygdrive/c/users
rsync -avzh -P --delete --stats --timeout=120 --exclude=ntuser* --exclude=NTUSER* --exclude=AppData "./Frank Jackson" han@10.0.0.246:/home/han/backups/laptop
echo "---------Backup of `hostname` Complete---------"
