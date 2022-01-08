<template>
  <div class="container-photo">
    <div class="left-option">
      <el-form>
        <el-form-item label="模型选择">
          <el-select v-model="modules" placeholder="请选择合适的模型">
            <el-option label="yolov3-spp3(高准确度）" value="yolov3-spp3" />
            <el-option label="yolov3-tiny(高帧数)" value="yolov3-tiny" />
            <el-option label="smoke-yolov5s" value="mask-yolov5s" />
            <el-option label="smoke-yolov5m" value="mask-yolov5m" />
          </el-select>
        </el-form-item>
        <el-form-item style="margin-left:68px;">
          <el-button type="primary" style="width:200px;" @click="onSubmit">开始检测</el-button>
        </el-form-item>
        <el-form-item style="margin-left:68px;">
          <el-button type="primary" style="width:200px;" @click="offSubmit">关闭检测</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="right-present">
      <i v-if="!showCamera" class="el-icon-video-camera" style="font-size:80px;" />
      <!-- <video id="iv" src="" autoplay="autoplay" height="600px" width="800px" /> -->
      <img v-if="showCamera" id="cameraImg" :src="cameraUrl" alt="" srcset="">
    </div>
  </div>
</template>
<script>
export default {
  data: function() {
    return {

      modules: '',
      fileList: [],
      cameraUrl: 'http://localhost:81/api/output/camera.jpg?ranadom=' + (Math.random() * 100 + 1),
      showCamera: false

    }
  },
  mounted() {
    const that = this
    setInterval(() => {
      console.log('1')
      that.cameraUrl = 'http://localhost:81/api/output/camera.jpg?ranadom=' + (Math.random() * 100 + 1)
      console.log(that.cameraUrl)
    }, 400)
  },
  methods: {
    onSubmit() {
      const that = this
      that.showCamera = true
      this.req({
        url: '/file/camera',
        methods: 'get',
        params: {
          model: that.modules
        }
      }).then(res => {
        console.log(res)
      })
    },
    offSubmit() {
      this.showCamera = false
      this.req({
        url: '/file/offcamera',
        methods: 'get',
        params: {
        }
      }).then(res => {
        console.log(res)
      })
    },
    submitUpload() {
      this.$refs.upload.submit()
    },
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePreview(file) {
      console.log(file)
    }
  }
}

// const img = document.getElementById('cameraImg')
// let i = 0
// setInterval(function() {
//   img.src = 'http://localhost:81/api/output/camera.jpg?ranadom=' + (Math.random() * 100 + 1)
//   i++
//   console.log(i)
// }, 1000)

</script>

<style>

.container-photo{

  display: flex;
  flex-direction: row;
  height: 80vh;
  margin: 30px;

}

.left-option{
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex: 1;
}

.right-present{
  flex: 2;
  border: dotted #000000;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>
