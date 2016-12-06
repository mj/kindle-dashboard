# Kindle Dashboard

I quickly hacked up The Kindle Dashboard to show information of everyday information on a wall-mounted Amazon Kindle device.

The information conists of

- current outside temperature (measured with digitemp)
- Times of sunrise and sunset (useful for planning outdoor sports)
- Current moon phase
- Estimated travel time to work

The system is open enough so that other types of information can be integrated as well. It is full of hardwired labels and makes assumption that will most likely not work for you immediately.

## Installation

### Server

TBD. You are pretty much on your own for now.

### Kindle

You'll need a jailbroken Kindle with [kite](http://www.mobileread.com/forums/showthread.php?t=168270) on it.

1. Add kite init script:

```sh
[root@kindle root]# ls -l /mnt/us/kite/onboot/
-rwxr-xr-x    1 root     root          130 Nov 20 06:01 init-dashboard.sh
[root@kindle root]#
```

2. Add reload cronjob

```sh
[root@kindle root]# mntroot rw
system: I mntroot:def:Making root filesystem writeable
[root@kindle root]# vi /etc/crontab/root
[...]
[root@kindle root]# /etc/init.d/cron restart
system: I cron:def:stopping crond
system: I cron:def:starting crond
[root@kindle root]# mntroot ro
system: I mntroot:def:Making root filesystem read-only
/dev/mmcblk0p1 on / type ext3 (ro,noatime,nodiratime)
[root@kindle root]# grep dashboard /etc/crontab/root
*/5 * * * *  /mnt/us/dashboard/display.sh
[root@kindle root]#
```

## CREDITS

This project is based on the excellent work by [Matthew Petroff](https://github.com/mpetroff/kindle-weather-display). It contains artwork from the [Moon Phases](https://thenounproject.com/MarkieAnn/collection/moon-phases/) collection by MarkieAnn Packer and the [Trash Icon](https://thenounproject.com/term/trash/70641/) by Pauel Tepikin.
