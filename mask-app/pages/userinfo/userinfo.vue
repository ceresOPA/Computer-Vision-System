<template>
	<view>
		<cu-custom bgColor="bg-gradual-blue" :isBack="true"><block slot="backText">返回</block><block slot="content">个人信息</block></cu-custom>
		<form >
			<view class="block-info" style="margin-top: 160upx;">
				<view style="display: flex;justify-content: center;align-items: center;" @click="uploadAvatar">
					<view class="cu-avatar round xl margin-left"  :style="[{ backgroundImage:'url(' + avatarUrl + ')' }]">
					</view>
				</view>
			</view>
			<view class="block-info" >
				<view class="title">用户名</view>
				<input placeholder="请输入用户名" v-model="username" name="input" class="input-info"></input>
			</view>
			<view class="block-info" >
				<view class="title">性别</view>
				<picker @change="PickerChange" :value="index" :range="picker" style="border-bottom: 2px solid #0083B0;">
					<view class="picker">
						{{index>-1?picker[index]:'选择性别'}}
					</view>
				</picker>
			</view>
			 
			<view class="block-info" >
				<view class="title">个性签名</view>
				<input placeholder="快来写下你的个性签名吧!" v-model="mark" name="input" class="input-info"></input>
			</view>
			
			<view class="btn-wapper" @click="changeInfo">
				<button form-type="submit" class="cu-btn round bg-cyan change-btn">确认修改</button>
			</view>
		</form>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				picker:['男','女'],
				index:-1,
				username:'',
				mark:'',
				avatarUrl:'',
				saveAvatar:''
			}
		},
		onLoad() {
			
			let userInfo = uni.getStorageSync("userInfo");

			this.username = userInfo.username;
			this.index = userInfo.gender=='男'?0:1;
			this.mark = userInfo.mark;
			this.avatarUrl = this.ServerUrl+userInfo.avatarUrl;
			this.saveAvatar = userInfo.avatarUrl;
		},
		methods: {
			
			changeInfo:function(){
				
				let that = this;
				let userInfo = uni.getStorageSync("userInfo");
				uni.request({
					url:that.ServerUrl+'/user/editUser',
					data:{
						username:that.username,
						gender:that.picker[that.index],
						mark:that.mark,
						id:userInfo.id,
						avatarUrl:that.saveAvatar
					},
					success(res){
						
						uni.setStorageSync("userInfo",res.data.user);
						uni.showToast({
							title:'保存成功',
							icon:'none'
						});
				
						
					}
				});
				
			},
			PickerChange:function(e){
				
				this.index = e.detail.value;
				
			},
			uploadAvatar:function(){
				
				let userInfo = uni.getStorageSync("userInfo");
				let that = this;
				uni.chooseImage({
					success: (chooseImageRes) => {
						uni.showLoading({
							title:'上传中'
						})
						const tempFilePaths = chooseImageRes.tempFilePaths;
						uni.uploadFile({
							url: that.ServerUrl+'/file/avatar?id='+userInfo.id, //仅为示例，非真实的接口地址
							filePath: tempFilePaths[0],
							name: 'file',
							success: (fileres) => {
								// that.imgName = res.data.imageName;
								console.log(JSON.parse(fileres.data));
								uni.hideLoading();
								that.avatarUrl = that.ServerUrl+JSON.parse(fileres.data).appImgUrl;
								that.saveAvatar = JSON.parse(fileres.data).appImgUrl;
								
							}
						});
					},
					complete() {
					
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
	
.block-info{
	
	margin: 60upx;
	
}

.title{
	
	margin-bottom: 30upx;
	
}

.btn-wapper{
	
	display: flex;
	justify-content: center;
	align-items: center;
	
}

.change-btn{
	
	margin: 0 auto;
	
}

.cu-form-group picker::after {
	color: #FFFFFF;
}

.input-info{
	
	border: none;
	border-bottom:2px #0083B0 solid;
	transition: .5s linear;
	
}

.input-info:hover{
	
	border-bottom: 2px #1CBBB4 solid;
	
}

</style>
