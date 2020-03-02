$(document).ready(function () {
    // Open Modal
    $('#openModal').click(function () {
        $('#modalToOpen').css({
            'display': 'block'
        });
    });

    $('#openModal1').click(function () {
        $('#modalToOpen').css({
            'display': 'block'
        });
    });

    // Close Modal
    $('#closeModal').click(function () {
        $('#modalToOpen').css({
            'display': 'none'
        });
    });
    $('#closeModalCancel').click(function () {
        $('#modalToOpen').css({
            'display': 'none'
        });
    });

    $('#closeNotificationModal1').click(function () {
        $('#js_alert_successModal').css({
            'display': 'none'
        });
    });
    $('#closeNotificationModal2').click(function () {
        $('#js_alert_dangerModal').css({
            'display': 'none'
        });
    });
    $('#closeNotificationEnd1').click(function () {
        $('#js_alert_successEnd').css({
            'display': 'none'
        });
    });
    $('#closeNotificationEnd2').click(function () {
        $('#js_alert_dangerEnd').css({
            'display': 'none'
        });
    });

    // send mail with ajax
    $('#sendEmailModal').click(function (e) {
        e.preventDefault();
        var data = {
            email: $('#email').val(),
            name: $('#name').val(),
            subject: $('#subject').val(),
            message: $('#message').val()
        };
        $.ajax({
            url: "mail.php",
            type: 'POST',
            data: data,
            success: function (data) {
                $('#js_alert_successModal').css({ 'display': 'block' });
                setTimeout(function () {
                    $('#email').val("");
                    $('#name').val("");
                    $('#subject').val("");
                    $('#message').val("")
                }, 3000);
            },
            error: function (data) {
                $('#js_alert_dangerModal').css({ 'display': 'block' });
                setTimeout(function () {
                    $('#email').val();
                    $('#name').val();
                    $('#subject').val();
                    $('#message').val()
                }, 3000);
            }
        });
    });

    $('#sendEmailModal').click(function(){
        if($('#email').val() == ''){
           alert('Input can not be left blank');
        }
     });
    // EmailTwo
    $('#sendEmailEnd').click(function (e) {
        e.preventDefault();
        var data = {
            email: $('#emailEnd').val(),
            name: $('#nameEnd').val(),
            subject: $('#subjectEnd').val(),
            message: $('#messageEnd').val()
        };
        $.ajax({
            url: "mail.php",
            type: 'POST',
            data: data,
            success: function (data) {
                $('#js_alert_successEnd').css({ 'display': 'block' });
                setTimeout(function () {
                    $('#emailEnd').val("");
                    $('#nameEnd').val("");
                    $('#subjectEnd').val("");
                    $('#messageEnd').val("")
                }, 3000);
            },
            error: function (data) {
                $('#js_alert_dangerEnd').css({ 'display': 'block' });
                setTimeout(function () {
                    $('#emailEnd').val();
                    $('#nameEnd').val();
                    $('#subjectEnd').val();
                    $('#messageEnd').val()
                }, 3000);
            }
        });
    });
    $('#sendEmailEnd').click(function(){
        if($('#emailEnd').val() == ''){
           alert('Input can not be left blank');
        }
     });
});

let btn = document.querySelector('.toggle_btn');
let nav = document.querySelector('.nav');
let toggle_btn = document.querySelector('.toggle_btn');

btn.onclick = function () {
    nav.classList.toggle('nav_open');
    toggle_btn.classList.toggle('toggle_btn_open');
}

$(document).ready(function () {
    let src1 = 'src/img/bars.svg'
    let src2 = 'src/img/times-circle.svg'
    let flag = 0;
    $("img#bars").click(function () {
        if (flag == 0) {
            $("#bars").attr("src", src2);
            flag = 1;
        } else if (flag == 1) {
            $("#bars").attr("src", src1);
            flag = 0;
        }
    });
});