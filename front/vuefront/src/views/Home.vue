<template>
<div class="home">
	<img alt="Vue logo" src="../assets/logo.png">
	<div class="categorys">
		<van-cell v-for="(item,index) in categorys" :title="item.name" is-link :to="'/categorys/'+item.id+'/'" />
	</div>
	
	
	
	
	
	
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
	<!--<div>
		<button @click="requestCategoryList">发起请求分类列表</button>
	</div>-->
	
	<div>
		<!--<label for="">分类名</label><input type="text" v-model="categoryname">
		<br>-->
		 <van-field v-model="categoryname" placeholder="请输入分类名" />
		<van-button type="primary" @click="requestCreateCategory">发起创建分类请求</van-button>
	</div>
	
	<!--<div>
		<label for="">需要修改的分类的id</label> <input type="text" v-model="newcategoryid"/>
		<br />
		<label for="">需要修改的分类的名字</label> <input type="text" v-model="newcategoryname">
		<br>
		<button @click="requestModifyCategory">修改分类</button>
	</div>-->


</div>	
  
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    // HelloWorld
  },
  data(){
	  return{
	  	categorys:[],
//		  username:"admin",
//		  password:"123456",
		  categoryname:"",
//		  newcategoryid:"",
//		  newcategoryname:""
	  }
  },
  created(){
  	this.requestCategoryList();
  },
  methods:{
	  requestCategoryList(){
	  	this.$api.getCategoryList().then(res=>{
	  		console.log("得到分类列表",res);
	  		if(res.status==200){
	  			this.categorys=res.data;
	  		}
	  		
	  	}).catch(err=>{
	  		console.log("发生错误",err);
	  	})
	  },

	  requestCreateCategory(){
		if(this.categoryname!=""){
			this.$api.createCategory({
				name:this.categoryname
			}).then(res=>{
				console.log("创建结果",res);
				this.categorys.push(res.data);
				this.categoryname="";
			}).catch(err=>{
				console.log("出错了",err)
			})
		}
		else{
			this.$toast("必须输入分类名")
			console.log("必须输入分类名")
		}
	  },
//	  requestModifyCategory(){
//	  	if(this.newcategoryid=="" || this.newcategoryname==""){
//	  		console.log("需要选择分类并且重新给予名字")
//	  	}
//	  	else{
//	  		this.$api.modifyCategory({
//	  			id:this.newcategoryid,
//	  			name:this.newcategoryname,
//	  		}).then(res=>{
//	  			console.log(res);
//	  		}).catch(err=>{
//	  			console.log(err);
//	  		})
//	  	}
//	  }
	  
  },
}
</script>


<!--浏览器默认的同源策略不允许跨域访问   域名端口必须一致
Access to XMLHttpRequest
at 'http://127.0.0.1:8000/api/v1/categorys/' 
from origin 'http://localhost:8080' has been blocked by CORS policy:
 No 'Access-Control-Allow-Origin' header is present on the requested resource.-->