<template>
	<view >
		<cu-custom bgColor="bg-gradual-blue" :isBack="true"><block slot="backText">返回</block><block slot="content">口罩图像识别</block></cu-custom>
		<view class="content">
			<view class="picture-block">
				<image v-if="imgUrl!=''" :src="imgUrl" mode="" @click="previewImg"></image>
				<text v-if="imgUrl==''" class="text-gray text-xxl">结果展示</text>
			</view>
			<button  class="cu-btn round bg-cyan lg picker-btn" @click="uploadPicture" >上传检测</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
				imgUrl:'',
				imgName:''
				
			}
		},
		methods: {
			
			uploadPicture:function(){

				let that = this;
				
		
				
				uni.chooseImage({
					success: (chooseImageRes) => {
						uni.showLoading({
							title:'检测中...'
						})
						const tempFilePaths = chooseImageRes.tempFilePaths;
						uni.uploadFile({
							url: that.ServerUrl+'/file/photo', //仅为示例，非真实的接口地址
							filePath: tempFilePaths[0],
							name: 'file',
							success: (fileres) => {
								// that.imgName = res.data.imageName;
								console.log(JSON.parse(fileres.data));
								uni.request({
									url:that.ServerUrl+'/file/checkphoto',
									data:{
										model:'mask-yolov5s',
										imageName:JSON.parse(fileres.data).imageName
									},
									success(res) {
										
										console.log("finalImage:",res);
										that.imgUrl = that.ServerUrl+res.data.appImgUrl;
										uni.hideLoading();
										
									}
								})
								
							}
						});
					},
					complete() {
					
					}
				});
				

				
			},
			previewImg:function(){
				
				var imgArr = [];
				imgArr.push(this.imgUrl);
				//预览图片
				uni.previewImage({
					urls: imgArr,
					current: imgArr[0]
				});

				
			}
			
		}
	}
</script>

<style>

page{
	
	background-color: #FFFFFF;
	
}

.content{
	
	margin-top: 60upx;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	
}

.picture-block{
	
	width: 720upx;
	height: 600upx;
	border: dotted #000000;
	display: flex;
	justify-content: center;
	align-items: center;
	
}

.picker-btn{
	
	margin-top: 160upx;
	background: #00B4DB;  /* fallback for old browsers */
	background: -webkit-linear-gradient(to right, #0083B0, #00B4DB);  /* Chrome 10-25, Safari 5.1-6 */
	background: linear-gradient(to right, #0083B0, #00B4DB); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

	
}

</style>
