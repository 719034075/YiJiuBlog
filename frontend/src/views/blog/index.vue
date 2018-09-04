<template>
    <div class="blog-page">
        <blog-head></blog-head>
        <div v-loading.body="listLoading" >
            <card-item v-for="item in list" :key="item.id" :item="item"></card-item>
        </div>
        <el-row class="">
            <el-col :offset="9">
                <el-pagination
                        background @current-change="handleCurrentChange"
                        :current-page="listQuery.page"
                        :page-sizes="[10,20,30, 50]" :page-size="listQuery.page_size"
                        :total="total"
                        layout="prev, pager, next,->"
                >
                </el-pagination>
            </el-col>
        </el-row>
        <blog-foot></blog-foot>
        <back-to-top transitionName="fade" :customStyle="myBackToTopStyle" :visibilityHeight="300"
                     :backPosition="0"></back-to-top>
    </div>
</template>

<script>
    import BlogHead from './components/BlogHead'
    import BlogFoot from './components/BlogFoot'
    import BackToTop from '@/components/BackToTop'
    import CardItem from './components/CardItem'

    import { fetchPublishedList } from '@/api/article'


    export default {
        name: "blog",
        data: () => ({
            myBackToTopStyle: {
                right: '50px',
                bottom: '50px',
                width: '40px',
                height: '40px',
                'border-radius': '20px',
                'line-height': '45px', // 请保持与高度一致以垂直居中 Please keep consistent with height to center vertically
                background: '#e7eaf1'// 按钮的背景颜色 The background color of the button
            },
            listLoading: true,
            list: null,
            total: 0,
            listQuery: {
                page: 1,
                page_size: 10
            }
        }),
        components: {
            BlogHead,
            BlogFoot,
            BackToTop,
            CardItem
        },
        created() {
            this.getList()
        },
        methods: {
            getList() {
                this.listLoading = true;
                fetchPublishedList(this.listQuery).then(response => {
                    this.list = response.data.results;
                    this.total = response.data.total;
                    this.listLoading = false
                }).catch(err => {
                    console.log(err)
                })
            },
            handleCurrentChange(val) {
                this.listQuery.page = val;
                this.getList()
            }
        }
    }
</script>

<style scoped lang='scss'>
    .blog-page {
        margin: 0 auto;
        padding: 0;
        width: 100%;
        max-width: 900px;
    }
</style>
