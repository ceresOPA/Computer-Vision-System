<template>
  <div id="myChart" class="total-class" :style="{width: '100%', height: '400px'}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme

export default {
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '350px'
    },
    autoResize: {
      type: Boolean,
      default: true
    },
    chartData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      chart: null
    }
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      this.setOptions(this.chartData)
    },
    setOptions({ hatCount, personCount } = {}) {
      this.chart.setOption({
        xAxis: {
          data: ['0:00', '1:00','2:00', '3:00','4:00', '5:00','6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00','22:00','23:00'],
          boundaryGap: false,
          axisTick: {
            show: false
          }
        },
        grid: {
          left: 10,
          right: 10,
          bottom: 20,
          top: 30,
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          },
          padding: [5, 10]
        },
        yAxis: {
          axisTick: {
            show: false
          }
        },
        legend: {
          data: ['吸烟人数', '未吸烟人数']
        },
        series: [{
          name: '吸烟人数', itemStyle: {
            normal: {
              color: '#00AC9A',
              lineStyle: {
                color: '#00AC9A',
                width: 2
              }
            }
          },
          smooth: true,
          type: 'line',
          data: hatCount,
          animationDuration: 2800,
          animationEasing: 'cubicInOut'
        },
        {
          name: '未吸烟人数',
          smooth: true,
          type: 'line',
          itemStyle: {
            normal: {
              color: '#ff7675',
              lineStyle: {
                color: '#ff7675',
                width: 2
              }
              // areaStyle: {
              //   color: '#f3f8ff'
              // }
            }
          },
          data: personCount,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }]
      })
    }
  }
}
</script>
