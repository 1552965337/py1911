import jsCookie from 'js-cookie'
import axios from "axios"

axios.defaults.baseURL = 'http://127.0.0.1:8000';

// 添加请求拦截器
axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么  config就是请求中的config参数
    if(jsCookie.get("access"))
    {
    	config.headers.Authorization=`Bearer ${jsCookie.get('access')}`;
    }
  
    
    return config;
  }, function (error) {
    // 对请求错误做些什么

    return Promise.reject(error);
  });

// 添加响应拦截器
axios.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    return response;
  }, function (error) {
    // 对响应错误做点什么
    if(error.response.status == 401){
    	//此处选择较为简单的直接重新登录
    	//还可以根据refresh和access进行刷新  再次重新请求
    	console.log("认证失败");
    	window.location.href="#/login/";
    	jsCookie.remove("access");
    	jsCookie.remove("refresh");
    	jsCookie.remove("username");
    	jsCookie.remove("userinfo");
    }
    
    return Promise.reject(error);
  });


export const getCategoryList=()=>{
	return axios.get("/api/v1/categorys/")

}

export const getCategoryDetail=(param)=>{
	return axios.get(`/api/v1/categorys/${param.id}`)

}

export const createCategory=(param)=>{
	return axios.post("/api/v1/categorys/",param)	
}


export const modifyCategory=(param)=>{
	return axios.put(`/api/v1/categorys/${param.id}/`,param)	
}


export const getToken=(param)=>{
	return axios.post("/obtaintoken/",param)
}

export const getUserinfo=(param)=>{
	return axios.get("/getuserinfo/",param)
}

export const regist=(param)=>{
	return axios.post("/api/v1/users/",param)
}

export const modifyUserInfo=(param)=>{
	let id=param.userinfo.id
	return axios.patch(`/api/v1/users/${id}/`,param.userinfo)
}

