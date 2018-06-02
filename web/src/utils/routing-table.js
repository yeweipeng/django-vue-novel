export const routes = [
  // { path: '/empty',  name: 'empty',   component: (resolve) => require(['../page/status.vue'], resolve) },
  // { path: '/noauth',  name: 'noauth',   component: (resolve) => require(['../page/status.vue'], resolve) },
  // { path: '/error',  name: 'error',   component: (resolve) => require(['../page/status.vue'], resolve) },
  
  // { path: '/test',   name: 'test',  component: (resolve) => require(['../page/test.vue'], resolve) },
  { path: '/index',  name: 'index',   component: (resolve) => require(['../page/index.vue'], resolve) },
  // { path: '/ip',     name: 'ip', component: (resolve) => require(['../page/ip.vue'], resolve) },
  // { path: '/menus',     component: (resolve) => require(['../page/menus.vue'], resolve) },
  { path: '/book/:id', name: 'book', component: (resolve) => require(['../page/book.vue'], resolve)},
  { path: '/book/:id/:chapter', name: 'chapter', component: (resolve) => require(['../page/chapter.vue'], resolve)},
  // { path: '/flow/:id', name: 'flow', component: (resolve) => require(['../page/task.vue'], resolve)},
  // { path: '/tool/:id/:instance', name: 'tool-instance', component: (resolve) => require(['../page/tool-detail.vue'], resolve)},
  // { path: '/flow/:id/:instance', name: 'flow-instance', component: (resolve) => require(['../page/tool-detail.vue'], resolve)},
  // { path: '/approval', name: 'approval', component: (resolve) => require(['../page/approval.vue'], resolve)},
  { path: '*', redirect: '/index' }
]
