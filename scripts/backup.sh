#!/bin/bash
mount /dev/sda1 /mnt

dd if=/dev/mmcblk0 bs=1M status=progress of=/mnt/raspberrypi/"$(date +%Y%m%d\_%H%M%S)"\_pi_clone.img
find /media/pi/Cortana/raspberry/ -mtime +3 -exec rm -f {} \;

umount /dev/sda1 /mnt
