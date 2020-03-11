<template>
  <div class="category">
	<van-sticky >
    <van-nav-bar
    class="header"
    title="分类"
    left-arrow
    @click-left="onClickLeft"
    @click-right="onClickRight"
    >
    <van-icon name="search" slot="right" />
    </van-nav-bar>
	</van-sticky>
		<div class="main">
			<div class="left" >
				<van-sidebar @change="onChange" v-model="activeKey">
				  <van-sidebar-item v-for="(item,index) in list" :key="index" :title="item.name"/>
				</van-sidebar>
			</div>
			<div class="right" ref="right">
				<div  v-for="(item1,index) in list[activeKey].goods" @click="det1(item1.name)">
					<van-card
					  :num="item1.num"
					  tag="特价"
					  :price="item1.price"
					  :desc="item1.desc"
					  :title="item1.name"
					  :thumb=item1.imgs[0].img
					  :origin-price="item1.historyprice"
					/>
					<van-divider :style="{borderColor: '#1989fa', padding: '0 16px' }"/>
				</div>
				
				<div style="">
					<van-loading size="24px" type="spinner" color="#1989fa" >加载中...</van-loading>
				</div>
			</div>
		</div>
  </div>
</template>

<script>
	export default{
		data(){
			return{
				activeKey:0,
				list:null,
			}
		},
		created(){
			this.activeKey=this.$route.params.id;
			this.requestCatory();
		},
		methods:{
			det1(code){
				this.$router.push("/detail2/"+code)
				
			},
			
			onChange(index) {
			     // 在左侧点击时需要控制右侧滚动条位置
							// 通过$refs  找到需要控制的dom元素  控制元素的滚动条到顶部
				this.$refs.right.scrollTo(0,0);
			   },
			onClickLeft() {
			  this.$router.go(-1);
			},
			onClickRight() {
			  this.$router.push("/search")
			},
			
			requestCatory(){
				this.$api.getCategory().then(res=>{
					console.log("获取分类成功",res)
					this.list=res.data
					console.log(this.activeKey)
				}).catch(err=>{
					console.log("获取分类失败",err)
				})
			}
		},
		
	}
</script>
<style scoped="scoped" lang="less">
	.category{
		.header{
			background-color: rgb(242,242,242);
			line-height: 50px;
			height: 50px;
		}
		.main{
			display: flex;
			position: absolute;
			left:0;
			top:50px;
			right: 0px;
			bottom: 50px;
			.left{
				overflow-y: auto;
				width: 25%;
			}
			// webkit内核浏览器控制滚动条不显示
			.left::-webkit-scrollbar{
				display:none ;
			}
			.right::-webkit-scrollbar{
				display:none ;
			}
			.right{
				overflow-y: auto;
				width: 75%;
				background-color: rgb(240,240,240);
				}
			}
			
		}
</style>