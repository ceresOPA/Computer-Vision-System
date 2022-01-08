<template>
	<view>
		<cu-custom bgColor="bg-gradual-blue" :isBack="false"><block slot="backText">返回</block><block slot="content">口罩识别助手</block></cu-custom>
		<view class="content">
			<view class="block margin-top" @click="toPicture">
				<view class="cu-bar justify-left ">
					<view class="action sub-title">
						<text class="text-xl text-bold text-cyan">口罩图像识别</text>
						<text class="bg-blue" style="width:2rem"></text>
						<!-- last-child选择器-->
					</view>
				</view>
				<view class="card-1 ">
					<text class="cuIcon-picfill"></text> 图像识别
				</view>
			</view>
			<view class="block margin-top" @click="toVideo">
				<view class="cu-bar justify-left ">
					<view class="action sub-title">
						<text class="text-xl text-bold text-cyan">口罩视频识别</text>
						<text class="bg-blue" style="width:2rem"></text>
						<!-- last-child选择器-->
					</view>
				</view>
				<view class="card-2 ">
					<text class="cuIcon-videofill"></text>视频识别
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
			toPicture:function(){
				
				uni.navigateTo({
					url:'../picture/picture'
				});
				
			},
			toVideo:function(){
				
				uni.navigateTo({
					url:'../video/video'
				})
				
			}
			
		}
	}
</script>

<style>
	
page{
	background-color: #FFFFFF;
}

.card-1{
	
	width: 720upx;
	height: 300upx;
	text-align: center;
	margin: 0 auto;
	border-radius: 20px;
	line-height: 300upx;
	font-size: 30px;
	font-family: '宋体';
	background: #00B4DB;  /* fallback for old browsers */
	background: -webkit-linear-gradient(to right, #0083B0, #00B4DB);  /* Chrome 10-25, Safari 5.1-6 */
	background: linear-gradient(to right, #0083B0, #00B4DB); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */




	color: #FFFFFF;
	
}

.card-2{
	
	width: 720upx;
	height: 300upx;
	text-align: center;
	margin: 0 auto;
	border-radius: 20px;
	line-height: 300upx;
	font-size: 30px;
	font-family: '宋体';
	background: #74ebd5;  /* fallback for old browsers */
	background: -webkit-linear-gradient(to right, #ACB6E5, #74ebd5);  /* Chrome 10-25, Safari 5.1-6 */
	background: linear-gradient(to right, #ACB6E5, #74ebd5); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

	color: #FFFFFF;
}

</style>
