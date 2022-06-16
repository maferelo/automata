CURRENT_DATE=`date`

echo "Update started at $CURRENT_DATESTAMP"

apt update
apt full-upgrade

echo "Update finished at $CURRENT_DATESTAMP"