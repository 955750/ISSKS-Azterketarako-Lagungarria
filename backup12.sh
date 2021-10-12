#Atzoko data

urteaAtzo=$(date -d yesterday +%Y)
hilaAtzo=$(date -d yesterday +%m)
egunaAtzo=$(date -d yesterday +%d)

#Gaurko data

urteaGaur=$(date +%Y)
hilaGaur=$(date +%m)
egunaGaur=$(date +%d)
atzo=${urteaAtzo}-${hilaAtzo}-${egunaAtzo}
gaur=${urteaGaur}-${hilaGaur}-${egunaGaur}


rsync -av --link-dest=/var/tmp/Backups/$atzo /home/jfu/Escritorio/ISSKS/Laborategiak/1_laborategia/\
Segurtasuna /var/tmp/Backups/$gaur



