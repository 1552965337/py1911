<template>
  <div class="mine">
	  <vueToTop :type='2' :size='30' :bottom='50'style="z-index: 10;"></vueToTop>
    <div class="header">
		<van-sticky >
		<van-nav-bar
		  id="searchdiv"
		  title="标题"
		  left-arrow
		  @click-left="onClickLeft"
		  @click-right="onClickRight"
		>
		
		<input v-model="value" id="searchinput" slot="title" placeholder="请输入搜索内容" />
		
		<van-icon name="search" slot="right" />
		</van-nav-bar>
		</van-sticky >
	</div>
	
	<div class="other">
		<p>历史搜索<span style="margin-right:10px;float: right;"@click="del">清除</span></p>
		<div class="searchhot">
			
			<van-tag style="margin: 5px;" class='searchitem' @click="searchHot(item)" v-for="item in searchHistory" :type="colors[ parseInt(Math.random()*colors.length)  ]">{{item}}</van-tag>
		</div>
		
		<p>热门搜索</p>
		<img src="img/13.png" alt="" style="width:95%;">
		
		<div class="searchhot1" >
			<div class='search1' v-for="item1 in hot" @click="det1(item1.ItemCode)"style="text-align: left;">
				<van-card
				  :num="item1.Sales"
				  tag="特价"
				  :price="item1.Price"
				  :desc="item1.Instro"
				  :title="item1.Cpmc"
				  :thumb=item1.img
				  :origin-price="item1.LinePrice"
				/>
			</div>
			<div style="margin-left: 65px;">
				<van-loading size="24px" type="spinner" color="#1989fa" >加载中...</van-loading>
			</div>
		</div>
		
		
	
	</div>
  </div>
</template>
<style scoped="scoped" lang="less">
	.mine{
		width: 375px;
		
	.header{
		
		#searchdiv{
			background-color: #f2f2f2;
		}
		#searchinput{
			height: 30px;
			line-height: 30px;
			border: none;
		}
	}
	.other{
		img{
			width: 100%;
		}
		.searchhot{
			display: flex;
			flex-wrap: wrap;
			justify-content:center;
			padding: 5px;
			.searchitem{
				padding: 10px;
			}
		}
		.searchhot1{
			width: 375px;
			display: flex;
			flex-wrap: wrap;
			justify-content: center;
			.search1{
				border:1px #F06431 solid;
				width: 178px;
				height: 130px;
				
			}
		}
	}
	}
</style>
<script>
	import {dictA} from '../data.js'
	export default {
		data(){
			return{
				value:"",
				colors:["primary","success","danger","warning"],
				historySearch: JSON.parse(localStorage.getItem("historySearch"))||[],
				hot:[],
				dict:null
			}
		},
		created(){
			
			this.dict=dictA,
			this.hots()
		},
		computed:{
			searchHistory(){
				// let now = localStorage.getItem("historySearch");
				return this.historySearch
			}
		},
	  methods: {
		  del(){
			  this.historySearch=[];
			  localStorage.removeItem("historySearch")
		  },
	    onClickLeft() {
	      // this.$toast('返回');
		  this.$router.go(-1)
	    },
	    onClickRight() {
			if(this.value.length<=0){
				this.$toast("请输入搜索内容")
			}
			else{
				this.$toast(`搜索了${this.value}`);
				this.historySearch.unshift(this.value);
				console.log(this.historySearch);
				localStorage.setItem("historySearch",JSON.stringify(this.historySearch))
			}
	      
		  // 需要请求服务器对应的搜索接口
	    },
		searchHot(item){
			this.$toast(`搜索了${item}`);
		},
		hots(){
			for(let i=0;i<8;i++){
				this.hot.push(this.dict[ parseInt(Math.random()*this.dict.length)])
			}
		},
		det1(index){
			this.$router.push("/Detail/"+index)
			}
		
	  }
	}
</script>