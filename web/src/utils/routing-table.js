export const routes = [
  // { path: '/empty',  name: 'empty',   component: (resolve) => require(['../page/status.vue'], resolve) },
  // { path: '/noauth',  name: 'noauth',   component: (resolve) => require(['../page/status.vue'], resolve) },
  // { path: '/error',  name: 'error',   component: (resolve) => require(['../page/status.vue'], resolve) },
  
  // { path: '/test',   name: 'test',  component: (resolve) => require(['../page/test.vue'], resolve) },
  { path: '/index',  name: 'index',   component: (resolve) => require(['../page/index.vue'], resolve) },
  { path: '/book/:id', name: 'book', component: (resolve) => require(['../page/book.vue'], resolve)},
  { path: '/book/:id/:chapter', name: 'chapter', component: (resolve) => require(['../page/chapter.vue'], resolve)},
  { path: '*', redirect: '/index' }
]
