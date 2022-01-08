<template>
  <div class="container-photo">
    <div class="left-option">
      <el-form>
        <el-form-item label="模型选择">
          <el-select v-model="modules" placeholder="请选择合适的模型">
            <el-option label="yolov3-spp3(高准确度）" value="yolov3-spp3" />
            <el-option label="tolov3-tiny(高帧数)" value="yolov3-tiny" />
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
      <el-upload
        class="avatar-uploader el-upload--text"
        action="http://localhost:81/api/file/video"
        :show-file-list="false"
        :on-success="handleVideoSuccess"
        :before-upload="beforeUploadVideo"
        :on-progress="uploadVideoProcess"
      >
        <video
          v-if="videoForm.Video !='' && videoFlag == false"
          :src="videoForm.Video"
          class="avatar"
          controls="controls"
          height="600px"
          width="800px"
        >您的浏览器不支持视频播放</video>
        <i
          v-else-if="videoForm.Video =='' && videoFlag == false"
          class="el-icon-plus avatar-uploader-icon"
        />
        <el-progress
          v-if="videoFlag == true"
          type="circle"
          :percentage="videoUploadPercent"
          style="margin-top:30px;"
        />
        <P class="text">请保证视频格式正确，且不超过10M</P>
        <el-button v-if="videoFlag == true" size="small" type="primary">点击上传</el-button>
      </el-upload>

      <!-- <img src="" alt="" srcset=""> -->
    </div>
  </div>
</template>
<script>
export default {
  data: function() {
    return {
      modules: '',
      uploadUrl: '',
      videoForm: {
        Video: ''
      },
      videoFlag: true,
      videoUploadPercent: 0,
      videoName: ''
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
        url: '/file/checkvideo',
        methods: 'get',
        params: {
          model: that.modules,
          videoName: that.videoName
        }
      }).then((res) => {
        console.log(res)
        // this.photoUrl = res.data.imageUrl
        this.videoForm['Video'] = res.data.videoUrl
        loading.close()
      })
    },
    beforeUploadVideo(file) {
      const isLt10M = file.size / 1024 / 1024 < 10
      if (
        [
          'video/mp4',
          'video/ogg',
          'video/flv',
          'video/avi',
          'video/wmv',
          'video/rmvb'
        ].indexOf(file.type) == -1
      ) {
        this.$message.error('请上传正确的视频格式')
        return false
      }
      if (!isLt10M) {
        this.$message.error('上传视频大小不能超过10MB哦!')
        return false
      }
    },
    uploadVideoProcess(event, file, fileList) {
      this.videoFlag = true
      console.log('percentage', file.percentage)
      this.videoUploadPercent = file.percentage.toFixed(0)
    },
    handleVideoSuccess(res, file) {
      this.videoUploadPercent = 100
      this.videoFlag = false
      console.log(res)
      this.videoForm['Video'] = res.videoUrl
      this.videoName = res.videoName
    }
  }
}
</script>
<style>
.container-photo {
  display: flex;
  flex-direction: row;
  height: 80vh;
  margin: 30px;
}

.left-option {
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex: 1;
}

.right-present {
  flex: 2;
  border: dotted #000000;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
