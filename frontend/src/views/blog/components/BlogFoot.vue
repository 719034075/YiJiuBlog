<template>
    <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="6" :offset="1"><div class="copy">Copyright © 2018 Zeu's Blog</div></el-col>
    </el-row>
</template>

<script>
    export default {
        name: "blog-foot"
    }
</script>

<style scoped>
    .el-row{
        height: 120px;
    }
    .el-col{
        margin-top: 40px;
    }
    .copy{
        color: #999;
    }

</style>