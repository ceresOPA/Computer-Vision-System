<template>
  <div class="login-container">
    <el-form
      ref="loginForm"
      :model="loginForm"
      class="login-form"
      auto-complete="on"
      label-position="left"
      :rules="loginRules"
    >
      <div class="top-container">
        <img src="../../images/smoke.png" style="margin-bottom:30px;" alt srcset>
        <h2 class="title-top">吸烟识别系统</h2>
      </div>

      <div class="title-container">
        <h3 class="title">注册账号</h3>
      </div>

      <el-form-item prop="username">
        <span class="svg-container">
          <svg-icon icon-class="user" />
        </span>
        <el-input
          ref="username"
          v-model="loginForm.username"
          placeholder="用户名"
          name="username"
          type="text"
          tabindex="1"
          auto-complete="off"
        />
      </el-form-item>

      <el-form-item prop="password">
        <span class="svg-container">
          <svg-icon icon-class="password" />
        </span>
        <el-input
          :key="passwordType"
          ref="password"
          v-model="loginForm.password"
          :type="passwordType"
          placeholder="密码"
          name="password"
          tabindex="2"
          auto-complete="off"
          @keyup.enter.native="handleLogin"
        />
        <span class="show-pwd" @click="showPwd">
          <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
        </span>
      </el-form-item>

      <el-form-item prop="confirmPassword">
        <span class="svg-container">
          <svg-icon icon-class="password" />
        </span>
        <el-input
          :key="confirmPasswordType"
          ref="confirmPassword"
          v-model="loginForm.confirmPassword"
          :type="confirmPasswordType"
          placeholder="确认密码"
          name="confirmPassword"
          tabindex="2"
          auto-complete="off"
        />
        <span class="show-pwd" @click="showConfirmPwd">
          <svg-icon :icon-class="confirmPasswordType === 'password' ? 'eye' : 'eye-open'" />
        </span>
      </el-form-item>

      <el-form-item>
        <el-select v-model="gender" placeholder="请选择性别" style="width:526px;">
          <el-option label="男" value="男" />
          <el-option label="女" value="女" />
        </el-select>
      </el-form-item>

      <div style="display:flex;">

        <el-button
          :loading="loading"
          type="primary"
          style="width:100%;margin-bottom:30px;"
          @click.native.prevent="returnIndex"
        >返回</el-button>

        <el-button
          :loading="loading"
          type="primary"
          style="width:100%;margin-bottom:30px;"
          @click="handleRegister"
        >注册</el-button>
      </div>

      <!--
      <div class="tips">
        <span style="margin-right:20px;">username: admin</span>
        <span> password: any</span>
      </div>-->
    </el-form>
  </div>
</template>

<script>

export default {
  name: 'Register',
  data() {
    const validateUsername = (rule, value, callback) => {
      console.log('username', value)
      if (value.length == 0) {
        callback('用户名不能为空')
        return
      }
      this.req({
        url: '/user/checkuser',
        params: {
          username: value
        }
      }).then(res => {
        if (res.data.state == 'fail') {
          callback('用户名已存在')
        }
      })
    }

    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback('密码不能少于6位')
      } else {
        callback()
      }
    }

    const validateConfirmPassword = (rule, value, callback) => {
      console.log('sada', value)
      if (value != this.loginForm.password) {
        callback(new Error('两次密码不一致'))
      }else{
        callback()
      }
    }
    return {
      loginForm: {
        username: '',
        password: '',
        confirmPassword: ''
      },
      loginRules: {
        username: [
          { required: true, trigger: 'blur', validator: validateUsername }
        ],
        password: [
          { required: true, trigger: 'blur', validator: validatePassword }
        ],
        confirmPassword: [
          { required: true, trigger: 'blur', validator: validateConfirmPassword }
        ]
      },
      loading: false,
      passwordType: 'password',
      confirmPasswordType: 'password',
      redirect: undefined,
      gender: ''
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  methods: {

    returnIndex() {
      this.$router.push({ path: '/' })
    },

    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
    },

    showConfirmPwd() {
      if (this.confirmPasswordType === 'password') {
        this.confirmPasswordType = ''
      } else {
        this.confirmPasswordType = 'password'
      }
    },

    handleRegister() {

        let user = {
          username:this.loginForm.username,
          password:this.loginForm.password,
          gender:this.gender
        }

        this.req({
          url: '/user/register',
          method:'post',
          params:user,
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        }).then(res=>{

            console.log(res);

            this.$message({

              message: '注册成功，请返回登录',
              type: 'success'

            });

        })
    }

  }
}
</script>

<style lang="scss">
$bg: #2d3a4b;
$light_gray: #fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }

  .top-container {
    display: flex;
    flex-direction: column;
    align-items: center;

    .title-top {
      font-size: 30px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }
}
</style>

<style lang="scss" scoped>
$bg: #2d3a4b;
$dark_gray: #889aa4;
$light_gray: #eee;

.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }

  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: -15px auto 20px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }
}
</style>
