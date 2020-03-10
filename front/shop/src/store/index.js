import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
	// data
  state: {
	  // 购物车
	  goodList:[],
	  // 我的订单
	  mygoodList:[],
	  // 全部订单
	  mytatalList:[],
  },
  // computed
  getters:{
	  // 购物车
	  getGoodList(state){
		  return state.goodList
	  },
	  // 我的
	  myGoodList(state){
		  return state.mygoodList
	  },
	   // 全部
	  myTatalList(state){
	  		  return state.mytatalList
	  },
  },
  // methods
  mutations: {
	  //加入到全部订单
	  addTotal(state,totgood){
		  state.mytatalList.push(totgood)
	  },
	  //加入到我的订单
	  addMy(state,mygod){
		  state.mygoodList.push(mygod)
	  },
	  // 加入购物车
	  addGood(state,good){
		  // state.goodList.push(good);
		  let canAdd=true;
		  let index=-1;
		  state.goodList.forEach((item,i)=>{
			  if(item.id==good.id){
				  canAdd=false;
				  index=i
			  }
		  })
		  if(canAdd){
			  state.goodList.push(good);
		  }
		  else{
			  state.goodList[index].num+=good.num;
			  
		  }
	  },
	  // 清空购物车
	  changeRemove(state){
		  state.goodList=[]
	  },
	  // 移除一个商品
	  changeRemoveOne(state,index){
	  		  state.goodList.splice(index,1);
	  },
	  // 改变购物车中商品的数量
	  changeGoodNum(state,index_num)
	  {   
		  // console.log(index_num[0],index_num[1],"++");
		  if(index_num[1]==0){
		  	state.goodList.splice(index_num[0],1);
		  }
		  else{
			  state.goodList[index_num[0]].num=index_num[1];
		  }
	  }
	  
  },
  // promise
  actions: {
  },
  // 模块
  modules: {
  }
})
