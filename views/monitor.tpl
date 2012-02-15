<article id="wikilinks">
    <h2>כל הקישורים</h2>
    <p>
    %l= pages
    <p>סה"כ עריכות מה<a href="https://apps.db.ripe.net/whois/lookup/ripe/inetnum/147.237.0.0-147.237.255.255.html" target="_blank">בלוק הממשלתי</a>:<strong>{{number}}</strong>(אנחנו בודקים עד 500 לכתובת)</p>
    <!--<div class="links_nav"></div>-->
    <div id ="wiki-list">    
    <label for="wikisearch">לחיפוש בערכים: </label><input id = "wikisearch" class="search" placeholder="התחילי להקליד את שם הערך"/>
    
        <ul class="wiki-content" >
        %for m in monitor:
        %term = m.title
        %source = m.user_ip
        %a = u"http://he.wikipedia.org/w/index.php?title={0}&oldid={1}&diff=prev".format(m.title,m.revision)
        <li><strong>מקור:</strong> <span class="source">{{source}}</span>, <strong>הערך:</strong> <span class="term">{{term}}</span>. <a href="{{a}}" target="_blank" class="wiklink">(להשוואה)</a>
            
        </li>
            %end
    </ul>        
        <ul class="paging">
            %for i in range(0,pages,1):
            <li>
                <a href ="#" id="{{i}}" onclick=changePage({{i}})>
                {{i+1}}
                </a>
            </li>
            %end
        </ul>
    </div>
        
    </p>
    <section>
        <p><a href="http://t.co/szecd3nI" target="_blank">והנה גם קצת סטטיסטיקות בנושא:</a>תודות לדביר וולק</p>
    </section>
</article>

%rebase layout