# Update rpi and install requirements for project

apt-get update -y
apt-get upgrade -y
sudo apt-get install -y git openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev

# Enable support for exFAT filesystems for the HDD
apt-get install exfat-fuse
apt-get install exfat-utils
mkdir /mnt/

# Docker installation for linux
curl -fsSL https://get.docker.com -o get-docker.s
sh get-docker.sh
