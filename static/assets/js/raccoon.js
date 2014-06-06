/**
 * Created by carvee on 14-6-5.
 */
window.raccoon = {
    handler:{}
}


raccoon.ready = function(){
    // element cache
    var
    $sidebarBtn = $('.top.icon.button'),

    handler;

    handler = {
        snsBind : function(){
            console.log($(this).attr('data-bind-sns'))
            url = $(this).attr('data-bind-sns');
            result = window.open(url)
        }
    }

    $('#sidebar').sidebar({overlay:true}).sidebar('attach events',$sidebarBtn);
    $('[data-bind-sns]').click(handler.snsBind)
}

$(document).ready(raccoon.ready)