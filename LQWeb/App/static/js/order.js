$(function(){
				function car(){
					//从cookie中获取购物车的所有商品
					var log = $.cookie("log")
					$('.tttt').find("ul").remove();
				var arr = $.cookie(log+"_cart");
				if (arr) {
					arr = JSON.parse(arr);


					//遍历数组, 显示所有商品的信息

					for (var i=0; i<arr.length; i++) {
					  var tbody = $(".tttt")
					  var ul = $("<ul/>").appendTo(tbody)
					  var li = $("<li/>").appendTo(ul)
					  $("<input/>").attr({
					  	"type":"checkbox",
					  	"class":"imp"
					  }).css({
					  	"display":"block",
					  	"float":'left',
					  	"margin-left":"15px",
					  	"margin-top":"30px"
					  }).appendTo(li)
					  var pic = $("<div/>").attr("class","pic").appendTo(li);
					  var a = $("<a/>").html(arr[i].img).appendTo(pic);
					  var title = $("<div/>").attr("class","title").appendTo(li)
					  var b = $("<a/>").html(arr[i].name).appendTo(title);
					  var price = $("<div>").attr("class","price").css({"font-size":"13px"}).appendTo(li);
					  var sp = $("<span/>").html(arr[i].price).attr("class","sp").appendTo(price);
					  var num = $("<div/>").attr("class","num").appendTo(li);

					  var sp2 = $("<span>").appendTo(num)
					  var inp2 = $("<input/>").attr({
					  	    "class":"btn2",
					  	    "type":"text",
					  	    "value":"1"
					  }).css({
					  	'border': 0,
					  	"width": "30px",
					  	"height": "20px",
					  	"line-height": "20px",
					  	"text-align": "center",
					  	"margin-top": "30px"
					  }).val(arr[i].ber).appendTo(sp2)


					  var Price = $("<div/>").attr("class","Price").appendTo(li)
					  var sp4 = $("<span/>").html("￥"+arr[i].sp).css({"font-size":"13px"}).attr("class","sp4").appendTo(Price)
						// 判断是否登录
					  if($.cookie("log")) {
						  var user = $.cookie("log")
						  var jifen = $("<div/>").attr("class", "jifen").html(user).appendTo(li)
					  }
					  var caozuo = $("<div/>").attr("class","caozuo").appendTo(li)
					  var a1 = $("<a/>").html("清除").appendTo(caozuo)

					  var other = $("<div/>").attr("class","other").appendTo(li)
					  var font = $("<font/>").html("满赠活动").css({"color":"red","font-size":"12px"}).appendTo(other)


                       $("[type=checkbox]").prop("checked",true)
                      // 添加选择状态
                      $("#buton").click(function(){
                      	if($(this).prop("checked")){
                      		$(".imp").prop('checked',true);
                      		CC();
                      	}else{
                      		$(".imp").prop('checked',false);
                      		$("#NUM").html(0);
					        $("#check_acount").html(0)
					        $("#PRI").html("￥0.00")
				            $("#check_allacount").html("￥0.00")
                      	}

                      })




                      //  给单个选中添加价格事件
                      $(".imp").click(function(){
                      	CC();
                      	var SS=0;
                      	var IMp = $(".imp")
                      	for(var i=0;i<IMp.length;i++){
                      		if($(".imp").prop("checked")){
                      		SS++;
                      	  }
                      	}
                        var VV = $(".imp").length;
                        $("#buton").prop("checked",SS==VV)
                      })
				    }
				}
			}

			    //页面加载时 刷新cookie
                car();

				// 给商品添加数量增减事假
				$(".btn1").click(function(){
					var val = parseInt($(this).parent().siblings().find(".btn2").val())
					$("#NUM").html(val-1);
					$("#check_acount").html(val-1)
					if(val>1){
						val-=1;
						$(this).parent().siblings().find(".btn2").val(val)
						var pr = parseFloat($(this).parents("li").find(".sp").html().slice(1))
					    $(this).parents("li").find(".sp4").html("￥"+(val*pr).toFixed(2))
					    $("#PRI").html("￥"+(val*pr).toFixed(2))
					    $("#check_allacount").html("￥"+(val*pr).toFixed(2))
					    BB()
					    CC()
					}
				})

				//给加 添加事件
				$(".btn3").click(function(){
					var val = parseInt($(this).parent().siblings().find(".btn2").val())

					$("#check_acount").html(val+1)
						val+=1;
						$(this).parent().siblings().find(".btn2").val(val)
						var pr = parseFloat($(this).parents("li").find(".sp").html().slice(1))
					    $(this).parents("li").find(".sp4").html("￥"+(val*pr).toFixed(2))
				        $("#PRI").html("￥"+(val*pr).toFixed(2))
				        $("#check_allacount").html("￥"+(val*pr).toFixed(2))
				        BB()
				        CC()
				})

				// 封装 cookie数量增减
				function BB(){
					var log = $.cookie("log")
					var arr3 = $.cookie(log+"_cart") ? JSON.parse( $.cookie(log+"_cart") ) : [];
					for(var i=0;i<arr3.length;i++){
						arr3[i].ber=$(".btn2").eq(i).val();
					}
					$.cookie(log+"_cart",JSON.stringify(arr3),{expires:7,path:'/'});
				}

				// 封装cookie总价格
				function CC(){
					var log = $.cookie("log")
					var arr3 = $.cookie(log+"_cart") ? JSON.parse( $.cookie(log+"_cart") ) : [];
					var numbe = 0;
					var price = 0;

					for(var i=0;i<arr3.length;i++){
						if($(".imp").eq(i).prop("checked")){
							numbe+=parseInt($(".btn2").eq(i).val());
						    price+=parseFloat($(".sp4").eq(i).text().slice(1))
						}

					};
					$("#check_acount").html(numbe)
					//总价
                    $("#check_allacount").html("￥"+price.toFixed(2))
                    $("#PRI").html("￥"+price.toFixed(2))
					$("#NUM").html(numbe);
					document.getElementById('total_price').value = price.toFixed(2)
				}

				//  在删完商品后对页面进行隐藏
				$(".caozuo a").click(function(){
					var log = $.cookie("log")
					var index = $(this).parents("ul").index();
					var arr2 = JSON.parse($.cookie(log+"_cart"));
					arr2.splice(index,1);
					$.cookie(log+"_cart",JSON.stringify(arr2),{expires:7,path:'/'});
					$(this).parents("ul").remove();
					if($(".tttt").find("li").length==0){
						$(".car-info").hide()
					}else{
						$(".car-info").show()
					}
					CC();

				})
				//在页面加载的时候  没有商品进行隐藏
				if($(".tttt").find("li").length==0){
						$(".car-info").hide()
					}else{
						$(".car-info").show()
					}

				// 刷新页面的价格 商品个数
				CC();

				// 判断是否登录
				if($.cookie("log")){
					var user = $.cookie("log")
					$("<div>").css({
						"width":"120px",
						"height":"24px",
						"position":"absolute",
						"left":"500px",
						"top":"0px",
						"font-size":"13px",
						"line-height":"24px",
						"margin-top":"1px"
					}).attr("class","use").html("您好：").appendTo("body")

					$("<p>").css({
						"width":"70px",
						"height":"24px",
						"float":"left",
						"color":"blue"
					}).html(user).appendTo(".use")

					$(".Navright li").eq(0).find("a").hide()
					$("<a/>").html("退出").attr("id","exit").css({
      		           "color":"blue"
     	            }).appendTo($(".Navright li").eq(0))

     	           $("#exit").click(function(){
		        		$(".Navright li").eq(0).find("a").show();
		        		$(this).hide()
		        		$.cookie("log","",{expires:30, path:"/"})
		        		$(".use").html("")
		        		window.location.reload();
	        	    })

		        	$("#exit").mouseenter(function(){
		        		$(this).css({
		        			"color":"red"
		        		})
		        	})

		        	$("#exit").mouseleave(function(){
		        		$(this).css({
		        			"color":"blue"
		        		})
		        	})
			 }


		})