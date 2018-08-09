<template>
    <div class="components-container">
        <div v-html="html"></div>
    </div>
</template>

<script>
    import { fetchArticle } from '@/api/blog'

    export default {
        name: "view",
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
        mounted() {
            // this.markdown2Html()
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

</style>