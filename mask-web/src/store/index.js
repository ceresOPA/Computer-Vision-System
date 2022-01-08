import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
import app from './modules/app'
import settings from './modules/settings'
import user from './modules/user'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    app,
    settings,
    user
  },
  state: {
    userInfo: localStorage.getItem('userInfo')
  },
  getters,
  // 同步赋值方法
  mutations: {
    SET_USERINFO(state, params) {
      state.userInfo = params
    }
  }
})

export default store
