import axios from 'axios'
// import { Message } from 'element-ui'
// import store from '@/store'
// import { getToken } from '@/utils/auth'

// create an axios instance
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
const service = axios.create({
  // baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
  baseURL: 'http://localhost:81/api',
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 80000000 // request timeout
})

// service.interceptors.response.use(
//   response => {
//     const res = response.data
//     // 如果服务器的状态码不为200，说明请求异常，应给出错误提示。
//     if (res.code !== 200) {
//       Message({
//         message: res.msg || 'Error check your token or method',
//         type: 'error',
//         duration: 2 * 1000
//       })
//       return Promise.reject(new Error(res.msg || 'Error'))
//     } else {
//       return res
//     }
//   },
//   error => {
//     console.log('err' + error) // for debug
//     Message({
//       message: error.message,
//       type: 'error',
//       duration: 2 * 1000
//     })
//     return Promise.reject(error)
//   }
// )

export default service
