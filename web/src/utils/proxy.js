import axios from 'axios'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

// axios.interceptors.request.use(function(req) {
//   this.$bus.$emit('loading:show')
//   return req
// })
//
// axios.interceptors.response.use(function(rsp) {
//   this.$bus.$emit('loading:hide')
//   return rsp
// })

let Vue

function buildProxy (proxyKey, proxyParams) {
  var key_list = [];
  var argsMap = [];
  for (var key in proxyParams) {
    key_list.push(key);
    argsMap.push(encodeURIComponent(key) + '=' + encodeURIComponent(proxyParams[key]))
  }
  argsMap.push('arg_list=' + encodeURIComponent(key_list.join("|")))
  argsMap.push('proxy_key=' + encodeURIComponent(proxyKey))
  return argsMap.join('&');
}

var sProxy = {
  installed: false,
  post: function(proxyKey, proxyParams, proxyUrl = '/service/proxy.cgi') {
    let paramMap = buildProxy(proxyKey, proxyParams)
    return axios.post(proxyUrl, paramMap).then(function(rsp) {
      return rsp.data
    })
  }
}

sProxy.install= function(externalVue) {
  if (this.installed) {
    console.error('$proxy already installed')
    return
  }
  Vue = externalVue
  Vue.prototype.$proxy = this
  this.installed = true
}

export default sProxy
