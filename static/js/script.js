/* Author:alonisser

*/
function changePage(page){
    window.location.search = "page="+page;
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
    
    

});







