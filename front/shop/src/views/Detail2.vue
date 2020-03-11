<template>
	<div class="detail1" v-if="data">	
	<vueToTop :type='2' :size='30' :bottom='50'style="z-index: 10;"></vueToTop>
		<div class="header">
			<van-sticky >
			<van-nav-bar
			title="详情"
			left-arrow
			@click-left="onClickLeft"
			/>
			</van-sticky >
		</div>
		<div class="imb">
			<img :src="data.img" alt=""/>
		</div>
		<div style="color:red;font-size: 27px;">{{data.name}}</div>
		<div style="background-color: #F0C674;margin: 10px;">
			<div style="text-align: left; margin-left: 10px;">
				<p><b>材料：{{data.desc}}</b></p>
				<p><b>配送范围：</b>全国</p>
			</div>
			<div style="text-align: left; margin-left: 10px;">
				<p><b>原价：{{data.historyprice}}元</b><del></del> </p>
				<span><b>到手价：{{data.price}}元</b><b style="color: #FF0000;"></b></span>
				<p>月销售：{{data.num}}件</p>
				<p><b>购买数量：</b>   <span><van-stepper v-model="buyNum"  style="display: inline-block;"/></span></p>
			</div>
			
			<div>
				<van-button @click='choose()' v-if='!flag'  size="small"  color="linear-gradient(to right, #4bb0ff, #6149f6)" style='width: 100%; height: 35px;'>点击选择地址</van-button>
				<van-address-edit
				v-show="flag"
			    :area-list="areaList"
			    show-postal
			    show-delete
			    show-set-default
			    show-search-result
			    :search-result="searchResult"
			    :area-columns-placeholder="['请选择', '请选择', '请选择']"
			    @save="onSave"
			    @delete="onDelete"
			    @change-detail="onChangeDetail"
			   />
			</div>
			
			<div style="text-align: left; margin-left: 10px;"><b >订单评价</b> <span class="sp2"> 最近已有10175条评价<van-icon name="arrow"/></span></div>
		</div>
		<div style="text-align: center;width: 95%;margin: 10px;">
			<div class="pp"><img src="img/14.jpg" alt="" style="width:100%;height: 300px;"></div>
			<div class="pp"><img src="img/15.jpg" alt="" style="width:100%;height: 300px;"></div>
			<div class="pp"><img src="img/16.jpg" alt="" style="width:100%;height: 300px;"></div>
			<div class="pp"><img src="img/17.jpg" alt="" style="width:100%;height: 300px;"></div>
		</div>
		<div>
			<van-goods-action>
			  <van-goods-action-icon icon="home-o" text="首页" @click="goToHome"/>
			  <van-goods-action-icon icon="chat-o" text="客服" :info="12"/>
			  <van-goods-action-icon icon="cart-o" type="warning"  @click="$router.push('/cart')" text="购物车" :info="$store.getters.getGoodList.length" />
			  <van-goods-action-button type="danger" text="加入购物车" @click="addCart"/>
			</van-goods-action>
		</div>
		
		<br>
		<br>
		<br>
	</div>
	
	
</template>

<script>
	export default {
		data(){
			return{
				data:null,
				flag:false,
				buyNum:1,
				areaList:{
						province_list: {
						  110000: '北京市',
						  120000: '河南'
						},
						city_list: {
						  110100: '北京市',
						  120100: '郑州市',
						  120200: '濮阳市'
						},
						county_list: {
						  110101: '东城区',
						  110102: '西城区',
						  110103: '昌平区',
						  110104: '海淀区',
						  110105: '朝阳区',
						  110106: '丰台区',
						  120101: '金水区',
						  120102: '惠济区',
						  120103: '二七区',
						  120104: '经开区',
						  120201: '华龙区',
						  120202: '老城区',
						  120202: '新城区',
						  
						  // ....
					}
				},
				searchResult: []
			}
		},
		created(){
			
			this.requestGood();
		},
	  methods: {
		  // 点击选择地址
		  choose(){this.flag=!this.flag},
		  // 保存地址
		  onSave() {
			this.$toast('保存成功');
			this.flag=false
		  },
		  onDelete() {
			this.$toast('删除成功');
			this.flag=false
		  },
		  onChangeDetail(val) {
			if (val) {
			  this.searchResult = [{
				name: '黄龙万科中心',
				address: '杭州市西湖区'
			  }];
			} else {
			  this.searchResult = [];
			}
		  },
		  
		  goToHome(){
		  		this.$router.push("/")
		  	},
		  	addCart(){
		  		// this.show=false;
		  		this.$toast("加入成功");
		  		this.$store.commit("addGood",{id:this.$route.params.id,num:this.buyNum,data:this.data})
		  	},
		requestGood(){
			this.$api.getGoodList().then(res=>{
				console.log("获取good成功",res)
				res.data.forEach(item=>{
					if(item.name==this.$route.params.id){
						this.data=item
					}
				})
			}).catch(err=>{
				console.log("获取good失败",err)
			})
		
		},
	    onClickLeft(){
	      this.$router.go(-1)
	    },
	  }
	}
</script>

<style>
	.imb{img{width: 100%;}color: #E5E5E5;}
	.pp{width:100%;height: 300px; background-color: white;margin-bottom: 10px;}
</style>
