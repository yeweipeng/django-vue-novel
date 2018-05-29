<template>
  <div id="app">
    <transition :name="transitionName">
    <router-view></router-view>
    </transition>
    <loading text="加载中..." v-model="loading" position="fixed"></loading>
  </div>
</template>

<script>
import { Loading } from 'vux'
export default {
  name: 'app',
  components: {
    Loading
  },
  data () {
    return {
      loading: false,
      transitionName: 'slide-right'
    }
  },
  created: function() {
    this.$bus.$on('loading:show', () => this.loading = true)
    this.$bus.$on('loading:hide', () => this.loading = false)
  },
  watch: {
    '$route': function(to, from) {
      this.transitionName = to.path == '/index' ? 'slide-left' : 'slide-right'
      if (from.path == '/') {
        this.transitionName = 'fade'
      }
      if (from.name == 'tool-instance' || from.name == 'flow-instance') {
        this.transitionName = 'slide-left'
      }
    }
  }
}
</script>

<style>
  .slide-right-enter-active, .slide-right-leave-active,
  .slide-left-enter-active, .slide-left-leave-active {
    transition: all .4s linear;
  }
  .slide-right-enter, .slide-right-leave-active {
    opacity: 0;
    transform: translateX(-400px);
  }
  .slide-left-enter, .slide-left-leave-active {
    opacity: 0;
    transform: translateX(400px);
  }
  .fade-enter-active, .fade-leave-active {
    transition: all 0.4s ease;
  }
  .fade-enter, .fade-leave-active {
    opacity: 0;
  }
  body {
    background-color: #f5f5f5;
  }
  .margin-border {
    margin: 10px 12px!important;
  }
  .none-space {
    margin: 0;
    padding: 0!important;
  }
  #app, button {
    font-family: 'Microsoft YaHei';
  }
  hr.white {
    border-color: #FFF
  }
  button.btn-blue {
    background-color: #0079ff ;/*#00a3f7;*/
    color: #FFF;
  }
  a {
    text-decoration: none;
  }
  .tab-blue.vux-button-group > a:first-child {
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
  }
  .tab-blue.vux-button-group > a:last-child {
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
  }
  .tab-blue.vux-button-group > a.vux-button-group-current,
  .tab-blue.vux-button-group > a.hover,
  .tab-blue.vux-button-group > a:active {
    border-color: #0079ff;
    color: #FFF;
    background: #0079ff;
  }
  .tab-blue.vux-button-group > a {
    border-color: #0079ff;
  }

  .flex {
    display: flex;
    flex-direction: row;
  }
  .flex-item-1 {
    flex-grow: 1
  }
  .flex-item-4 {
    flex-grow: 4
  }
  .flex-column {
    flex-direction: column;
  }
  .flex-card {
    align-items: center;
    color: #FFF;
    box-shadow: 6px 6px 6px 0px #fbbfbf;
    font-family: 'Microsoft YaHei'
  }
  .text-center {
    text-align: center;
  }
  .text-right {
    text-align: right;
  }
  .flex-card-content {
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    padding-left: 4px;
    padding-bottom: 2px;
    color: #000;
    background-color: #FFF;
  }
  .font12 {
    font-size: 12px;
  }
  .flex-card-success-status {
    background-color: #82af6f;
  }
  .flex-card-warn-status {
    background-color: #f89406;
  }
  .flex-card-waiting-status {
    background-color: #d15b47;
  }
  .small-item {
    color: gray;
    font-size: 12px;
  }
  i.white {
    color: #FFF;
  }
  .margin-t-5 {
    margin-top: 5px;
  }
  .card-wrap {
    /*border: 1px solid #DDD;*/
    margin: 10px;
    border-radius: 6px;
    /*margin-top: 20px;*/
  }
  .flex-space-between {
    justify-content: space-between;
  }
  .flex-end {
    justify-content: flex-end;
  }
  .status-table {
    padding-top: 5px;
    padding-bottom: 5px;
  }
  .status-table>div {
    font-size: 14px;
  }
  .status-table>div>span {
    color: #f74c31;
  }
  .ip-summary {
    font-size: 14px;
    color: #999;
  }
  .date-time {
    padding-right: 5px;
  }
  .gray {
    color:grey;
  }
</style>

<style lang="less">
@import '~vux/src/styles/1px.less';
</style>
