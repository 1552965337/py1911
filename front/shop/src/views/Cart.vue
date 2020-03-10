<template>
	<div class="cart">
		<vueToTop :type='2' :size='30' :bottom='50'style="z-index: 10;"></vueToTop>
		<van-sticky >
		<van-nav-bar
		class="header"
		title="购物车"
		left-arrow
		@click-left="onClickLeft"
		@click-right="onClickRight"
		>
		<van-icon name="search" slot="right" />
		</van-nav-bar>
		</van-sticky >
		<div v-if="value">
			<van-cell title="登录后享受更多优惠" is-link value="去登录" to="/mine"/>
		</div>
		<div class="mg" style="text-align: center;font-size: 15px;" v-show="flag">
			<img src="img/0.png" alt="" style="width: 127px;height: 98px;">
			<p>购物车内暂时没有商品</p>
			<p style="border-radius:10px;width:60px;height:20 ;background-color: rgb(255,115,76);margin-left: 155px;" @click="$router.push('/')">去逛逛</p>
		</div>
		<div>
			<van-card v-for="(item,index) in $store.getters.getGoodList "
			  :num="item.num"
			  :price="item.data.Price"
			  :origin-price="item.data.LinePrice"
			  :title="'商品名:  '+item.data.Cpmc"
			  :thumb="item.data.img"
			>
			<van-stepper @change="change(index,item.num)" min="0" v-model="item.num"  slot="bottom"/>
			<div slot="footer">
			    <van-button size="mini" @click="del2(index)" color="linear-gradient(to right, #4bb0ff, #6149f6)">移除</van-button>
			  </div>
			</van-card>
		</div>
		<!-- 卖家推荐 -->
		<div style="margin-left: 10px;"><p style="color: #F16969; font-size: 25px;">推荐</p></div>
		<div class="recommend" style="text-align: center;">
			<!-- <img src="img/13.png" alt="" style="width:95%;"> -->
			<div class='recom1' v-for="item1 in hot" @click="det1(item1.ItemCode)" style="text-align: left;">
				<van-card
				  :num="item1.Sales"
				  tag="Hot"
				  :price="item1.Price"
				  :desc="item1.Instro"
				  :title="item1.Cpmc"
				  :thumb=item1.img
				  :origin-price="item1.LinePrice"
				/>
			</div>
			<div style="margin-left: 65px;">
				<van-loading size="24px" type="spinner" color="#1989fa" >加载中...</van-loading>
				<br>
				<br>
				<br>
			</div>
		</div>
		<van-submit-bar
		  :price="money"
		  button-text="提交订单"
		  @submit="onSubmit"
		>
		 <span class="s1" @click="del()" style="width: 40px;height: 20px;background-color: green;border-radius: 10px;color: white;text-align: center;">清空</span>
		</van-submit-bar>
	</div>
</template>
	
<script>
	import {dictA} from '../data.js'
	import Cookie from 'js-cookie'
	export default{
		
		data(){
			return{
				value:true,
				flag:true,
				money:"",
				dict:null,
				hot:[],
			}
		},
		created() {
			this.dict=dictA,
			this.moneys();
			this.disap();
			this.hots();
			if( Cookie.get("islog")){this.value=false;}
		},
		methods:{
			det1(index){
				this.$router.push("/Detail/"+index)
				},
				
			// 推荐
			hots(){
				for(let i=0;i<8;i++){
					this.hot.push(this.dict[ parseInt(Math.random()*this.dict.length)])
				}
			},
			
			// 显示与消失
			disap(){
				if(this.$store.getters.getGoodList.length>0){
					this.flag=false
				}
				else{
					this.flag=true
				}
			},
			
			del(){
				this.$toast('清空成功'); 
				// this.$store.getters.getGoodList=[];
				this.$store.commit("changeRemove");
				this.money=0;
				this.disap();
				},
			del2(index){
				if( Cookie.get("islog")){}
				this.$toast('移除成功'); 
				this.$store.commit("changeRemoveOne",index);
				this.disap();
				this.moneys()
				},
			onSubmit(){
				if( Cookie.get("islog")){
					this.$toast("提交成功");
					this.money=0;
					this.$store.getters.getGoodList.forEach(item=>{
						this.$store.commit("addMy",item);
					})
					
					this.$store.commit("changeRemove");
					this.disap();
				}
				else{
					this.$router.push("/mine")
				}
			},
			moneys(){
				let qian=0;
				this.$store.getters.getGoodList.forEach(item=>{
					qian+=item.data.Price*item.num
				})
				this.money=qian*100
			},
			change(index,num){
				// console.log(num,index);
				this.$store.commit("changeGoodNum",[index,num]);
				this.moneys();
				this.disap();
				
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
