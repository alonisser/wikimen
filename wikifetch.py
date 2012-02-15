#!/bin/usr/env python
#-*- coding:UTF-8 -*-

import requests,json
from datetime import datetime,date
connectstring = "mysql+mysqldb://pyuser:pyuser@localhost:3306/wikidb?charset=utf8&use_unicode=0" #user:password@server:port/dbname change to real db params
from sqlalchemy import create_engine,String,Unicode,Integer, Column
engine = create_engine(connectstring) #created the engine connecting sqlalchemy to the db

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
Base  = declarative_base()


def init_db():
    connectstring = "mysql+mysqldb://pyuser:pyuser@localhost:3306/wikidb?charset=utf8&use_unicode=0" #user:password@server:port/dbname change to real db params
    engine = create_engine(connectstring) #created the engine connecting sqlalchemy to the db


def load_session():

    Session = sessionmaker(bind = engine)
    session = Session() #the session used to communicate with the db
    return session



class Wikilink(Base):

    __tablename__='Wikilinks'
    __table_args__={'extend_existing':True}
        
    id = Column(Integer,autoincrement=True,primary_key=True)
    title = Column(Unicode(350))
    user_ip = Column(String(50))
    page = Column(String(20))
    revision = Column(String(20))
    timestamp = Column(String(50))

def wiki_populate():
    init_db()
    Wikilink.metadata.create_all(engine)
    
    ip_range = []
    for i in range(228,238,1):
        for n in range(0,256,1):
            ip_range.append('147.%d.%d'%(i,n))
    #ip_range = ['147.237.70']#debuggin
    
    for ip in ip_range:
        try:
            wikifetch(ip)
        except:
            continue
    
def wikifetch(ip,more = None):
    session = load_session()
    timestamp = datetime.now().isoformat()
    headers = {'User-Agent':'wikipediagovmonitoring'}
    if not more:
        print "fetching..%s" %ip
        query = 'http://he.wikipedia.org/w/api.php?action=query&list=usercontribs&format=json&uclimit=500&ucuserprefix=%s&ucdir=newer&ucprop=title|ids' % ip
    else:
        print 'fetching continues for ip ', ip
        query = 'http://he.wikipedia.org/w/api.php?action=query&list=usercontribs&format=json&uclimit=500&ucuserprefix=%s&uccontinue=%s&ucdir=newer&ucprop=title|ids' % (ip, more)
    #print ip
    try:        
        r = requests.get(query,headers=headers)
    except:
        print "raising error from ip:%s" % ip
        raise
    if r.ok:
        content = json.loads(r.content)
        print "number of items from %s is %s" % (ip,len(content['query']['usercontribs']))
        for i in content['query']['usercontribs']:
            link = Wikilink(user_ip=i['user'],
                            title=i['title'][0:350],
                            page=i['pageid'],
                            revision=i['revid'],
                            timestamp=timestamp)
                            
            #print edit
            session.add(link)
            #print link.id,link.title, link.page, link.timestamp, link.revision,link.user_ip
            session.flush()
            
        if content.get('query-continue',False):
            wikifetch(ip,more =content['query-continue']['usercontribs']["uccontinue"])
    
def wikimonitor(dump=None):
    
    ip_range = []
    
    ip_range = ['147.237.70']#debuggin
    headers = {'User-Agent':'wikipediagovmonitoring'}
    result = []
    for ip in ip_range:
        query = 'http://he.wikipedia.org/w/api.php?action=query&list=usercontribs&format=json&uclimit=100&ucuserprefix=%s&ucdir=newer&ucprop=title|ids' % ip
        print ip
        try:        
            r = requests.get(query,headers=headers)
        except:
            continue
        if r.ok:
            content = json.loads(r.content)
            for i in content['query']['usercontribs']:
                edit = {'source':i['user'],'title':i['title'],'page':i['pageid'],'revision':i['revid']}
                #print edit
                result.append(edit)

    if dump:
        return result