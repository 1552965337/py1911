<template>
	<div class="personal">
		<van-sticky >
		<van-nav-bar
		  title="个人中心"
		  left-arrow
		  @click-left="onClickLeft"
		/>
		</van-sticky >
		<div class="header">
			<img class="img1" src="img3/1.png" alt="" >
			<div class="box1" v-show="value==null">
				<b class="box1-a" >Hi,欢迎来到花礼网</b>
				<van-button type="warning" plain size="small"  style='margin-top: 8px;color:rgb(65,168,99);' @click="login"><b>登录/注册</b></van-button>
				<!-- <van-button  plain size="small"   style='margin-top: 8px;'><b></b></van-button></span> -->
			</div>
			
			
			<div class="head" v-show="value!=null" v-if="value">
				<img :src="value.M_Face?value.M_Face:'img2/'+parseInt(Math.random()*34)+'.jpg'" alt="" >
				<div style="margin-top: 20px;" >
					<p style="color: rgb(65,168,99) ; margin-left: 23%;"><b>{{value.M_UserName}}</b></p>
					<p style="color: rgb(65,168,99);margin-left: 25%;height: 15px;width: 40px;;"  @click="loginout"><b>注销</b></p>
				</div>
			</div>
		</div>
		
		
		<div class="body">
			<div style="width: 100%;background-color: firebrick;">
				<van-nav-bar
				   left-text="我的订单"
				   right-text="全部订单"
				   @click-left="my()"
				   @click-right="total()"
			   />
			</div>
			
			<div class="body-2" style="display: flex;">
				<div class="body-a">
					<img src="img3/2.png" alt="">
					<span>待付款</span>
				</div>
				
				<div class="body-a b">
					<img src="img3/3.png" alt="">
					<span>待收货</span>
				</div>
				
				<div class="body-a">
					<img src="img3/4.png" alt="">
					<span>待评价</span>
				</div>
			</div>
		</div>
		
		<div class="body body-b">
			<div class="body-c">
				<van-icon name="balance-pay" size='15px'/>
				<span>优惠卡</span>
			</div>
			<div class="body-c">
				<van-icon name="vip-card-o" size='15px' />
				<span>权益卡</span>
			</div>
			<div class="body-c">
				<van-icon name="after-sale" size='15px' />
				<span>余额</span>
			</div>
			<div class="body-c">
				<van-icon name="gem-o" size='15px' />
				<span>会员积分</span>
			</div>
			<div class="body-c">
				<van-icon name="location-o" size='15px' />
				<span>收货地址</span>
			</div>
			<div class="body-c">
				<van-icon name="clock-o"  size='15px'/>
				<span>生日提醒</span>
			</div>
			<div class="body-c">
				<van-icon name="star-o"  size='15px'/>
				<span>我的收藏</span>
			</div>
			<div class="body-c">
				<van-icon name="todo-list-o"  size='15px'/>
				<span>浏览记录</span>
			</div>
		</div>
	</div>
</template>

<script>
	import Cookie from 'js-cookie'
	export default{
		data(){
			return{
				value:null,
				
			}
		},
		created() {
			let haslog = Cookie.get("islog");
			if(haslog){
				// this.$http({
				// 	url:`http://www.520mg.com/member/ajax_login.php`,
				// 	method:"get",
				// 	// 强制上传cookie信息
				// 	withCredentials:true
					
				// }).then(res=>{
					// console.log(res.data);
					this.value = {
						M_Face:"",
						M_UserName:"1234567"
					}
				// })
			}
		},
		methods:{
			// 跳转至我的订单页面
			my(){
				if(Cookie.get("islog")){
					this.$router.push("/my")
				}
				else{
					this.$router.push("/mine");
				}
			},
			total(){
				if(Cookie.get("islog")){
					this.$router.push("/total")
				}
				else{
					this.$router.push("/mine");
				}
			},
			onClickLeft() {
			  this.$router.go(-1);
			},
			
			// 登录
			login(){
				
				this.$router.push("/mine");
				// this.value=true
			},
			// 注销
			loginout(){
				// this.$http({
				// 	url:`http://www.520mg.com/member/index_login.php?dopost=exit`,
				// 	method:'post',
				// 	withCredentials:true
				// }).then(res=>{
				// 	if(res.data.status==1){
						this.$toast("退出成功");
						this.value=null;
						Cookie.remove("islog")
				// 	}
				// 	else{
				// 		this.$toast("退出失败");
				// 	}
				// })
			},
		}
	}
</script>

<style scoped="scoped" lang="less">
	*{margin: 0;padding: 0;}
	.personal{
		.header{
			
			width: 100%;
			.img1{
				width: 95%;
			}
			.box1{margin: 0 auto;
			 position: absolute; 
			 top:85px; left:32% ;
			 .box1-a{display:block;color: white;}
			 }
			 .head{
				 display: flex; position: absolute;top: 65px; left: 20px;
				 img{
					 border-radius: 50%; width: 20%;height: 20%; border: #ED6A0C solid 3px;
				 }
				 .b{margin: 0 ;}
			 }
		}
		.body{
			background-color: #F0C674; margin: 5px 5px; 
			border-radius: 6px;
			padding: 5px;
			.body-2{
				background-color: white;
				.body-a{margin: 0 auto; 
					img{width: 30%;} 
					span{display:block; font-size: 8px;} 
				}
			}
		}
		.body-b{
		  display: flex;
		  flex-wrap: wrap;
		  margin: 5px 5px;
		  padding: 5px;
		  }
		.body-c{
			width:25% ;
			 margin: 15px 0px; 
			 font-size:2px;  
			span{display: block;}
		}
	}
</style>
