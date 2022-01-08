<template>
  <div class="container">
    <div class="title">用户信息</div>
    <el-form ref="form" :model="form" label-width="100px">
      <el-form-item label="用户名" style="width:300px;">
        <el-input v-model="form.username" />
      </el-form-item>
      <el-form-item label="性别" style="width:360px;">
        <el-select v-model="form.gender" placeholder="请选择活动区域">
          <el-option label="男" value="男" />
          <el-option label="女" value="女" />
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">确认修改</el-button>
        <el-button>取消重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  data() {
    return {

      form: {
        username: '',
        gender: ''
      }

    }
  },
  created() {
    const userInfo = JSON.parse(sessionStorage.getItem('userInfo'))
    // console.log('userInfo', userInfo)
    this.form = userInfo
  },
  methods: {
    onSubmit() {
      // const that = this
      console.log('form-userInfo', this.form)
      const username = this.form.username
      const user_id = this.form.id
      const gender = this.form.gender
      this.req({
        url: '/user/editUserWeb',
        method: 'get',
        params: {
          id: user_id,
          username: username,
          gender: gender
        }
      }).then(res => {
        console.log(res)

        this.$message({

          message: '信息修改成功',
          type: 'success'

        });

      })
    }
  }
}
</script>
<style >

.container{

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 300px;

}

.title{

  margin-bottom: 50px;
  font-size: 26px;
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;

}

</style>
