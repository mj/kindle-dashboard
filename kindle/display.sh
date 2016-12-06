#!/bin/sh

. kindle.conf

cd "$(dirname "$0")"

rm kindle-dashboard.png
eips -c
eips -c

if wget $DASHBOARD_URL; then
	eips -g kindle-dashboard.png
fi
