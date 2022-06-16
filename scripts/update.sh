CURRENT_DATE=`date`

echo "Update started at $CURRENT_DATESTAMP"

apt-get update -y
apt-get full-upgrade -y

echo "Update finished at $CURRENT_DATESTAMP"