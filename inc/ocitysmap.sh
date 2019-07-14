#----------------------------------------------------
#
# Fetch OCitysMap from GitHub and configure it
#
#----------------------------------------------------

# install latest ocitysmap from git
cd /home/maposmatic
git clone -q https://github.com/geraldhe/ocitysmap.git
cd ocitysmap
./i18n.py --compile-mo
cd ..

