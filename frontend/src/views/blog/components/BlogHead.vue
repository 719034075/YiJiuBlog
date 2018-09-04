<template>
  <div>
    <img class="fl" src="/src/assets/pictures/eggs.svg"/>
    <h5 class="fl nav">HOME</h5>
    <h5 class="fl nav">BLOG</h5>
    <h5 class="fl nav">ABOUT</h5>


    <!--<h1 class="fl title">my tea egg</h1>-->
  </div>
</template>

<script>
    export default {
        name: "blog-head",
        data: () => ({}),
    }
</script>

<style scoped lang='scss'>
  @font-face {
    font-family: "Futura LT Book";
    src: url("/src/assets/fonts/Futura_LT_Book.ttf");
  }

  /*.title{*/
    /*font-family: "Futura LT Book", "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Hiragino Sans GB", "Heiti SC", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;*/
    /*color: #2F2E2E;*/
  /*}*/

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
