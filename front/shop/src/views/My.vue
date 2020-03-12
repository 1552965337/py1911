<template>
	<div class="cart">
		<vueToTop :type='2' :size='30' :bottom='50'style="z-index: 10;"></vueToTop>
		<van-sticky >
		<van-nav-bar
		class="header"
		title="我的订单"
		left-arrow
		@click-left="onClickLeft"
		@click-right="onClickRight"
		>
		<van-icon name="search" slot="right" />
		</van-nav-bar>
		</van-sticky >
		<div class="mg" style="text-align: center;font-size: 15px;" v-show="flag">
			<img src="img/0.png" alt="" style="width: 127px;height: 98px;">
			<p>暂时没有购买商品</p>
			<p style="border-radius:10px;width:60px;height:20 ;background-color: rgb(255,115,76);margin-left: 155px;" @click="$router.push('/')">去逛逛</p>
		</div>
		<div v-for="(item,index) in list">
			<van-card 
			  :num="item.num"
			  :price="item.data.price"
			  :origin-price="item.data.historyprice"
			  :title="'商品名:  '+item.data.name"
			  :thumb="item.data.imgs[0].img"
			>
			<div slot="footer">
			    <van-button size="mini" color="linear-gradient(to right, #4bb0ff, #6149f6)" @click="shou(item,index)">签收</van-button>
			</div>
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
			this.list=this.$store.getters.myGoodList
			this.disap();
		},
		methods:{
			shou(task,indexs){
				this.$toast("收货成功"),
				this.$store.commit("addTotal",task),
				this.$store.getters.myGoodList.splice(indexs,1)
				
			},
			// 显示与消失
			disap(){
				if(this.$store.getters.myGoodList.length>0){
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
