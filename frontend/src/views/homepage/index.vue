<template>
  <transition name="el-fade-in-linear">
    <div class="wrapper" v-if="show">
      <h1 class="title">Who Moved My Tea Egg ?</h1>
      <div style="height: 250px">
        <div class="egg"></div>
      </div>
      <p><router-link to="/blog">Blog</router-link></p>
      <p><a>About Me</a></p>
    </div>
  <!--</el-collapse-transition>-->
  </transition>
</template>

<script>
  export default {
    name: "homepage",
    data: () => ({
      show: false
    }),
    mounted() {
      this.show = true
    }
  }
</script>

<style scoped lang='scss'>

  @font-face {
    font-family: "Zorus Serif";
    src: url("../../assets/fonts/Zorus_Serif.otf");
  }

  $gray: #DDD;
  $gray-text: #999;
  $black: #333;
  $white: #FFF;
  $red: #f33;

  .wrapper {
    position: fixed;
    width: 320px;
    height: 568px;
    text-align: center;
    top: 30%;
    left: 50%;
    margin-left: -160px;
    margin-top: -160px;
    user-select: none;
  }

  .title {
    font-family: "Zorus Serif", "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Hiragino Sans GB", "Heiti SC", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
    font-size: 50px;
  }

  .egg {
    border: 5px solid $black;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 200px;
    height: 250px;
    background: $white;
    border-top-left-radius: 50% 60%;
    border-top-right-radius: 50% 60%;
    border-bottom-left-radius: 50% 40%;
    border-bottom-right-radius: 50% 40%;
    box-shadow: inset -10px -5px $gray;
    animation: wobble 8s linear infinite;
    transform-origin: 0 50%;
  }

  p {
    font-size: 14px;
    line-height: 2em;
    margin: 0;
    letter-spacing: 2px;
  }

  a {
    color: $gray-text;
    text-decoration: none;
    &:hover {
      color: $red;
    }
  }

  @keyframes wobble {
    0% {
      transform: rotate(0deg) translate(-50%, -50%);
    }
    25% {
      transform: rotate(5deg) translate(-50%, -50%);
    }
    75% {
      transform: rotate(-5deg) translate(-50%, -50%);
    }
    100% {
      transform: rotate(0deg) translate(-50%, -50%);
    }
  }
</style>
