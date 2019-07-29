$(function () {

    // 点击支付
    $('#pay').click(function () {
        $.get("/app/topay/", function (data) {
            console.log(data)
            let re_url = data.re_url
            location.href = re_url;
        });

    });

});