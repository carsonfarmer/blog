     $(document).ready(function() {
    
        $("#top-query").keydown(function(event) {
            if (event.keyCode == 13) {
                event.preventDefault();
                site_search();
                return false;
            }
        });
        $("#top-btn").click(function(event) {
            event.preventDefault();
            site_search();
            return false;
        });
    });
    
function site_search() {
    var query = $("#top-query").val();
    if (query == "") return false;
    var api = 'http://tapirgo.com/api/1/search.json?';
    var token = '51980cd33f61b05bbb000ce0';
    var el = $("#top-results");
    el.empty();
    el.append('<li style="padding-left: 10px">Fetching results...</li>')
    $.getJSON(api + 'token=' + token + '&query=' + query + '&callback=?', 
        function(data) {
            // insert function here if needed
            if (data.length) {
                el.empty();
                $.each(data, function(key, val) {
                    var xx = new Date(val.published_on)+""
                    if ((/^http\:\/\/www.carsonfarmer.com/).test(val.link)) { // hack to ignore duplicate returns
                        el.append('<li><a href="' + val.link + '" data-toggle="tooltip" data-placement="left" ' + 
                            'title="'+ xx.substring(0,15) + '">' + val.title + '</a>' + '</li>');
                    }
                });
            } else {
                el.empty();
                el.append('<li style="padding-left: 10px">No results found...</li>')
            };
            $("[data-toggle=tooltip]").tooltip();
        });
        $("#top-toggle").dropdown('toggle');
    }  

(function() {
    var win = $(window);
    win.resize(function() {
        var win_w = win.width(),
            win_h = win.height(),
            bg    = $("#bg");
        // Load narrowest background image based on 
        // viewport width, but never load anything narrower 
        // that what's already loaded if anything.
        var available = [ 1024, 1280, 1400, 1800, 2400 ];
        var current = bg.attr('src').match(/([0-9]+)/) ? RegExp.$1 : null;

        if (!current || ((current < win_w) && (current < available[available.length - 1]))) {
          var chosen = available[available.length - 1];
          for (var i=0; i<available.length; i++) {
            if (available[i] >= win_w) {
              chosen = available[i];
              break;
            }
          }
          // Set the new image
          bg.attr('src', '/theme/images/bg/bg-' + chosen + '.png');
          // for testing...
          // console.log('Chosen background: ' + chosen);
        }
        // Determine whether width or height should be 100%
        if ((win_w / win_h) < (bg.width() / bg.height())) {
          bg.css({height: '100%', width: 'auto'});
        } else {
          bg.css({width: '100%', height: 'auto'});
        }
      }).resize();
    })(jQuery);
    
    
/*
 * Replace all SVG images with inline SVG
 */
    jQuery('img.svg').each(function(){
        var $img = jQuery(this);
        var imgID = $img.attr('id');
        var imgClass = $img.attr('class');
        var imgURL = $img.attr('src');

        jQuery.get(imgURL, function(data) {
            // Get the SVG tag, ignore the rest
            var $svg = jQuery(data).find('svg');

            // Add replaced image's ID to the new SVG
            if(typeof imgID !== 'undefined') {
                $svg = $svg.attr('id', imgID);
            }
            // Add replaced image's classes to the new SVG
            if(typeof imgClass !== 'undefined') {
                $svg = $svg.attr('class', imgClass+' replaced-svg');
            }

            // Remove any invalid XML tags as per http://validator.w3.org
            $svg = $svg.removeAttr('xmlns:a');

            // Replace image with new SVG
            $img.replaceWith($svg);

        }, 'xml');

    });