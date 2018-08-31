<template>
  <div>
    <card-item></card-item>
    <card-item></card-item>
    <card-item></card-item>
    <card-item></card-item>
    <card-item></card-item>
    <card-item></card-item>
    <card-item></card-item>
    <card-item></card-item>
    <card-item></card-item>
  </div>
</template>

<script>
  import CardItem from './CardItem'
    export default {
        name: "blog-list",
        data: () => ({}),
      components:{
        CardItem
      }
    }
</script>

<style scoped lang='scss'>
</style>
