<template>
  <div class="book-dir-wrap">
    <group :title="book_name">
      <cell v-for="chapter in chapters" :key="chapter.id" :title="chapter.name" :link="chapter.url"></cell>
    </group>
  </div>
</template>
<script>
import {Group, GroupTitle, Cell} from 'vux'
import axios from 'axios'
export default {
  components: {
    Group, GroupTitle, Cell
  },
  data () {
    return {
        book_id: this.$route.params.id,
        book_name: '',
        chapters: []
      }
    },
    methods: {
    },
    created () {
    axios.get('/book/api/get_chapter_list', {
      params : {
        user_id: 1,
        book_id: this.book_id,
      }
    }).then((data) => {
      this.book_name = data.data.book_name
      this.chapters = _.reverse(data.data.chapters.map((item, i) => {
        return {
          id: i,
          name: item.text,
          url: '/book/' + this.book_id + '/' + item.chapter_id
        }
      }))
    })
    }
}
</script>

<style>
  .book-dir-wrap .vux-label {
    font-size: 14px;
  }
</style>

