// let lists=[
// 				"img1/1.jpg",
// 				"img1/2.jpg",
// 				"img1/3.jpg",
// 				"img1/4.jpg",
// 				"img1/5.jpg",
// 				"img1/6.jpg",
// 				"img1/7.jpg",
// 				"img1/8.jpg",
// 				"img1/9.jpg",
// 				"img1/10.jpg",
// 				"img1/11.jpg",
// 				"img1/12.jpg",
// 				];
				
let dictBs=[
	{"ItemCode":"1","num":"已售8.8万件","Price":239,"LinePrice":315,"Cpmc":"一往情深","Instro":"精品玫瑰礼盒:19枝红玫瑰，勿忘我0.1扎","Sales":"2.5万","img":"img1/1.jpg"},
	{"ItemCode":"2","num":"已售4.3万件","Price":298,"LinePrice":382,"Cpmc":"忘情巴黎","Instro":"33枝红玫瑰","Sales":"6.5万","img":"img1/2.jpg"},
	{"ItemCode":"3","num":"已售3.4万件","Price":198,"LinePrice":255,"Cpmc":"恋恋情深","Instro":"11枝香槟玫瑰，白色多头百合2枝","Sales":"2.2万","img":"img1/3.jpg"},
	{"ItemCode":"4","num":"已售5000件","Price":539,"LinePrice":766,"Cpmc":"不变的承诺","Instro":"99枝红玫瑰","Sales":"1.2万","img":"img1/4.jpg"},
	{"ItemCode":"5","num":"已售8000件","Price":368,"LinePrice":485,"Cpmc":"甜美公主","Instro":"白玫瑰22枝，粉佳人粉玫瑰14枝，粉色桔梗5枝","Sales":"1.2万","img":"img1/5.jpg"},
	{"ItemCode":"6","num":"已售5.1万件","Price":389,"LinePrice":479,"Cpmc":"爱在心头","Instro":"玫瑰50枝：戴安娜粉玫瑰19枝，红玫瑰31枝","Sales":"1.9万","img":"img1/6.jpg"},
	{"ItemCode":"7","num":"已售1.1万件","Price":139,"LinePrice":189,"Cpmc":"一心一意","Instro":"玫瑰11枝，粉色勿忘我0.3扎","Sales":"5.1万","img":"img1/7.jpg"},
	{"ItemCode":"8","num":"已售7.5万件","Price":248,"LinePrice":331,"Cpmc":"你最珍贵","Instro":"精品玫瑰礼盒:香槟玫瑰19枝，勿忘我适量","Sales":"3.7万","img":"img1/8.jpg"},
	{"ItemCode":"9","num":"已售2.1万件","Price":198,"LinePrice":256,"Cpmc":" 语笑嫣然","Instro":"粉佳人玫瑰9枝、粉色小菊、洋桔梗、尤加利叶","Sales":"1427","img":"img1/9.jpg"},
	{"ItemCode":"10","num":"已售6000件","Price":196,"LinePrice":281,"Cpmc":"牵手一生","Instro":"红玫瑰19枝","Sales":"2.1万","img":"img1/10.jpg"},
	{"ItemCode":"11","num":"已售7.3万件","Price":469,"LinePrice":601,"Cpmc":"不变的心","Instro":"戴安娜玫瑰66枝","Sales":"1.1万","img":"img1/11.jpg"},
	{"ItemCode":"12","num":"已售5.2万件","Price":639,"LinePrice":859,"Cpmc":"永恒的爱情","Instro":"红玫瑰99枝","Sales":"3829","img":"img1/12.jpg"},
	];

// let img1=[
// 			[ "img2/1.jpg", "img2/2.jpg", "img2/3.jpg", "img2/4.jpg","img2/5.jpg","img2/6.jpg", "img2/7.jpg", "img2/8.jpg", "img2/9.jpg","img2/10.jpg"],
// 			["img2/11.jpg", "img2/12.jpg", "img2/13.jpg", "img2/14.jpg","img2/15.jpg",],
// 			["img2/16.jpg", "img2/17.jpg", "img2/18.jpg", "img2/19.jpg","img2/20.jpg"],
// 			[ "img2/21.jpg", "img2/22.jpg", "img2/23.jpg", "img2/24.jpg","img2/25.jpg","img2/26.jpg", "img2/27.jpg"],
// 			[ "img2/28.jpg", "img2/29.jpg", "img2/30.jpg", "img2/31.jpg","img2/32.jpg","img2/33.jpg", "img2/34.jpg"]
// 		];

let dictC=[
		[
			{"ItemCode":"13","Price":239,"LinePrice":315,"Cpmc":"一往情深","Instro":"精品玫瑰礼盒:19枝红玫瑰，勿忘我0.1扎","Sales":"7.5万","img":"img2/1.jpg"},
			{"ItemCode":"14","Price":298,"LinePrice":382,"Cpmc":"忘情巴黎","Instro":"33枝红玫瑰","Sales":"6.5万","img":"img2/2.jpg"},
			{"ItemCode":"15","Price":198,"LinePrice":255,"Cpmc":"恋恋情深","Instro":"11枝香槟玫瑰，白色多头百合2枝","Sales":"7.2万","img":"img2/3.jpg"},
			{"ItemCode":"16","Price":539,"LinePrice":766,"Cpmc":"不变的承诺","Instro":"99枝红玫瑰","Sales":"6.2万","img":"img2/4.jpg"},
			{"ItemCode":"17","Price":368,"LinePrice":485,"Cpmc":"甜美公主","Instro":"白玫瑰22枝，粉佳人粉玫瑰14枝，粉色桔梗5枝","Sales":"2.2万","img":"img2/5.jpg"},
			{"ItemCode":"18","Price":389,"LinePrice":479,"Cpmc":"爱在心头","Instro":"玫瑰50枝：戴安娜粉玫瑰19枝，红玫瑰31枝","Sales":"1.9万","img":"img2/6.jpg"},
			{"ItemCode":"19","Price":139,"LinePrice":189,"Cpmc":"一心一意","Instro":"玫瑰11枝，粉色勿忘我0.3扎","Sales":"11.1万","img":"img2/7.jpg"},
			{"ItemCode":"20","Price":248,"LinePrice":331,"Cpmc":"你最珍贵","Instro":"精品玫瑰礼盒:香槟玫瑰19枝，勿忘我适量","Sales":"5.7万","img":"img2/8.jpg"},
			{"ItemCode":"21","Price":198,"LinePrice":256,"Cpmc":" 语笑嫣然","Instro":"粉佳人玫瑰9枝、粉色小菊、洋桔梗、尤加利叶","Sales":"1427","img":"img2/9.jpg"},
			{"ItemCode":"22","Price":196,"LinePrice":281,"Cpmc":"牵手一生","Instro":"红玫瑰19枝","Sales":"6.1万","img":"img2/10.jpg"},],
		[
			{"ItemCode":"23","Price":398,"LinePrice":498,"Cpmc":"永生花满月艺术台灯/朦胧粉","Instro":"永生花台灯","Sales":"70","img":"img2/11.jpg"},
			{"ItemCode":"24","Price":298,"LinePrice":398,"Cpmc":"花好月圆永生花台灯","Instro":"精选进口奥斯汀永生玫瑰台灯","Sales":"793","img":"img2/12.jpg"},
			{"ItemCode":"25","Price":588,"LinePrice":788,"Cpmc":"我如此爱你-口红款520","Instro":"Dior#520口红(专柜正品)＋进口永生玫瑰礼盒","Sales":"1261","img":"img2/13.jpg"},
			{"ItemCode":"26","Price":298,"LinePrice":398,"Cpmc":"一鹿(路)有你永生花小夜灯","Instro":"永生花礼盒","Sales":"70","img":"img2/14.jpg"},
			{"ItemCode":"27","Price":368,"LinePrice":468,"Cpmc":"时光的花","Instro":"复古相框 ,进口粉色玫瑰2枝 ,进口紫色玫瑰1枝","Sales":"2141","img":"img2/15.jpg"}],
		[
			{"ItemCode":"28","Price":178,"LinePrice":208,"Cpmc":"陪伴左右","Instro":"2磅(8寸)水果蛋糕","Sales":"5450","img":"img2/16.jpg"},
			{"ItemCode":"29","Price":168,"LinePrice":178,"Cpmc":"幸福时刻","Instro":"8寸(2磅)心形鲜奶蛋糕","Sales":"6520","img":"img2/17.jpg"},
			{"ItemCode":"30","Price":178,"LinePrice":188,"Cpmc":"我的心属于你","Instro":"8寸(2磅)鲜奶水果蛋糕","Sales":"5213","img":"img2/18.jpg"},
			{"ItemCode":"31","Price":179,"LinePrice":209,"Cpmc":"纯洁挚爱","Instro":"2磅(8寸)水果蛋糕","Sales":"3491","img":"img2/19.jpg"},
			{"ItemCode":"32","Price":168,"LinePrice":178,"Cpmc":"I LOVE YOU","Instro":"8寸(2磅)心形鲜奶蛋糕","Sales":"5943","img":"img2/20.jpg"}],
		[
			{"ItemCode":"33","Price":1580,"LinePrice":1680,"Cpmc":"Dior烈艳蓝金唇膏烟花限量版套装","Instro":"高订套装饰以璀璨烟花，一套汇集6款明星色号，打造百变妆容 演绎百变魅力","Sales":"81","img":"img2/21.jpg"},
			{"ItemCode":"34","Price":1099,"LinePrice":1199,"Cpmc":"Dior迪奥真我香氛礼盒(圣诞限量版)","Instro":"原产法国真我精选：迪奥真我香氛、迪奥全新真我香调身体乳","Sales":"303","img":"img2/22.jpg"},
			{"ItemCode":"35","Price":228,"LinePrice":368,"Cpmc":"布蕾兔暖水袋","Instro":"寒潮中的法式温暖","Sales":"661","img":"img2/23.jpg"},
			{"ItemCode":"36","Price":198,"LinePrice":298,"Cpmc":"星期耳钉礼盒","Instro":"s925银个性耳钉","Sales":"1194","img":"img2/24.jpg"},
			{"ItemCode":"37","Price":2399,"LinePrice":2480,"Cpmc":"施华洛世奇DAZZLING SWAN手链+项链套装","Instro":"浪漫天鹅  项链+手链套装饰品 镀玫瑰金色","Sales":"35","img":"img2/25.jpg"},
			{"ItemCode":"38","Price":129,"LinePrice":229,"Cpmc":"素乐Line联名暖手宝充电宝-可妮兔","Instro":"USB暖手宝 Line Friends定制款","Sales":"60","img":"img2/26.jpg"},
			{"ItemCode":"39","Price":198,"LinePrice":298,"Cpmc":"woody书灯木质led折叠usb书本灯-时尚版（黑胡桃）","Instro":"","Sales":"193","img":"img2/27.jpg"}],
		[
			{"ItemCode":"40","Price":558,"LinePrice":598,"Cpmc":"蝴蝶兰6株","Instro":"蝴蝶兰-室内盆栽（6株红色一品蝴蝶兰）","Sales":"1459","img":"img2/28.jpg"},
			{"ItemCode":"41","Price":338,"LinePrice":398,"Cpmc":"蝴蝶兰4株","Instro":"蝴蝶兰-室内盆栽（4株紫色一品蝴蝶兰）","Sales":"923","img":"img2/29.jpg"},
			{"ItemCode":"42","Price":498,"LinePrice":560,"Cpmc":"纯洁天使","Instro":"蝴蝶兰（5株白色一品蝴蝶兰）","Sales":"397","img":"img2/30.jpg"},
			{"ItemCode":"43","Price":899,"LinePrice":999,"Cpmc":"十全十美","Instro":"蝴蝶兰- 室内盆栽（10株红色一品蝴蝶兰）。 ","Sales":"1060","img":"img2/31.jpg"},
			{"ItemCode":"44","Price":498,"LinePrice":538,"Cpmc":"蝴蝶兰5株","Instro":"蝴蝶兰- 室内盆栽(紫蝴蝶兰3株、浅粉蝴蝶兰2株)。","Sales":"614","img":"img2/32.jpg"},
			{"ItemCode":"45","Price":452,"LinePrice":498,"Cpmc":"迎福纳祥","Instro":"5株粉红色一品蝴蝶兰。(开花期3个月以上)","Sales":"1423","img":"img2/33.jpg"},
			{"ItemCode":"46","Price":218,"LinePrice":238,"Cpmc":"吉祥如意","Instro":"蝴蝶兰- 室内盆栽（2株紫红色蝴蝶兰）","Sales":"1826","img":"img2/34.jpg"}]
	];
	
	let dictA=[
		{"ItemCode":"1","Price":239,"LinePrice":315,"Cpmc":"一往情深","Instro":"精品玫瑰礼盒:19枝红玫瑰，勿忘我0.1扎","Sales":"2.5万","img":"img1/1.jpg"},
		{"ItemCode":"2","Price":298,"LinePrice":382,"Cpmc":"忘情巴黎","Instro":"33枝红玫瑰","Sales":"6.5万","img":"img1/2.jpg"},
		{"ItemCode":"3","Price":198,"LinePrice":255,"Cpmc":"恋恋情深","Instro":"11枝香槟玫瑰，白色多头百合2枝","Sales":"2.2万","img":"img1/3.jpg"},
		{"ItemCode":"4","Price":539,"LinePrice":766,"Cpmc":"不变的承诺","Instro":"99枝红玫瑰","Sales":"1.2万","img":"img1/4.jpg"},
		{"ItemCode":"5","Price":368,"LinePrice":485,"Cpmc":"甜美公主","Instro":"白玫瑰22枝，粉佳人粉玫瑰14枝，粉色桔梗5枝","Sales":"1.2万","img":"img1/5.jpg"},
		{"ItemCode":"6","Price":389,"LinePrice":479,"Cpmc":"爱在心头","Instro":"玫瑰50枝：戴安娜粉玫瑰19枝，红玫瑰31枝","Sales":"1.9万","img":"img1/6.jpg"},
		{"ItemCode":"7","Price":139,"LinePrice":189,"Cpmc":"一心一意","Instro":"玫瑰11枝，粉色勿忘我0.3扎","Sales":"5.1万","img":"img1/7.jpg"},
		{"ItemCode":"8","Price":248,"LinePrice":331,"Cpmc":"你最珍贵","Instro":"精品玫瑰礼盒:香槟玫瑰19枝，勿忘我适量","Sales":"3.7万","img":"img1/8.jpg"},
		{"ItemCode":"9","Price":198,"LinePrice":256,"Cpmc":" 语笑嫣然","Instro":"粉佳人玫瑰9枝、粉色小菊、洋桔梗、尤加利叶","Sales":"1427","img":"img1/9.jpg"},
		{"ItemCode":"10","Price":196,"LinePrice":281,"Cpmc":"牵手一生","Instro":"红玫瑰19枝","Sales":"2.1万","img":"img1/10.jpg"},
		{"ItemCode":"11","Price":469,"LinePrice":601,"Cpmc":"不变的心","Instro":"戴安娜玫瑰66枝","Sales":"1.1万","img":"img1/11.jpg"},
		{"ItemCode":"12","Price":639,"LinePrice":859,"Cpmc":"永恒的爱情","Instro":"红玫瑰99枝","Sales":"3829","img":"img1/12.jpg"},
		
		{"ItemCode":"13","Price":239,"LinePrice":315,"Cpmc":"一往情深","Instro":"精品玫瑰礼盒:19枝红玫瑰，勿忘我0.1扎","Sales":"7.5万","img":"img2/1.jpg"},
		{"ItemCode":"14","Price":298,"LinePrice":382,"Cpmc":"忘情巴黎","Instro":"33枝红玫瑰","Sales":"6.5万","img":"img2/2.jpg"},
		{"ItemCode":"15","Price":198,"LinePrice":255,"Cpmc":"恋恋情深","Instro":"11枝香槟玫瑰，白色多头百合2枝","Sales":"7.2万","img":"img2/3.jpg"},
		{"ItemCode":"16","Price":539,"LinePrice":766,"Cpmc":"不变的承诺","Instro":"99枝红玫瑰","Sales":"6.2万","img":"img2/4.jpg"},
		{"ItemCode":"17","Price":368,"LinePrice":485,"Cpmc":"甜美公主","Instro":"白玫瑰22枝，粉佳人粉玫瑰14枝，粉色桔梗5枝","Sales":"2.2万","img":"img2/5.jpg"},
		{"ItemCode":"18","Price":389,"LinePrice":479,"Cpmc":"爱在心头","Instro":"玫瑰50枝：戴安娜粉玫瑰19枝，红玫瑰31枝","Sales":"1.9万","img":"img2/6.jpg"},
		{"ItemCode":"19","Price":139,"LinePrice":189,"Cpmc":"一心一意","Instro":"玫瑰11枝，粉色勿忘我0.3扎","Sales":"11.1万","img":"img2/7.jpg"},
		{"ItemCode":"20","Price":248,"LinePrice":331,"Cpmc":"你最珍贵","Instro":"精品玫瑰礼盒:香槟玫瑰19枝，勿忘我适量","Sales":"5.7万","img":"img2/8.jpg"},
		{"ItemCode":"21","Price":198,"LinePrice":256,"Cpmc":" 语笑嫣然","Instro":"粉佳人玫瑰9枝、粉色小菊、洋桔梗、尤加利叶","Sales":"1427","img":"img2/9.jpg"},
		{"ItemCode":"22","Price":196,"LinePrice":281,"Cpmc":"牵手一生","Instro":"红玫瑰19枝","Sales":"6.1万","img":"img2/10.jpg"},
		
		{"ItemCode":"23","Price":398,"LinePrice":498,"Cpmc":"永生花满月艺术台灯/朦胧粉","Instro":"永生花台灯","Sales":"70","img":"img2/11.jpg"},
		{"ItemCode":"24","Price":298,"LinePrice":398,"Cpmc":"花好月圆永生花台灯","Instro":"精选进口奥斯汀永生玫瑰台灯","Sales":"793","img":"img2/12.jpg"},
		{"ItemCode":"25","Price":588,"LinePrice":788,"Cpmc":"我如此爱你-口红款520","Instro":"Dior#520口红(专柜正品)＋进口永生玫瑰礼盒","Sales":"1261","img":"img2/13.jpg"},
		{"ItemCode":"26","Price":298,"LinePrice":398,"Cpmc":"一鹿(路)有你永生花小夜灯","Instro":"永生花礼盒","Sales":"70","img":"img2/14.jpg"},
		{"ItemCode":"27","Price":368,"LinePrice":468,"Cpmc":"时光的花","Instro":"复古相框 ,进口粉色玫瑰2枝 ,进口紫色玫瑰1枝","Sales":"2141","img":"img2/15.jpg"},
		
		{"ItemCode":"28","Price":178,"LinePrice":208,"Cpmc":"陪伴左右","Instro":"2磅(8寸)水果蛋糕","Sales":"5450","img":"img2/16.jpg"},
		{"ItemCode":"29","Price":168,"LinePrice":178,"Cpmc":"幸福时刻","Instro":"8寸(2磅)心形鲜奶蛋糕","Sales":"6520","img":"img2/17.jpg"},
		{"ItemCode":"30","Price":178,"LinePrice":188,"Cpmc":"我的心属于你","Instro":"8寸(2磅)鲜奶水果蛋糕","Sales":"5213","img":"img2/18.jpg"},
		{"ItemCode":"31","Price":179,"LinePrice":209,"Cpmc":"纯洁挚爱","Instro":"2磅(8寸)水果蛋糕","Sales":"3491","img":"img2/19.jpg"},
		{"ItemCode":"32","Price":168,"LinePrice":178,"Cpmc":"I LOVE YOU","Instro":"8寸(2磅)心形鲜奶蛋糕","Sales":"5943","img":"img2/20.jpg"},
		
		{"ItemCode":"33","Price":1580,"LinePrice":1680,"Cpmc":"Dior烈艳蓝金唇膏烟花限量版套装","Instro":"高订套装饰以璀璨烟花，一套汇集6款明星色号，打造百变妆容 演绎百变魅力","Sales":"81","img":"img2/21.jpg"},
		{"ItemCode":"34","Price":1099,"LinePrice":1199,"Cpmc":"Dior迪奥真我香氛礼盒(圣诞限量版)","Instro":"原产法国真我精选：迪奥真我香氛、迪奥全新真我香调身体乳","Sales":"303","img":"img2/22.jpg"},
		{"ItemCode":"35","Price":228,"LinePrice":368,"Cpmc":"布蕾兔暖水袋","Instro":"寒潮中的法式温暖","Sales":"661","img":"img2/23.jpg"},
		{"ItemCode":"36","Price":198,"LinePrice":298,"Cpmc":"星期耳钉礼盒","Instro":"s925银个性耳钉","Sales":"1194","img":"img2/24.jpg"},
		{"ItemCode":"37","Price":2399,"LinePrice":2480,"Cpmc":"施华洛世奇DAZZLING SWAN手链+项链套装","Instro":"浪漫天鹅  项链+手链套装饰品 镀玫瑰金色","Sales":"35","img":"img2/25.jpg"},
		{"ItemCode":"38","Price":129,"LinePrice":229,"Cpmc":"素乐Line联名暖手宝充电宝-可妮兔","Instro":"USB暖手宝 Line Friends定制款","Sales":"60","img":"img2/26.jpg"},
		{"ItemCode":"39","Price":198,"LinePrice":298,"Cpmc":"woody书灯木质led折叠usb书本灯-时尚版（黑胡桃）","Instro":"","Sales":"193","img":"img2/27.jpg"},
		
		{"ItemCode":"40","Price":558,"LinePrice":598,"Cpmc":"蝴蝶兰6株","Instro":"蝴蝶兰-室内盆栽（6株红色一品蝴蝶兰）","Sales":"1459","img":"img2/28.jpg"},
		{"ItemCode":"41","Price":338,"LinePrice":398,"Cpmc":"蝴蝶兰4株","Instro":"蝴蝶兰-室内盆栽（4株紫色一品蝴蝶兰）","Sales":"923","img":"img2/29.jpg"},
		{"ItemCode":"42","Price":498,"LinePrice":560,"Cpmc":"纯洁天使","Instro":"蝴蝶兰（5株白色一品蝴蝶兰）","Sales":"397","img":"img2/30.jpg"},
		{"ItemCode":"43","Price":899,"LinePrice":999,"Cpmc":"十全十美","Instro":"蝴蝶兰- 室内盆栽（10株红色一品蝴蝶兰）。 ","Sales":"1060","img":"img2/31.jpg"},
		{"ItemCode":"44","Price":498,"LinePrice":538,"Cpmc":"蝴蝶兰5株","Instro":"蝴蝶兰- 室内盆栽(紫蝴蝶兰3株、浅粉蝴蝶兰2株)。","Sales":"614","img":"img2/32.jpg"},
		{"ItemCode":"45","Price":452,"LinePrice":498,"Cpmc":"迎福纳祥","Instro":"5株粉红色一品蝴蝶兰。(开花期3个月以上)","Sales":"1423","img":"img2/33.jpg"},
		{"ItemCode":"46","Price":218,"LinePrice":238,"Cpmc":"吉祥如意","Instro":"蝴蝶兰- 室内盆栽（2株紫红色蝴蝶兰）","Sales":"1826","img":"img2/34.jpg"},
		
	]
	export {dictBs,dictC,dictA}