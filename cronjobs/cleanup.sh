CURRENT_DATE=`date`

echo "Cleanup started at $CURRENT_DATESTAMP"

apt autoremove
apt clean

echo "Cleanup finished at $CURRENT_DATESTAMP"