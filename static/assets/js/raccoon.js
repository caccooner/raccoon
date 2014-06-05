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

    }

    $('#sidebar').sidebar({overlay:true}).sidebar('attach events',$sidebarBtn);

}

$(document).ready(raccoon.ready)