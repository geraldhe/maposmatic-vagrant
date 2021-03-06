#----------------------------------------------------
#
# German CartoOsm style sheet - the current openstreetmap.de style
#
#----------------------------------------------------

cd /home/maposmatic/styles

git clone https://github.com/geraldhe/openstreetmap-carto-de.git /home/maposmatic/styles/openstreetmap-carto-de-rk

cd openstreetmap-carto-de-rk

sed -i -e's/dbname: "osm"/dbname: "gis"/' project.mml
sed -i -e's/carto /carto -q /g' Makefile
make

for a in *.xml
do
    php /vagrant/files/postprocess-style.php $a
done

ln -s /home/maposmatic/shapefiles data

cat <<EOF >> /home/maposmatic/ocitysmap/ocitysmap.styledefs
[german_carto_rk]
name: GermanCartoOSMRK
group: Countries
description: German CartoCSS OSM style (RK edition)
path: /home/maposmatic/styles/openstreetmap-carto-de-rk/osm-de.xml
annotation: German OSM style (customized for red cross)
url: http://www.osm-baustelle.de/dokuwiki/doku.php?id=style:german

EOF

echo "  german_carto_rk," >> /home/maposmatic/ocitysmap/ocitysmap.styles


