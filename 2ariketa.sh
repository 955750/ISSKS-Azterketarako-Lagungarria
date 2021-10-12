####Irudien izenak izango dituen fitxategia sortu
ls /home/jfu/Descargas/2\ Laborategia\ -\ Zifraketa-20211003/irudia/ > irudiIzenak.txt

####Zenbat irudi dauden jakiteko (begiztak gehienez izango duen iterazio kopurua)
#WC: -l -> fitxategiko lerro kopurua;
#CUT: -d -> hitzak zeren arabera banatu; -f -> zenbatgarren eremua hartu behar den adierazteko
irudiKop=$(wc -l irudiIzenak.txt | cut -d " " -f 1)

####Mezua daukan irudiak hurrengo Hash (MD5) kodea du:
hash="e5ed313192776744b9b93b1320b5e268"

####Mezua zein irudik duen deskubritzeko begizta
#for (( i=1; i<=$irudiKop; i++ ))
unekoIrudiHash=""
#aurkitua=0
i=1
#while [ $aurkitua -ne 1 ] && [ $i -le $irudiKop ]
while [ $i -le $irudiKop ]
do
  unekoIrudia=$(awk "NR == $i" irudiIzenak.txt)
  unekoIrudiaHash=$(md5sum /home/jfu/Descargas/2\ Laborategia\ -\ Zifraketa-20211003/irudia/$unekoIrudia | cut -d " " -f 1)
  if [ $unekoIrudiaHash == $hash ]
  then
    echo $unekoIrudia
    echo $unekoIrudiaHash
  fi
  i=`expr $i + 1`
done

