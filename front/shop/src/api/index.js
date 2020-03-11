import jsCookie from 'js-cookie'
import axios from "axios"


axios.defaults.baseURL = 'http://127.0.0.1:8000';

export const getAds=()=>{
	return axios.get("/api/v1/adss/")
}

export const getProduct=()=>{
	return axios.get("/api/v1/products/")
}

export const getProductDetail=(param)=>{
	return axios.get(`/api/v1/products/${param.id}`)
}

export const getCategory=()=>{
	return axios.get("/api/v1/categorys/")
}

export const getGoodList=(param)=>{
	return axios.get("/api/v1/goods/")
}