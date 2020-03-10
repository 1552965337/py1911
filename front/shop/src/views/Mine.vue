<template>
	<div class="mine">
	
		<van-tabs v-model="active">
			<van-tab title="登录">
		<div class="login">
			<p>用户登录</p>
			 <van-cell-group>
			  <van-field
				v-model="loginusername"
				required
				clearable
				label="用户名"
				placeholder="请输入用户名"
			  />
			
			  <van-field
				v-model="loginpassword"
				type="password"
				label="密码"
				placeholder="请输入密码"
				required
			  />
			</van-cell-group>
			<van-button @click="login" type="primary">登录</van-button>
		</div>
		</van-tab>
		<van-tab title="注册">
		<div class="regist">
			<p>用户注册</p>
			 <van-cell-group>
			  <van-field
				v-model="username"
				required
				clearable
				label="用户名"
				placeholder="请输入用户名"
			  />
			
			  <van-field
				v-model="password"
				type="password"
				label="密码"
				placeholder="请输入密码"
				required
			  />
			  <van-field
				v-model="password2"
				type="password"
				label="密码"
				placeholder="请再次输入密码"
				required
			  />
			  <van-field
				v-model="email"
				type="email"
				label="邮箱"
				placeholder="请输入邮箱"
				required
			  />
			</van-cell-group>
			
			<van-button @click="regist" type="primary">注册</van-button>
		</div>
		</van-tab>
		</van-tabs>
		<!-- </div> -->
	</div>
</template>

<script>
	import Cookie from 'js-cookie'
	// import Personal from '@/views/Personal.vue'
	
	export default{
		// components: {
		// 	Personal,
		// 	},
		data(){
			return{
				username:"werwer",
				password:"1234567",
				password2:"1234567",
				email:"1234@qq.com",
				loginusername:"",
				loginpassword:"",
				userinfo:null,
				active:0
			}
		},
		created() {
			this.initUser();
		},
		methods:{
			initUser(){
				// this.$http({
				// 	url:`http://www.520mg.com/member/ajax_login.php`,
				// 	method:"get",
				// 	// 强制上传cookie信息
				// 	withCredentials:true
					
				// }).then(res=>{
				// 	console.log(res.data);
						
					this.userinfo = {
					}
				// })
			},
			
			login(){
				if(this.loginusername.length<=0||this.loginpassword.length<=0){
					this.$toast("必填项目不能为空");
					}
				else{
					// this.$http({
					// 	url:`http://www.520mg.com/member/index_login.php?fmdo=login&dopost=login&userid=${this.loginusername}&pwd=${this.loginpassword}`,
					// 	method:"post",
					// 	withCredentials:true
					// }).then(res=>{
					// 	if(res.data.status==1){
							this.$toast("登录成功");
							Cookie.set("islog",true,{expires:7});
							this.initUser();
							// localStorage.setItem('key','999')
							this.$router.push('/personal')
					// 	}
					// 	else{
					// 		this.$toast(res.data.msg)
					// 	}
					// })
				}
			},
			regist(){
				if(this.username.length<=0||this.password.length<=0||this.password2.length<=0||this.email.length<=0){
					this.$toast("必填项目不能为空");
					}
				else if(this.password!=this.password2){
					this.$toast("密码必须一致");
				}
				else{
					// this.$http({
					// 	url:`http://www.520mg.com/member/reg_new2.php?userid=${this.username}&userpwd=${this.password}&email=${this.email}`,
					// 	method:"post",
					// }).then(res=>{
					// 	if(res.data.status==1){
							this.$toast("注册成功")
					// 	}
					// 	else{
					// 		this.$toast(res.data.msg)
					// 	}
					// }).catch(err=>{
					// 	console.log("请求出错",err);
					// })
				}
			}
		}
	}
</script>

<style>
</style>
