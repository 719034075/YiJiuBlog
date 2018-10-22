<template>
  <div class="blog-head">
    <img class="fl" :src="egg"/>
    <h5 class="fl nav">
      <router-link to="/homepage">HOME</router-link>
    </h5>
    <h5 class="fl nav">
      <router-link to="/blog">BLOG</router-link>
      </h5>
    <h5 class="fl nav">ABOUT</h5>
    <!--<h1 class="fl title">my tea egg</h1>-->
  </div>
</template>

<script>
  import egg from '@/assets/pictures/eggs.svg'
    export default {
        name: "blog-head",
        data: () => ({
          egg
        }),
    }
</script>

<style scoped lang='scss'>
  @font-face {
    font-family: "Futura LT Book";
    src: url("../../../assets/fonts/FuturaLT-Book.otf") format('truetype');
  }

  .blog-head{
    height: 75px;
  }

  .fl{
    float: left;
  }

  .nav{
    margin-top: 35px;
    font-family: "Futura LT Book", "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Hiragino Sans GB", "Heiti SC", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
    margin-left: 5px;
    margin-right: 20px;
  }
</style>
