<template>
	<div class="cart">
		<vueToTop :type='2' :size='30' :bottom='50'style="z-index: 10;"></vueToTop>
		<van-sticky >
		<van-nav-bar
		class="header"
		title="全部订单"
		left-arrow
		@click-left="onClickLeft"
		@click-right="onClickRight"
		>
		<van-icon name="search" slot="right" />
		</van-nav-bar>
		</van-sticky >
		<div class="mg" style="text-align: center;font-size: 15px;" v-show="flag">
			<img src="img/0.png" alt="" style="width: 127px;height: 98px;">
			<p>暂时购买记录</p>
			<p style="border-radius:10px;width:60px;height:20 ;background-color: rgb(255,115,76);margin-left: 155px;" @click="$router.push('/')">去逛逛</p>
		</div>
		<div v-for="(item,index) in list">
			<van-card 
			  :num="item.num"
			  :price="item.data.Price"
			  :origin-price="item.data.LinePrice"
			  :title="'商品名:  '+item.data.Cpmc"
			  :thumb="item.data.img"
			>
			</van-card>
		</div>
	</div>
</template>
	
<script>
	import {dictA} from '../data.js'
	export default{
		
		data(){
			return{
				flag:true,
				money:"",
				dict:null,
				list:[],
			}
		},
		created() {
			this.dict=dictA,
			this.list=this.$store.getters.myTatalList,
			this.disap();
		},
		methods:{
			// 显示与消失
			disap(){
				if(this.$store.getters.myTatalList.length>0){
					this.flag=false
				}
				else{
					this.flag=true
				}
			},
			
			onClickLeft() {
			  this.$router.go(-1);
			},
			onClickRight() {
			  this.$router.push("/search")
			}
		}
	}
</script>

<style scoped="scoped" lang="less">
	.cart{
		text-align: left;
		.header{
		}
		.recommend{
			width: 375px;
			display: flex;
			flex-wrap: wrap;
			justify-content: center;
			.recom1{
			// border:1px red solid;
			width: 175px;
			height: 130px;
		}
		}
	}
</style>
