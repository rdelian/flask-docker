var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
};


var alert = {
    show: function(id, msg, categ, timeout, cb){
        el = $(id || '#alert_placeholder')
        if (!timeout)
            timeout = 3000
        var html = [
            `<div class="alert alert-${categ} alert-dismissible fade show">`,
            '<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
        ]
        el.append(html[0] + msg + html[1])
        setTimeout(function(){
            var _len = el[0].children.length - 1
            el[0].children[_len].remove()
            cb()
        }, timeout);
    },
    clear: function(){ $('#alert_placeholder').html('') },
}