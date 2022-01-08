<template>
  <el-row :gutter="160" class="panel-group">
    <el-col :xs="16" :sm="16" :lg="24" class="card-panel-col">
      <div class="card-panel">
        <div class="card-panel-icon-wrapper icon-mask">
          <svg-icon icon-class="mask" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
            口罩识别系统
          </div>
        </div>
      </div>
    </el-col>
  </el-row>
</template>
<script>
export default {
  props: {
    username: {
      type: String,
      default: ''
    }
  }

}
</script>
<style lang="scss" scoped>
.panel-group {
  margin-top: 18px;

  .card-panel-col {
    margin-bottom: 32px;
  }

  .card-panel {
    height: 108px;
    cursor: pointer;
    font-size: 12px;
    position: relative;
    overflow: hidden;
    color: #666;
    background: #fff;
    box-shadow: 4px 4px 40px rgba(0, 0, 0, .05);
    border-color: rgba(0, 0, 0, .05);

    &:hover {
      .card-panel-icon-wrapper {
        color: #fff;
      }

      .icon-mask {
        background: #304156;
      }

      .rectangle{

        width: 1000px;

      }

    }

    .card-panel-icon-wrapper {
      float: left;
      margin: 14px 0 0 14px;
      padding: 16px;
      transition: all 0.38s ease-out;
      border-radius: 6px;
    }

    .card-panel-icon {
      float: left;
      font-size: 48px;
    }

    .card-panel-description {
      float: left;
      font-weight: bold;
      margin: 26px;
      margin-left: 60px;

      .card-panel-text {
        // line-height: 18px;
        color: rgba(0, 0, 0, 0.45);
        font-size: 36px;
        letter-spacing: 10px;
        // margin-bottom: 12px;
      }

      .card-panel-num {
        font-size: 20px;
      }
    }

        .username-welcom{

      font-size: 36px;
      float: right;

    }

  }
}
</style>
