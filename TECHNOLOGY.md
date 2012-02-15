'all wikipedia people' - the technology
--------------------------------------

based on [bottle.py][d1] microwebframework.
[d1]:http://bottlepy.org/docs
the DB is handled with magical [sqlalchemy][d2]
[d2]:http://www.sqlalchemy.org/
Rapid web page authoring based on [Html5Boilerplate 3.0][d3] and [Initializr][d4] responsive version of it.
[d3]:http://html5boilerplate.com/
[d4]:http://www.initializr.com/

the scraping of wikipedia api is handled by wikifetch.py while the main app is wikifetch.
the templates - using simpletemplate engine are in /views directory.
and all the static content in (as you can guess) in /static directory.
running with a PASTER httpserver