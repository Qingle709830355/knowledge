$(function () {

    $("#all_types").click(function () {

        $("#all_types_container").show();
        $("#all_type_logo").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
        $("#sort_container").hide();
        $("#sort_rule_logo").addClass("glyphicon-chevron-down").removeClass("glyphicon-chevron-up");
    })


    $("#all_types_container").click(function () {
        $(this).hide();
        $("#all_type_logo").addClass("glyphicon-chevron-down").removeClass("glyphicon-chevron-up");

    })


    $("#sort_rule").click(function () {
        $("#sort_container").show();
        $("#sort_rule_logo").addClass("glyphicon-chevron-up").removeClass("glyphicon-chevron-down");
        $("#all_types_container").hide();
        $("#all_type_logo").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
    })

    $("#sort_container").click(function () {
        $(this).hide();
        $("#sort_rule_logo").addClass("glyphicon-chevron-down").removeClass("glyphicon-chevron-up");
    });

    $('.addShopping').on('click', function () {


    });


    // // 添加商品到购物车
    // $(".subShopping").click(function () {
    //     //    拿到商品id发送给服务器
    //     // var subShop = $(this);
    //     // var goodsid = $(this).attr("goodsid");
    //     // // console.log(goodsid);
    //     // // console.log($(this).attr("class"));
    //     // // console.log("**************")
    //     // // var goodsid2 = $(this).prop("goodsid");
    //     // // console.log(goodsid2);
    //     // // console.log($(this).prop("class"));
    //     //
    //     // $.getJSON("/axf/subtocart/", {"goodsid": goodsid}, function (data) {
    //     //     console.log(data);
    //     //     if (data["status"] == "901") {
    //     //         window.open("/axf/userlogin/", target = "_self");
    //     //     } else if (data["status"] == "200") {
    //     //         var g_num = data["g_num"];
    //     //         var span_num = subShop.next();
    //     //         span_num.html(g_num);
    //     //     } else if (data["status"] == "902") {
    //     //         alert(data["msg"]);
    //     //     }
    //     // })
    //     alert('点击了这里！')
    // })

    show_aready_choice()

});
 //  添加商品到购物车
function addtocart(id){
    var str1 = '#span' + id;
    csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type: 'post',
        data: {'goods': id},
        headers: {'X-CSRFToken': csrf},
        dataType: 'json',
        url: '/axf/addcar/',
        error: function (msg) {
            console.log(msg);
            console.log('添加失败！')
        },

        success: function (msg) {
            console.log(msg);
            console.log('添加成功!');
            $(str1).text(msg.c_num);
            $('#total').text(msg.total)
        }
    })
}

function subtocart(id) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val();
    var str1 = '#span' + id;
    $.ajax({
        type: 'post',
        data: {'goods': id},
        headers: {'X-CSRFToken': csrf},
        dataType: 'json',
        url: '/axf/subcar/',
        error: function (msg) {
            alert('错误')
        },

        success: function (msg) {
            console.log(msg);
            $(str1).text(msg.c_num);
            $('#total').text(msg.total)
        }
    })
}

function show_aready_choice(){
        csrf = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            type: 'get',
            dataType: 'json',
            url: '/axf/showareadychoice/',
            headers: {'X-CSRFToken': csrf},
            error: function (msg) {
                console.log('请求错误！')
            },

            success: function (msg) {
                console.log(msg);
                for(var i = 0; i < msg.data.length; i++){
                    $('#span'+ msg.data[i].good_id).text(msg.data[i].c_num);
                }
            }
        });
}

function choose_foodtype(typeid) {

    csrf = $('input[name="csrfmiddlewaretoken"]');
    $.ajax({
        type: 'get',
        dataType: 'json',
        url: '/axf/typeidchoice/',
        data: {'typeid': typeid},
        headers: {'X-CSRFToken': csrf},
        error: function (msg) {
            console.log('请求失败！')
        },

        success: function (msg) {
            console.log(msg);
            var goods = msg.goods;

            $('.yellowSlide').attr('class', '').attr('foodtype', '');
            $('#id_' + typeid).attr('class', 'yellowSlide').attr('foodtype', typeid);
            $('#show-goods').empty();
            $('#typeslist').empty();
            for(var i = 0; i < goods.length; i++){
                if(('' +goods[i].price).length == 1){
                    goods[i].price = goods[i].price + '.0'
                }
                if(('' + goods[i].marketprice).length == 1){
                    goods[i].marketprice = goods[i].marketprice + '.0'
                }
                s = '<li>' +
                    '<a href="#"><img src="' + goods[i].productimg + '" alt="" id="good_img">' +
                    '<div class="shoppingInfo">' +
                    '<h6>' +  goods[i].productlongname +  '</h6>' +
                    '<p class="detailTag"><span>精选</span><span>热销中</span>' +
                    '</p><p class="unit">' +
                    '</p><p class="price">' +
                    '<span>￥'+ goods[i].price + '</span>'+
                    '<s>￥' + goods[i].marketprice + '</s></p></div></a>' +
                    '<section>' +
                    '<button goodsid="' +  goods[i].id +'" onclick="subtocart(' + goods[i].id +' )">-</button>' +
                    '<span id="span'+ goods[i].id +'">0</span>'+
                    '<button goodsid="' + goods[i].id + '" onclick="addtocart('+ goods[i].id + ')">+</button>' +
                    '</section></li>';
                $('#show-goods').append(s)
            }
            for(var j = 0; j < msg.listnames.length; j++){
                s = '<a href="#" onclick="choice_childid('+ msg.listnames[j].id +  ',' + 1 + ')">\n' +
                    '<span>'+msg.listnames[j].childname + '</span>\n' +
                    '</a>';
                $('#typeslist').append(s)
            }
            show_aready_choice()
        }
    });
}

function choice_childid(childid, type) {
    typeid = $('.yellowSlide').attr('foodtype');
    $.ajax({
        type: 'get',
        dataType: 'json',
        url: '/axf/childidchoice/',
        data: {'typeid': typeid, 'childid': childid, 'type': type},
        error: function (msg) {
            console.log(msg);
            console.log('请求失败！');
        },

        success: function (msg) {
            console.log(msg);
            var goods = msg.goods;
            $('#show-goods').empty();
            $('#typeslist').empty();
            for(var i = 0; i < goods.length; i++){
                if(('' +goods[i].price).length == 1){
                    goods[i].price = goods[i].price + '.0'
                }
                if(('' + goods[i].marketprice).length == 1){
                    goods[i].marketprice = goods[i].marketprice + '.0'
                }
                s = '<li>' +
                    '<a href="#"><img src="' + goods[i].productimg + '" alt="" id="good_img">' +
                    '<div class="shoppingInfo">' +
                    '<h6>' +  goods[i].productlongname +  '</h6>' +
                    '<p class="detailTag"><span>精选</span><span>热销中</span>' +
                    '</p><p class="unit">' +
                    '</p><p class="price">' +
                    '<span>￥'+ goods[i].price + '</span>'+
                    '<s>￥' + goods[i].marketprice + '</s></p></div></a>' +
                    '<section>' +
                    '<button goodsid="' +  goods[i].id +'" onclick="subtocart(' + goods[i].id +' )">-</button>' +
                    '<span id="span'+ goods[i].id +'">0</span>'+
                    '<button goodsid="' + goods[i].id + '" onclick="addtocart('+ goods[i].id + ')">+</button>' +
                    '</section></li>';
                $('#show-goods').append(s)
            }
            for(var j = 0; j < msg.listnames.length; j++){
                s = '<a href="#" onclick="choice_childid('+ msg.listnames[j].id + ',' + 1 + ')">\n' +
                    '<span id="">'+msg.listnames[j].childname + '</span>\n' +
                    '</a>';
                $('#typeslist').append(s);

            }
            for(var s = 1; s < 5; s ++){
                    $('#sort_' + s).attr('onclick', 'choice_childid(' + childid + ',' + s + ')')
            }

            show_aready_choice()
        }
    })
}
