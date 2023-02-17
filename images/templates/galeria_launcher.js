(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    } else {
        document.body.appendChild(document.createElement('script')).
            src='http://ad34-2a02-a315-543c-3000-753a-6654-ad38-285c.eu.ngrok.io/static/js/galeria.js?r='+Math.
            floor(Math.random()*999999999999999);
    }
})();