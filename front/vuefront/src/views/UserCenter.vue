<template>
	<div class="username">
		用户中心
		<div v-if="userinfo">
			<div>
				<h2>修改信息</h2>
				<van-field v-model="userinfo.username" type="tel" label="用户名" />
				<van-field v-model="userinfo.telephone" type="tel" label="手机号" />
				<van-field v-model="userinfo.password" type="password" label="密码" />
				<van-field v-model="userinfo.email" type="email" label="邮箱" />
				<van-button @click="modify" round block type="info" native-type="submit">
			      	修改信息
			    </van-button>
			</div>
		</div>
		
	</div>
	
</template>

<script>
	export default{
		methods:{
			modify(){
				this.$api.modifyUserInfo({
					userinfo:this.userinfo,
				}).then(res=>{
					console.log("更改成功",res)
				}).catch(err=>{
					console.log("更改失败",err)
				})
			}
		},
		data(){
			return{
				userinfo:null,
//				tel: '',
//				password:'',
//				email:'',
			}
		},
		created(){
			this.$api.getUserinfo().then(res=>{
				console.log("个人信息",res);
				this.userinfo=res.data;
				this.$jsCookie.set("userinfo",res.data)
			}).catch(err=>{
				console.log("出错了");
			})
		},
		filters:{
			dataFormat(date){
				date=new Date(date);
				return `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`
			}
		}
	}
	
</script>

<style>
</style>