<template>
    <el-card class="box-card">
        <div slot="header" class="clearfix">
            <span class="title">{{item.title}}</span>
        </div>
        <div class="text item">
            {{item.abstract}}
            <router-link :to="'/blog/'+item.id">阅读全文</router-link>
        </div>
    </el-card>
</template>

<script>
    export default {
        name: "card-item",
        props: {
            item: {
                type: Object,
                default: {}
            }
        },
        data: () => ({}),
    }
</script>

<style scoped lang='scss'>
    $gray-text: #999;
    $red: #f33;
    .title {
        font-weight: 700;
        font-size: 1.5em;
    }

    .text {
        font-size: 0.9em;
    }

    .item {
        margin-bottom: 18px;
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }

    .clearfix:after {
        clear: both
    }

    .box-card {
        width: 100%;
        margin-top: 0;
        margin-bottom: 48px;
    }

    a {
        color: $gray-text;
        text-decoration: none;
        &:hover {
            color: $red;
        }
    }
</style>
