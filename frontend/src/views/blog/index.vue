<template>
  <div class="blog-page">
    <blog-head></blog-head>
    <blog-list></blog-list>
    <el-row class="">
      <el-col :offset="9">
        <el-pagination
          layout="prev, pager, next,->"
          :total="50">
        </el-pagination>
      </el-col>
    </el-row>
    <back-to-top transitionName="fade" :customStyle="myBackToTopStyle" :visibilityHeight="300"
                 :backPosition="0"></back-to-top>
  </div>
</template>

<script>
  import BlogHead from './components/BlogHead'
  import BlogList from './components/BlogList'
  import BackToTop from '@/components/BackToTop'

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
      }
    }),
    components: {
      BlogHead,
      BlogList,
      BackToTop
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
