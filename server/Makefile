all: render png

render:
	./render-dashboard.py

png: output.svg
	rsvg-convert --background-color=white -o output.png output.svg
	pngcrush -q -c 0 -ow output.png

install: output.png
	cp output.png /srv/www/sites/intranet/web/kindle-dashboard.png

uninstall:
	rm -r /srv/www/sites/intranet/web/kindle-dashboard.png

clean:
	rm output.svg output.png
