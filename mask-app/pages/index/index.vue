<template>
	<view class="content ">
		<image class="logo" src="/static/mask.png" mode="aspectFit"></image>
		<view class="title">
			口罩识别助手
		</view>
		<input type="text" value="" placeholder="请输入用户名" class="input" v-model="username" />
		<input type="password" value="" placeholder="请输入密码" class="input" v-model="password" />
		<button class="cu-btn round bg-cyan lg margin-top" @click="LoginIn">登录</button>
		<text class="lg text-green cuIcon-weixin wechat" @click="wechatLogin">微信登录</text>
	</view>

</template>

<script>
	export default {
		data() {
			return {
				title: 'Hello',
				username: '',
				password: ''
			}
		},
		onLoad() {

			let userInfo = uni.getStorageSync("userInfo");
			if (userInfo != null && userInfo != undefined && userInfo != "") {

				uni.switchTab({
					url: '../main/main'
				});

			}

		},
		methods: {

			LoginIn: function() {

				uni.showLoading({
					title: '登录中'
				});

				let that = this;
				uni.request({
					url: that.ServerUrl + '/user/login?username=' + that.username + '&password=' + that.password,
					method: 'POST',
					data: {

					},
					success(res) {
						console.log(res);
						if (res.data.state == 'fail') {
							uni.showToast({
								icon: 'none',
								title: res.data.msg
							});
						} else {

							uni.setStorageSync("userInfo", res.data);
							uni.hideLoading();
							uni.showToast({
								title: '登录成功',
								icon: 'none'
							});
							uni.switchTab({
								url: '../main/main'
							});

						}
					},
					fail(res) {

						uni.showToast({
							icon: 'none',
							title: '服务器连接失败'
						})

					},

				})

			},
			wechatLogin: function() {

				uni.showToast({
					title:'仅微信小程序可用',
					icon:'none'
				});

			}

		}
	}
</script>

<style>
	.content {

		margin-top: 160upx;
		display: flex;
		flex-direction: column;
		/* justify-content: center; */
		align-items: center;
		width: 750upx;
		height: 100vh;
		position: fixed;

	}

	.logo {

		width: 200upx;
		height: 200upx;
		margin-bottom: 30upx;

	}

	.title {

		font-size: 26px;

	}

	.input {

		background-color: #FFFFFF;
		padding-left: 10upx;
		margin: 15px;
		border-radius: 15px;
		width: 600upx;
		height: 80upx;
		box-shadow: 5px 5px 30px #CCCCCC;

	}

	.wechat {

		font-size: 16px;
		margin-top: 60upx;

	}
</style>
