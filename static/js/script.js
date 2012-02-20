/* Author:alonisser

*/
function changePage(page){
    var search = window.location.search;
    if (search.indexOf('title')==-1){
    window.location.search = "page="+page;
    } else {
        window.location.search = search.split('&')[0]+"&page="+page;
    }
    
}

function nicePagination(current){
    console.log(current)
    //current is the current page number
    
    list = $('ul.paging li');
    len = list.length;
    list.addClass('remove').hide();
    
    show = [0,len];
    if (len>3){
        show.push(1,len-1,len-2);
    }
    if (current){
        show.push(current-1,current,current+1);
        }
    show.sort();
    var s = show.length;
    var li;
    for (var i=0;i<s;i++){
        li = "#page-"+show[i];
        $(li).parent().show().removeClass('remove');
        if (show[i]>0 &&(show[i]-show[i-1])>1){
            $(li).parent().append('<span>...</span>');
            $(li).parent().prepend('<span>...</span>');
        }
        //console.log(li);
        
    }
    //$('ul.paging li.remove').each(function(index,elem){
    //    elem.remove();
    //    });
    
    
    
}
$(document).ready(function(){
    $('#wikisearch').keydown(function(ev){
        //ev.preventDefault();
        if (ev.keyCode == '13'){
            
            //var loc = window.location.origin+window.location.pathname;
            var title = this.value;
            window.location.search= "title="+title;
            console.log(title);
            //alert (this.value);
        }
        
    });
    var page = window.location.search.split('page=')[1];
    if (page){
        page = parseInt(page);
        nicePagination(page);
    } else {
        nicePagination(0);
    }
    
});