#!/bin/usr/env python
#-*- coding:UTF-8 -*-

from bottle import route,run, view, error, static_file, debug, url, redirect, request, response
from wikifetch import init_db,load_session,Wikilink
import bottle

debug(True)

init_db()
session = load_session()


@route()
def defualt():
    redirect("/monitor")

@route(["/monitor","/index","/"])
@view("monitor")
def monitor():
    title = unicode(request.query.title) or '%'
    page = request.query.page or 0
    page = int(page)
    try:
        all = session.query(Wikilink).filter(Wikilink.title.like('%'+ title +'%')).count()
        monitor = session.query(Wikilink).order_by('id').filter(Wikilink.title.like('%'+ title +'%')).filter(Wikilink.id>(page*20)).limit(20).all()
    except StatementError:
        session.rollback()
        session.begin()
        
    #print monitor
    return dict(monitor=monitor,pages=(all/20),number=all)

@route("/why")
@view("why")
def why():
    return dict()

@route("/about")
@view("about")
def about():
    return dict()

@route("/learned")
@view("learned")
def learned():
    return dict()


@route ("/static/<filepath:path>", name="static")
def static(filepath):
    #print 'yey', filepath
    return static_file(filepath,root = "./static/")
    
    
@error(404)
def error404(error):
    return static_file('404.html',root="./static")


bottle.run (host='localhost',port =8080)
#bottle.run (host = '127.0.0.1',server='paste', port = 48035)
