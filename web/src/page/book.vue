<template>
  <div>
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
        chapters: [{
          id: 1,
          name: '第一百二十章',
          url: 'xxx'
        }]
      }
    },
    methods: {
    },
    created () {
    axios.get('/book/api/get_dir', {
      params : {
        user_id: 1,
        book_id: this.book_id,
      }
    }).then((data) => {
      this.chapters = data.data.chapters.map((item, i) => {
        return {
          id: i,
          name: item.text,
          url: '/book/' + this.book_id + '/' + item.chapter_id
        }
      })
    })
    }
}
</script>

