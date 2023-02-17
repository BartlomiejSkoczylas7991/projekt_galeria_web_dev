(function(){
  var jquery_version = '3.4.1';
  var site_url = 'https://127.0.0.1:8000/';
  var static_url = site_url + 'static/';
  var min_width = 100;
  var min_height = 100;

  function galeria(msg) {
    var css = jQuery('<link>');
    css.attr({
      rel: 'stylesheet',
      type: 'text/css',
      href: static_url + 'css/galeria.css?r=' + Math.floor(Math.random()*99999999999999999999)
    });
    jQuery('head').append(css);

    box_html = '<div id="galeria"><a href="#" id="close">&times;</a><h1>Wybierz obraz do galerii:</h1><div class="images"></div></div>';
    jQuery('body').append(box_html);

    jQuery('#galeria #close').click(function(){
       jQuery('#galeria').remove();
    });
    jQuery.each(jQuery('img[src$="jpg"]'), function(index, image) {
      if (jQuery(image).width() >= min_width && jQuery(image).height()
      >= min_height)
      {
        image_url = jQuery(image).attr('src');
        jQuery('#galeria .images').append('<a href="#"><img src="'+
        image_url +'" /></a>');
      }
    });

    jQuery('#galeria .images a').click(function(e){
      selected_image = jQuery(this).children('img').attr('src');
      jQuery('#galeria').hide();
      window.open(site_url +'images/create/?url='
                  + encodeURIComponent(selected_image)
                  + '&title='
                  + encodeURIComponent(jQuery('title').text()),
                  '_blank');
    });

  };

  if(typeof window.jQuery != 'undefined') {
    galeria();
  } else {
    var conflict = typeof window.$ != 'undefined';
    var script = document.createElement('script');
    script.src = '//ajax.googleapis.com/ajax/libs/jquery/' +
      jquery_version + '/jquery.min.js';
    document.head.appendChild(script);
    var attempts = 15;
    (function(){
      if(typeof window.jQuery == 'undefined') {
        if(--attempts > 0) {
          window.setTimeout(arguments.callee, 250)
        } else {
          // Za dużo obrazów do wczytania - błąd
          alert('Wystąpił błąd podczas uruchamiania jquery')
        }
      } else {
          galeria();
      }
    })();
  }
})()