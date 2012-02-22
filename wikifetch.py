#!/bin/usr/env python
#-*- coding:UTF-8 -*-

import requests,json
from datetime import datetime,date
from config import connectstring

from sqlalchemy import create_engine,String,Unicode,Integer, Column, func,distinct, desc
engine = create_engine(connectstring) #created the engine connecting sqlalchemy to the db

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
Base  = declarative_base()


def init_db():
    
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

    def to_dict(self):
        try:
            title = self.title.encode('utf-8')
        except:
            title = self.title
        
        return {'id':self.id, 'title':title, 'Ip':self.user_ip,'revision':self.revision,'page':self.page}

def wiki_populate():
    '''a function to populate the db with wikipedia edits
    initializing the db and creating the tables if needed.
    iterating through the whole goverment ip range and calling wikifetch fucntion for each ip'''
    
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
    '''A function that does the actuall fetching of edits from wikipedia api'''
    
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
            wikifetch(ip,more =content['query-continue']['usercontribs']["uccontinue"])#recursive call to the function if there is more data in the same Ip
def schedule():
    '''this would be the scheduling function, running the fetch as a cron job'''
    pass

def statistic():
    '''some statistics about the usage including number, most edited, etc
    return result packed in a tuple'''
    session = load_session()
    total = session.query(Wikilink).count();
    used_ip_num = session.query(func.count(distinct(Wikilink.user_ip))).scalar() #scalar to return a number
    most_used_ip_addresses = session.query(func.count(Wikilink.user_ip),Wikilink.user_ip).group_by(Wikilink.user_ip).order_by(desc(func.count(Wikilink.user_ip))).all()
    #most_used_ip_addresses.sort()
    most_edited_ip_ten = most_used_ip_addresses[0:10]#.reverse() #top ten ip list
    #most_edited_ip_ten.reverse()
    title_num = session.query(func.count(distinct(Wikilink.title))).scalar()
    most_edited_titles = session.query(func.count(Wikilink.title),Wikilink.title).group_by(Wikilink.title).order_by(desc(func.count(Wikilink.title))).all()
    most_edited_titles_ten = most_edited_titles[0:10]#.reverse() #top ten title edits
    #most_edited_titles_ten.reverse()
                              
    return (total,used_ip_num, most_edited_ip_ten,title_num,most_edited_titles_ten)
    
