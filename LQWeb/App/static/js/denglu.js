$(function(){

				$("#username").focus(function(){
					$(".tishi").hide();
					$(".itemd").show();
				})

				//点击登录按钮
				$("#denglu").click(function(){
					$.get("/app/userdata/", function (response) {
							users = response.data;
					if (users) {
						//遍历查找是否有匹配的用户
						var isExist = false; //表示是否存在该用户
						for (var i=0; i<users.length; i++) {
							if ( $("#username").val() == users[i].name && $("#pass").val() == users[i].psd ) {
								console.log('h')
								isExist = true; //表示存在该用户
					            $.cookie("log",users[i].name,{expires:30, path:"/"})
					            location.href="/app/index?"+users[i].name;
							}
						}

						if (!isExist) {
							$(".tishi").show();
							$(".tishi").html("用户名或密码错误")
							return;
						}

					}

				})
				})
			})