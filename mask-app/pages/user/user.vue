<template>
	<view>
		<cu-custom bgColor="bg-gradual-blue" :isBack="false"><block slot="backText">返回</block><block slot="content">口罩识别助手</block></cu-custom>
		<view class="card-info bg-gradual-blue">
			<view class="cu-avatar round xl margin-left"  :style="[{ backgroundImage:'url(' + avatarUrl + ')' }]">
				<view class="cu-tag badge" :class="gender=='女'?'cuIcon-female bg-pink':'cuIcon-male bg-blue'"></view>
			</view>
			<view class="user-info">
				<view class="username">
					用户名：{{username}}
				</view>
				<view class="mark">
					{{mark}}
				</view>
			</view>
		</view>
		<view class="nav-block bg-gradual-blue" @click="toUserInfo">
			<text class="cuIcon-people"></text>
			个人信息
			<text class="cuIcon-right float"></text>
		</view>
		<view class="nav-block bg-gradual-blue" @click="toLogin">
			<text class="cuIcon-back_android"></text>
			退出登录
			<!-- <text class="cuIcon-right float"></text> -->
		</view>
	<!-- 	<view class="user-bg">
			<image src="../../static/timg.jpg" class="img-bg" mode="aspectFill"></image>
		</view> -->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				username:'',
				gender:'',
				mark:'快去个人信息设置你的个性签名吧！',
				avatarUrl: '',
				random:1
			}
		},
		onShow() {
			let userInfo = uni.getStorageSync("userInfo");
			console.log("userInfo",userInfo);
			this.username = userInfo.username;
			this.gender = userInfo.gender;
			this.mark = userInfo.mark;
			this.random = Math.floor(Math.random()*11);
			this.avatarUrl = this.ServerUrl+userInfo.avatarUrl;
			
		},
		methods: {
			
			toUserInfo:function(){
				
				uni.navigateTo({
					url:'../userinfo/userinfo'
				})
				
			},
			
			toLogin:function(){
				
				uni.removeStorageSync("userInfo");
				uni.redirectTo({
					url:'../index/index'
				});
				
			}
			
		}
	}
</script>

<style>
	
page{
	background-color: #FFFFFF;
}

.card-info{
	
	margin: 60upx 10upx 60upx 10upx;
	border-radius: 20px;
	width: 730upx;
	height: 260upx;
	display: flex;
	justify-content: space-evenly;
	align-items: center;
	
}

.gender , .username{
	
	font-size: 16px;
	
}

.nav-block{
	
	width: 720upx;
	padding: 20upx;
	margin: 15upx auto;
	border-radius: 15px;
	font-size: 16px;
	
}

.float{
	
	float: right;
	
}

.user-bg{
	
	display: flex;
	justify-content: center;
	align-items: center;
	margin-top: 60upx;
	
}

.user-info{
	line-height: 60upx;
}

.swapper-avatar{
	
	width: 180upx;
	height: 180upx;
	
	
}

.swapper-avatar image{
	
	border-radius: 50%;
	width: 180upx;
	height: 180upx;
	
}

</style>
