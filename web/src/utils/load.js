import sProxy from './proxy'
import Bus from './bus'
import { ToastPlugin } from 'vux'
import '../style.css'


export function load (Vue) {
  Vue.use(sProxy)
  Vue.use(Bus)
  Vue.use(ToastPlugin)

  const FastClick = require('fastclick')
  FastClick.attach(document.body)
}
