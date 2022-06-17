apt-get update -y
apt-get upgrade -y

# Python 3.9.13
wget https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tgz
tar -zxvf Python-3.9.13.tgz
cd Python-3.9.13
./configure --enable-optimizations
sudo make altinstall

# Enable support for exFAT filesystems for the HDD
apt-get install exfat-fuse
apt-get install exfat-utils
mkdir /mnt/

# Docker installation for linux
curl -fsSL https://get.docker.com -o get-docker.s
sh get-docker.sh