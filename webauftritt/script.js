var diagramm_step = 0;

function diagramm_animation() {
    diagramm_step++;
    if (diagramm_step % 4 == 0) {
        $('#diagramm').removeClass('step1');
        $('#diagramm').removeClass('step2');
        $('#diagramm').removeClass('step3');
        diagramm_step++;
    }
    $('#diagramm').addClass('step' + (diagramm_step % 4));
}

$(document).ready(function() {
    $('body').show();
    $('#fullpage').fullpage({
        scrollOverflow: true,
        anchors: ['ug', 'aboutus', 'aquaponic', 'concept', 'contact'],
        afterResize: function() {
            console.log('render');
            if ($(window).width() < 992) {
                $('#diagramm').css('height', $(window).height() * 0.3 + 'px');
                console.log('render2');
            } else {
                $('#diagramm').css('height', '');
            }
        },
        afterRender: function() {
            console.log('render');
            if ($(window).width() < 992) {
                $('#diagramm').css('height', $(window).height() * 0.3 + 'px');
                console.log('render2');
            } else {
                $('#diagramm').css('height', '');
            }
        }
    });
    $('#diagramm').on('click', function() {
        diagramm_animation();
    });
    $('#next').on('click', function() {
        diagramm_animation();
    });
});
