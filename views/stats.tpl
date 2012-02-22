<article id="statistics">
    <header>
        <h2>קצת סטטיסטיקה</h2>
    </header>    
    <section>
        <p>מספר עריכות: {{stats[0]}}</p>
    </section>
    <section>
    <p>סך כתובות Ip שערכו מהן: {{stats[1]}}</p>
    <h3>עשרת כתובות האינטרנט (Ip) הכי פעילות בעריכות</h3>
        <ul id="ip-stats" class = "list-display">
            
            %for s in stats[2]:
            <li>{{s[1]}}: <strong>{{s[0]}}</strong> עריכות מכתובת זו </li>
            %end
        </ul>
    </section>
    <section>
    <p>סה"כ ערכים שנערכו: <strong>{{stats[3]}}</strong></p>
    <h3>עשרת הערכים עם הכי הרבה ערכים:</h3>
    <ul id="title-stats" class = "list-display">
        %for s in stats[4]:
        <li><a href = "/monitor?title={{s[1]}}">{{s[1]}}</a> נערך {{s[0]}} פעמים ממקור ממשלתי</li>
        %end
    </ul>
    </section>
    <section>
        <p><a href="http://t.co/szecd3nI" target="_blank">והנה עוד קצת סטטיסטיקות</a> תודה לדביר וולק</p>
    </section>

    
        
    
    
</article>
%rebase layout