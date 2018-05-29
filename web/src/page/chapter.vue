<template>
    <div class="parent">
        <view-box >
            <h4 class="title">{{title}}</h4>
            <p class="chapter-content" v-html="chapter">
            </p>
            <tabbar slot="bottom">
                <tabbar-item link="/index">
                    <i class="fa fa-home"  slot="label"></i>
                </tabbar-item>
                <tabbar-item :link="'/book/' + book_id ">
                    <i class="fa fa-list" slot="label"></i>
                </tabbar-item>
                <tabbar-item>
                    <i class="fa fa-cog" slot="label"></i>
                </tabbar-item>
            </tabbar>
        </view-box>
    </div>
</template>

<script>
import { Tabbar, TabbarItem, ViewBox } from 'vux'
import axios from 'axios'
export default {
  components: {
    Tabbar, TabbarItem, ViewBox
  },
  data () {
      return {
          book_id: this.$route.params.id,
          chapter_id: this.$route.params.chapter,
          chapter: '',
          title: '',
      }
  },
  created () {
    axios.get('/book/api/get_chapter', {
      params : {
        user_id: 1,
        book_id: this.book_id,
        chapter_id: this.chapter_id
      }
    }).then((data) => {
      this.chapter = data.data.content
      this.title = data.data.title
    })
  }
}
</script>

<style>
  .weui-tabbar p.weui-tabbar__label {
      font-size: 26px;
  }
  .title {
      text-align: center;
  }
  .parent {
      height: 100%;
      background: #fbe1ba;
  }
  .chapter-content {
      white-space: pre-wrap;
      padding: 0 16px;
  }
</style>
