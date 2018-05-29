let Vue

var Bus = {
  installed: false
  // bus: new Vue({})
}

Bus.install= function(externalVue) {
  if (Bus.installed) {
    console.error('Bus already installed')
    return
  }
  Vue = externalVue
  Vue.prototype.$bus = new Vue({})
  Bus.installed = true
}

export default Bus
