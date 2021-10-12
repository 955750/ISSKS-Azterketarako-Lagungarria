#"Segurtasuna katalogoko babes-kopia inkrementala egiten du, egunero eguerdiok 12etan 
#(Karpeta bat egun bakoitzeko, cron erabiliz)

#mkdir /var/tmp/Backups/$(date '+%F')

rsync -av --link-dest=/var/tmp/Backups/$(date --date=yesterday "+%F") /home/jfu/Escritorio/ISSKS/\
Laborategiak/1_laborategia/Segurtasuna /var/tmp/Backups/$(date "+%F")
