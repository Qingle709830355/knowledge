// 页面加载准备好了     就是页面基本结构加载完成
$(function () {


    // $(".is_choose").click(function () {
    //     console.log("点击");
    //     var current_li = $(this);
    //     var cart_id = current_li.parents("li").attr("cartid");
    //     console.log(cart_id);
    //
    //     $.getJSON("/axf/changecartstatus/", {"cart_id":cart_id}, function (data) {
    //         console.log(data);
    //         if (data["status"] == "200"){
    //             if (data["check"]){
    //                 var span = current_li.find("span");
    //                 span.html("√");
    //
    //                 if(data["is_all_select"]){
    //                     $("#all_select").find("span").html("<span>√</span>");
    //                 }
    //
    //             }else{
    //                 var span = current_li.find("span");
    //                 span.html("");
    //                 $("#all_select").find("span").html("<span></span>");
    //             }
    //             current_li.attr("is_select",data["check"]);
    //         }
    //     })
    // })


    // $(".subShopping").click(function () {
    //     // 代表记住我们这一样  真实是点击的button
    //     var current_li = $(this);
    //     var cart_id = current_li.parents("li").attr("cartid");
    //     console.log(cart_id);
    //
    //     $.getJSON("/axf/subcart/", {"cart_id": cart_id}, function (data) {
    //
    //         console.log(data);
    //
    //         if (data["status"] == "200"){
    //             current_li.next().html(data["c_num"]);
    //         }else if (data["status"] == "903"){
    //             current_li.parents("li").remove();
    //         }
    //     })
    //
    // })
    //
    //
    // $(".addShopping").click(function () {
    //
    //     var current_li = $(this);
    //     var cart_id = current_li.parents("li").attr("cartid");
    //
    //     $.getJSON("/axf/addcart/", {"cart_id": cart_id}, function (data) {
    //         console.log(data);
    //         if (data["status"] == "200"){
    //             current_li.prev().html(data["c_num"]);
    //         }
    //     })
    //
    // })


    // $("#all_select").click(function () {
    //
    // //    如果有未选中的，应该执行操作是全部选中
    // //    并且让自己的按钮变成选中状态
    // //    如果全都是选中的，全部取消选中
    //     var not_selects = [];
    //     var selects = [];
    //
    //     $(".is_choose").each(function () {
    //         console.log($(this).attr("is_select"));
    //         if ($(this).attr("is_select").toLowerCase() == "false"){
    //             // 将未选中添加到指定集合中
    //             not_selects.push($(this).parents("li").attr("cartid"));
    //         }else{
    //             selects.push($(this).parents("li").attr("cartid"));
    //         }
    //     })
    //
    //     console.log(not_selects);
    //
    //     if (not_selects.length == 0){
    //         console.log("全都变成未选中");
    //
    //         $.getJSON("/axf/changecartselect/",{"selects": selects.join("#"),"action":"unselect"}, function (data) {
    //             console.log(data);
    //             if (data["status"] == "200"){
    //                 var selects = data["selects"];
    //                 var select_list = selects.split("#");
    //                 console.log(select_list);
    //                 $(".is_choose").each(function () {
    //                     $(this).find("span").html("");
    //                     $(this).attr("is_select", "false");
    //                 })
    //                 $("#all_select").find("span").html("<span></span>");
    //             }
    //         })
    //
    //     }else{
    //         console.log("全部变成选中");
    //         $.getJSON("/axf/changecartselect/",{"selects": not_selects.join("#"), "action":"select"}, function (data) {
    //             console.log(data);
    //             if(data["status"] == "200"){
    //                 var selects = data["selects"];
    //                 var select_list = selects.split("#");
    //                 $(".is_choose").each(function () {
    //
    //                      $(this).find("span").html("√");
    //                     $(this).attr("is_select", "true");
    //
    //                 })
    //                 $("#all_select").find("span").html("<span>√</span>");
    //
    //             }
    //         })
    //     }
    //
    // })
    //
    // $("#generate_order").click(function () {
    //
    //     alert('点击了这里！');
    //     var select_list = [];
    //
    //     $(".is_choose").each(function () {
    //
    //         var current = $(this);
    //
    //         if (current.attr("is_select").toLowerCase() == "True") {
    //             var cart_id = current.parents("li").attr("cartid");
    //             select_list.push(cart_id);
    //         }
    //     })
    //
    //     if (select_list.length == 0) {
    //         alert("您还没有选择任何商品");
    //         return false
    //     }
    // });
    //
    //         $.getJSON("/axf/generateorder/", {"selects": select_list.join("#")}, function (data) {
    //             console.log(data);
    //
    //             if (data["status"] == "200"){
    //
    //                 window.open("/axf/orderinfo/"+data["order_id"]+"/", target="_self");
    //
    //             }
    //
    //         })
    //
    //
    //
    //
    //     }
    //
    // });

    $(".is_choose").on('click', function () {
        cart_id = $(this).attr('cart_id');
        csrf = $('input[name="csrfmiddlewaretoken"]').val();
        len = $('.is_choose[is_select="True"]').length;
        $.ajax({
            type: 'post',
            data: {'id': cart_id, 'l': len},
            url: '/axf/changecartstatus/',
            headers: {'X-CSRFToken': csrf},
            error: function (msg) {
                console.log('错误');
            },

            success: function (msg) {
                console.log(msg);
                if(msg.is_select){
                    $('#select_' + cart_id).text('√');
                    $('#select_' + cart_id).parent().attr('is_select', 'True')
                }else{
                    $('#select_' + cart_id).text('');
                    $('#select_' + cart_id).parent().attr('is_select', 'False')
                }
                $('#total').text(msg.total);
                if(msg.is_all){
                    s = '<span is_all="True" id="isselectall">√</span>';
                }else{
                    s = '<span is_all="True" id="isselectall"></span>';
                }
                $('#select_all').html(s)
            }
        })
    });
    isSelectAll();

    if($('#message').val() != ''){
        alert($('#message').val())
    }
});
function isSelectAll(id) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val();
    len = $('.is_choose[is_select="True"]').length;
    is_all = $('#isselectall').attr('is_all');
    $.ajax({
        type: 'post',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        url: '/axf/isselectall/',
        data: {'len': len, 'is_all': is_all},
        error: function (msg) {
            console.log('错误')
        },

        success: function (msg) {
            console.log(msg);
            if(msg.is_all){
                s = '<span is_all="True" id="isselectall">√</span>';
                if( id==1 ){
                    $('.singleselect').text('√');
                    $('.singleselect').parent().attr('is_select', 'True')
                }
            }else{
                s = '<span is_all="False" id="isselectall"></span>';
                if( id== 1){
                    $('.singleselect').text('');
                    $('.singleselect').parent().attr('is_select', 'False')
                }
            }
            $('#select_all').html(s);
            $('#total').text(msg.total)
        }
    });
}