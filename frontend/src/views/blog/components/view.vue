<template>
  <div class="components-container">
    <blog-head></blog-head>
    <div v-html="html"></div>
  </div>
</template>

<script>
  import {fetchArticle} from '@/api/article'
  import BlogHead from './BlogHead'


  export default {
    name: "view",
    components:{
      BlogHead
    },
    data() {
      return {
        content: '',
        html: ''
      }
    },
    created() {
      const id = this.$route.params && this.$route.params.id;
      this.fetchData(id)
    },
    methods: {
      fetchData(id) {
        fetchArticle(id).then(response => {
          this.content = response.data.content;
          this.markdown2Html()
        }).catch(err => {
          console.log(err)
        })
      },
      markdown2Html() {
        import('showdown').then(showdown => {
          const converter = new showdown.Converter();
          this.html = converter.makeHtml(this.content)
        })
      }
    }
  }
</script>

<style scoped>
  .components-container {
    margin: 0 auto;
    padding: 0;
    width: 100%;
    max-width: 900px;
  }
</style>
