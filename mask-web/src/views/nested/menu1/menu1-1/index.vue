<template>
  <div style="padding:30px;">
    <el-alert :closable="false" title="menu 1-12312" type="success">
      <router-view />
    </el-alert>
  </div>
</template>
<script>
export default {
  data: function() {
    return {

    }
  },
  created() {

  }
}
</script>
