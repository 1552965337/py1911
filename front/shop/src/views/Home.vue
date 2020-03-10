<template>
  <div class="home">
	  <vueToTop :type='2' :size='30' :bottom='50'style="z-index: 10;"></vueToTop>
	  <van-sticky >
	  <van-nav-bar
	  class="header"
	  @click-left="onClickLeft"
	  @click-right="onClickRight"
	  >
	  <van-icon name="coupon-o" size='25px' slot="left" color= "white" />
	  <img src="img/m_hualogo.png" slot='title' alt="" style="width: 150px; height: 20px; margin-top: 11px;">
	  <van-icon name="service-o" size='25px' slot="right" color="white"/>
	  </van-nav-bar>
	  </van-sticky >
	  <!-- 轮播图 -->
	  <van-swipe :autoplay="3000" indicator-color="white">
	    <van-swipe-item v-for="(item, index) in images" :key="index">
			<img :src="item.img" alt="" style="width: 100%;">
		</van-swipe-item>
	  </van-swipe>
	 
	 
	 <div class="box1" style="padding: 10px;">
		 <div class="bov1_a" style="margin-right: 8px; font-size: 12.5px;width: 100%; height: 36px;display: flex;flex-wrap:nowrap;justify-content:space-between;">
			 <div><van-icon name="checked" />认证龙头企业</div>
			 <div><van-icon name="checked" />14年品牌</div>
			 <div><van-icon name="checked" />3小时送花</div>
			 <div><van-icon name="checked" />质量保证</div>
		 </div>
		 <div class="box2" style="display: flex;flex-wrap:nowrap;justify-content:space-between;">
			 <div class="box2-a"  v-for="(item,index) in list" :key="index" @click="gate(index)">
				 <img :src="item.imga" alt="" style="width: 36px;height: 36px;">
				 <p style="font-size: 12.5px;margin-top: -5px;">{{item.name}}</p>
			 </div>
		 </div>
		 <div style="margin-right: 250px;font-size: 20px;color: skyblue;">
			 一秒选花:
		 </div>
		 <div class="box3">
			 <div class="box3-a" v-for="(item1,index) in list2"  :key1="index" @click="home1(index)">
				 <img :src="item1.img" alt="" style="width: 117px; height: 130px;">
				 <p>{{item1.name}}</p>
			 </div>
		 </div>
		 <p style="margin-top:40px ; color: fuchsia;">送恋人/送鲜花</p>
		 <div >
			 <Home1></Home1>
		 </div>
		 
	 </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import Home1 from '@/views/Home1.vue'

export default {
  name: 'home',
  components: {
    // HelloWorld
	Home1,
  },
  data(){
	  return{
		  images:null,
			list:[
				{imga:"img/5.png",name:"鲜花"},
				{imga:"img/6.png",name:"永生花"},
				{imga:"img/7.png",name:"蛋糕"},
				{imga:"img/8.png",name:"礼品"},
				{imga:"img/9.png",name:"巧克力"}
			],
			list2:[
				{img:"img/10.png",name:"新品来袭"},
				{img:"img/11.png",name:"品味之选"},
				{img:"img/12.png",name:"设计师臻选"},
			]
	  }
	  
  },
	created(){
		this.requestAdsList();
	},
  methods:{
	  requestAdsList(){
				this.$api.getAds().then(res=>{
					console.log("轮播图",res)
					this.images=res.data
				}).catch(err=>{
					console.log("出错",err)
				})
			},
	  onClickLeft() {
	    this.$router.push("/search")
	  },
	  onClickRight() {
	    // this.$router.push("/search")
	  },
	
	  gate(task){
		  this.$router.push("/Category/"+task)
		  },
	  home1(task){
		  this.$router.push("/Category/"+task)
	  }
	
  }
}
</script>

<style scoped="scoped" lang="less">
	*{box-sizing:border-box;}
	
	.home{
		// height: 2000px;
		width: 100%;
		.header{
			// margin: 0;
			background-color: rgb(67,84,72);
			width: 100%;
			display: flex;
			line-height: 44px;
			height: 44px;
			
		}
		.box3{
			width: 100%; 
			height: 130px;
			// padding: 3px;
			display: flex;
			flex-wrap:nowrap;
			justify-content:space-between;
			.box3-a{
				width: 117px;
				height: 130px;
				p{
				display: inline-block;
				margin-right: 2px;
				margin-top: -30px;
				font-size: 12.5px;
				width: 117px;
				height: 25px;
				line-height: 25px;
				color: white;
				background-color: rgb(76,79,83);
				
			}
			}
			
		}
	}
	
</style>