'all wikipedia people' - the technology
--------------------------------------

based on [bottle.py][d1] microwebframework.
[d1]:http://bottlepy.org/docs
the DB is handled with magical [sqlalchemy][d2]
[d2]:http://www.sqlalchemy.org/
Rapid web page authoring based on [Html5Boilerplate 3.0][d3] and [Initializr][d4] responsive version of it.
[d3]:http://html5boilerplate.com/
[d4]:http://www.initializr.com/
the http is handled beautifuly with [requests][d5]
[d5]:http://docs.python-requests.org/en/latest/index.html

the scraping of wikipedia api is handled by wikifetch.py while the main app is wikifetch.
the templates - using simpletemplate engine are in /views directory.
and all the static content in (as you can guess) in /static directory.
running with a [PASTER][d6] httpserver
[d6]:http://pythonpaste.org/

everything can be simpy installed by running:
pip install -r require.txt

python 2.6 is needed for requests
