<template>
  <div>
    <search placeholder="搜索" cancelText="取消" :auto-fixed="false" v-model="search_keyword"></search>

    <group gutter=0>
      <swipeout-item transition-mode="follow" v-for="book in books" :key="book.id">
        <div slot="right-menu">
          <swipeout-button v-if="book.is_save" type="warn">删除</swipeout-button>
          <swipeout-button v-else background-color="#d0ba32">收藏</swipeout-button>
        </div>
        <cell slot="content" :link="'book/' + book.id + '/' + book.last_read_chapter_id" :inline-desc="book.last_read_chapter_name">
          <span slot="title">{{book.name}} <badge v-show="book.has_latest"></badge></span>
          <img class="book-img" slot="icon" :src="book.img_url"/>
        </cell>
      </swipeout-item>
    </group>
    
  </div>
</template>

<script>
import { Group, Cell, Search, Badge, Swipeout, SwipeoutItem, SwipeoutButton } from 'vux'
import axios from 'axios'

// import OverView from 'components/overview'
export default {
  components: {
    Cell, Group, Search, Badge,
    Swipeout, SwipeoutItem, SwipeoutButton
    // OverView
  },
  data () {
    return {
      search_keyword: '',
      books: []
    }
  },
  methods: {
  },
  computed: {
  },
  created: function() {
    axios.get('/book/api/get_like_book_list/').then((data) => {
      this.books = data.data.data
    })
  }
}
</script>

<style>
  .book-img {
    width: 40px;
    margin-right: 10px;
  }
</style>
