#!/bin/sh

#
# Put this script in /kite/onboot
#

/etc/init.d/framework stop
/etc/init.d/powerd stop
/mnt/us/dashboard/display.sh
