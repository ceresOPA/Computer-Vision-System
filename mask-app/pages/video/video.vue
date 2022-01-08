<template>
	<view>
		<cu-custom bgColor="bg-gradual-blue" :isBack="true"><block slot="backText">返回</block><block slot="content">口罩视频识别</block></cu-custom>
		<view class="content">
			<view class="picture-block">
				<video v-if="videoUrl!=''" :src="videoUrl" autoplay="true" controls></video>
				<text v-if="videoUrl==''" class="text-gray text-xxl">结果展示</text>
			</view>
			<button  class="cu-btn round bg-orange lg picker-btn" @click="uploadVideo" >上传检测</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return { 
				
				videoUrl:''
				
			}
		},
		methods: {
			 
			uploadVideo:function(){
				
				let that = this;
				
			
				
				uni.chooseVideo({
					count: 1,
					sourceType: ['camera', 'album'],
					success: (chooseVideoRes) => {
						uni.showLoading({
							title:'检测中'
						});
						const tempFilePath = chooseVideoRes.tempFilePath;
						uni.uploadFile({
							url: that.ServerUrl+'/file/video', 
							filePath: tempFilePath,
							fileType:'video',
							name: 'file',
							success: (fileres) => {
								// that.imgName = res.data.imageName;
								console.log(JSON.parse(fileres.data).appvideoUrl);
								// that.videoUrl = JSON.parse(fileres.data).appvideoUrl;
								uni.request({
									url:that.ServerUrl+'/file/checkvideo',
									data:{
										model:'mask-yolov5s',
										videoName:JSON.parse(fileres.data).videoName
									},
									timeout:80000000,
									success(res) {
										
										console.log("finalImage:",res);
										// that.videoUrl = that.ServerUrl+res.data.appVideoUrl;
										that.videoUrl = that.ServerUrl + res.data.appVideoUrl;
										console.log("videoUrl",that.videoUrl);
										
										uni.downloadFile({
										    url:  that.ServerUrl + res.data.appVideoUrl, //仅为示例，并非真实的资源
										    success: (res) => {
												console.log(res);
										        if (res.statusCode === 200) {
										            console.log('下载成功');
													that.videoUrl = res.tempFilePath;
										        }
										    }
										});
										
										uni.hideLoading();
										
									},
									fail(res) {
										console.log("error",res);
									},
									complete() {
										
										uni.hideLoading();
										
									}
									
								})
								
							}
						});
					}
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
		background: #74ebd5;  /* fallback for old browsers */
		background: -webkit-linear-gradient(to right, #ACB6E5, #74ebd5);  /* Chrome 10-25, Safari 5.1-6 */
		background: linear-gradient(to right, #ACB6E5, #74ebd5); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
		
	}
</style>
