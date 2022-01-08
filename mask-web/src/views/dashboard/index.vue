<template>
  <div class="dashboard-container">
    <WelcomPanel />
    <PanelGroup />
    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
      <line-chart :chart-data="lineChartData" />
    </el-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import PanelGroup from './components/panelGroup'
import LineChart from './components/lineChart'
import WelcomPanel from './components/welcomPanel'

export default {
  name: 'Dashboard',
  components: {
    PanelGroup,
    LineChart,
    WelcomPanel
  },
  data() {
    return {

      lineChartData: {
        hatCount: [52,8,34,100, 110,120, 161, 134, 105, 160, 165, 200, 220, 161, 184, 105, 160, 165, 261, 234, 205, 260,220,210],
        personCount: [150,100,120, 82, 91, 154, 162, 140, 145, 100, 86, 61, 134, 99, 110, 160, 161, 134, 105, 160, 165,150,130,62]
      }

    }
  },
  mounted(){

    let that = this;

    let mask = new Array(24).fill(0);
    let nomask = new Array(24).fill(0);

    this.req({
        url: '/util/getMaskData',
        method: 'get'
    }).then(res=>{

      console.log("res",res);

      let mask_data = res.data.mask_data;
      for(let item of mask_data){

        console.log(Number(item[2]),item[0],item[1],item);
        mask[Number(item[2])] = item[0];
        nomask[Number(item[2])] = item[1];

      }

      console.log(mask,nomask);

      that.lineChartData.hatCount = mask;
      that.lineChartData.personCount = nomask;

    })

  },
  computed: {
    ...mapGetters([
      'name'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
