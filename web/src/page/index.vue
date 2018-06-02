<template>
  <div>
    <search placeholder="搜索" cancelText="取消" :auto-fixed="false" v-model="search_keyword" @on-submit="query_book"></search>

    <msg v-if="books.length == 0" icon="info" title="这里空空如也" class="empty-book-msg"></msg>
    <group gutter=0>
      <swipeout-item transition-mode="follow" v-for="book in books" :key="book.id">
        <div slot="right-menu">
          <swipeout-button v-if="book.is_save" type="warn">删除</swipeout-button>
          <swipeout-button v-else background-color="#d0ba32">收藏</swipeout-button>
        </div>
        <cell slot="content" :link="'book/' + book.id + '/' + book.last_read_chapter_id" :inline-desc="book.last_read_chapter_name" class='book-item'>
          <span slot="title">{{book.name}} <badge v-show="book.has_latest"></badge></span>
          <img class="book-img" slot="icon" :src="book.img_url"/>
        </cell>
      </swipeout-item>
    </group>

  </div>
</template>

<script>
import { Group, Cell, Search, Badge, Swipeout, SwipeoutItem, SwipeoutButton, Msg } from 'vux'
import axios from 'axios'

export default {
  components: {
    Cell, Group, Search, Badge, Msg,
    Swipeout, SwipeoutItem, SwipeoutButton
  },
  data () {
    return {
      search_keyword: '',
      books: []
    }
  },
  methods: {
    query_book () {
      let kw = _.trim(this.search_keyword)
      if (kw == '') {
        return
      }
      this.$vux.loading.show({
        text: 'Loading'
      })
      axios.get('/book/api/get_books', {
        params: {
          user_id: 1,
          search_word: kw
        }
      }).then((data) => {
        this.$vux.loading.hide()
        let result = _.differenceBy(data.data, this.books, 'id')
        this.books = result.concat(this.books)
      })
    }
  },
  computed: {
  },
  created: function() {
    axios.get('/book/api/get_like_book_list').then((data) => {
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
  .empty-book-msg {
    color: gray;
  }
  .weui-cells>.vux-swipeout-item:first-child .book-item::before {
    display: none;
  }
  div.weui-cell.book-item::before {
    display: block;
  }
</style>
