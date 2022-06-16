CURRENT_DATE=`date`

echo "Cleanup started at $CURRENT_DATESTAMP"

apt-get autoremove
apt-get clean

echo "Cleanup finished at $CURRENT_DATESTAMP"