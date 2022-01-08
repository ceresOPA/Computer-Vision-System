<template>
  <div class="container-photo">
    <div class="left-option">
      <el-form>
        <el-form-item label="模型选择">
          <el-select v-model="modules" placeholder="请选择合适的模型">
            <el-option label="yolov3-spp3(高准确度）" value="yolov3-spp3" />
            <el-option label="yolov3-tiny(高帧数)" value="yolov3-tiny" />
            <el-option label="smoke-yolov5s" value="smoke-yolov5s" />
            <el-option label="smoke-yolov5m" value="mask-yolov5m" />
          </el-select>
        </el-form-item>
        <el-form-item style="margin-left:68px;">
          <el-button type="primary" style="width:200px;" @click="onSubmit">立即检测</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="right-present">
      <div v-if="photoUrl==''||photoUrl==null">
        <el-upload
          class="upload-demo"
          drag
          action="http://localhost:81/api/file/photo"
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :on-success="handleSuccess"
          :before-upload="handleBefore"
        >
          <i class="el-icon-upload" />
          <div class="el-upload__text">请将图片拖到此处，或<em>点击上传</em></div>
          <div slot="tip" class="el-upload__tip">只能上传jpg/png格式的图片，且不超过500kb</div>
        </el-upload>
      </div>
      <img v-if="photoUrl!=null&&photoUrl!=''" :src="photoUrl" alt="" srcset="">
      <el-button v-if="photoUrl!=null&&photoUrl!=''" type="primary" style="width:200px;margin-top:30px" @click="onBack">重新上传</el-button>
    </div>
  </div>
</template>
<script>
export default {
  data: function() {
    return {

      modules: '',
      photoUrl: '',
      imageName: ''

    }
  },
  methods: {
    onSubmit() {
      const that = this

      const loading = this.$loading({
        lock: true,
        text: '检测中...',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      })

      this.req({
        url: '/file/checkphoto',
        methods: 'get',
        params: {
          model: that.modules,
          imageName: that.imageName
        }
      }).then(res => {
        console.log(res)
        this.photoUrl = res.data.imageUrl
        loading.close()
      })
    },
    onBack() {
      this.photoUrl = ''
    },
    handleBefore() {

    },
    submitUpload() {
      this.$refs.upload.submit()
    },
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePreview(file) {
      console.log(file)
    },
    handleSuccess(res, file, fileList) {
      this.photoUrl = res.imageUrl
      this.imageName = res.imageName
      console.log('res', res)
    }
  }
}
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
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

</style>
