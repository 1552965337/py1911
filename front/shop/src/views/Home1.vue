<template>
	<div class="header">
		<div v-for='(item,index) in dictB' class="div1" @click="det1(item.id)">
			<img :src='dictB[index].img'style="width: 355px; height:323px ;margin-bottom: 5px;">
			<van-card
			  :num="dictB[index].num"
			  tag="恋人"
			  :price="dictB[index].price"
			  :desc="dictB[index].desc"
			  :title="dictB[index].name"
			  :thumb=dictB[index].img
			  :origin-price="dictB[index].historyprice"
			/>
			  <div slot="footer">
				  <van-button color="linear-gradient(to right, #D17070, #73B3CF)" size="large">立即抢购</van-button>
			  </div>
			</van-card>
		</div>
		<div style="padding-left: 30px;">
			<van-loading size="24px" type="spinner" color="#1989fa" >加载中...</van-loading>
		</div>
		<br>
		<br>
	</div>
</template>

<script>
//	import {dictBs} from '../data.js'
	export default{
		data(){return{

				dictB:null,
			}
		},
		created(){
			this.requestProductList()
//			this.dictB=dictBs
		},
		methods:{
			requestProductList(){
				this.$api.getProduct().then(res=>{
					console.log("首页产品",res)
					this.dictB=res.data
				}).catch(err=>{
					console.log("错误",err)
				})
			},
			det1(index){
				this.$router.push("/Detail/"+index)}
			},
		
	}
</script>

<style scoped="scoped" lang="less">
	.header{
		width:375px;
		display: flex;
		flex-wrap: wrap;
		justify-content:center ;
		.div1{
			width: 100%;
			height: 500px;
			margin-bottom: 20px;
		}
	}
</style>
