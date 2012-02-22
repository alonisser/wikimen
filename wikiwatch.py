#!/bin/usr/env python
#-*- coding:UTF-8 -*-

from bottle import route,run, view, error, static_file, debug, url, redirect, request, response
from wikifetch import init_db,load_session,Wikilink, statistic
import bottle
from sqlalchemy.exc import StatementError
from config import production_port, production_server
import json
debug(True)

init_db()
session = load_session()
stats = statistic()

@route()
def defualt():
    redirect("/monitor")

@route(["/monitor","/index","/"])
@view("monitor")
def monitor():
    title = request.query.title
    page = request.query.page or 0
    page = int(page)
    try:
        total = stats[0]
        all = session.query(Wikilink).filter(Wikilink.title.like('%'+ title +'%')).count()
        monitor = session.query(Wikilink).order_by('title').filter(Wikilink.title.like('%'+ title +'%')).offset(page*20).limit(20).all() #filter(Wikilink.id>(page*20))
        #print "page=",page," title=",title,
    except StatementError:
        session.rollback()
        #session.begin()
        
    #print monitor
    return dict(monitor=monitor,pages=(all/20),number=all,total = total)

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
    
@route("/api")
def api():
    off = request.query.off or 0
    lim = request.query.lim or False
    '''very basic json that throws all the data..not fully developed yet
    maybe some kind of predicate..'''
    if lim:
        monitor = session.query(Wikilink).order_by(Wikilink.title).offset(off).limit(lim).all()
    else:
        monitor = session.query(Wikilink).order_by(Wikilink.title).offset(off).all()
    jsonstr = []    
    for i in monitor:
        jsonstr.append(i.to_dict())
    return json.dumps(jsonstr)
    

@route("/stats")
@view("stats")
def statistic():
    return dict(stats= stats)

@route ("/static/<filepath:path>", name="static")
def static(filepath):
    #print 'yey', filepath
    return static_file(filepath,root = "./static/")
    
    
@error(404)
def error404(error):
    return static_file('404.html',root="./static")


bottle.run (host='localhost',port =8080)
#bottle.run (host = '127.0.0.1',server= production_server, port = production_port)
