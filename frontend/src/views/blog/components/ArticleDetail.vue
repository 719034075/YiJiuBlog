<template>
    <div class="createPost-container">
        <el-form class="form-container" :model="postForm" :rules="rules" ref="postForm">
            <sticky :className="'sub-navbar'">
                <el-button v-loading="loading" style="margin-left: 10px;" type="success" @click="submitForm">发布
                </el-button>
            </sticky>
            <div class="createPost-main-container">
                <el-form-item style="margin-bottom: 40px;" prop="title">
                    <MDinput name="name" v-model="postForm.title" required :maxlength="100">
                        标题
                    </MDinput>
                </el-form-item>
                <el-form-item style="margin-bottom: 40px;" label-width="45px" label="摘要:">
                    <el-input type="textarea" class="article-textarea" :rows="1" autosize placeholder="请输入内容"
                              v-model="postForm.abstract">
                    </el-input>
                    <span class="word-counter" v-show="contentShortLength">{{contentShortLength}}字</span>
                </el-form-item>
                <div class="editor-container">
                    <markdown-editor id="editor" ref="editor" v-model="postForm.content" :height="300"
                                     :zIndex="20"></markdown-editor>
                </div>
            </div>
        </el-form>
    </div>
</template>

<script>
    import MarkdownEditor from '@/components/MarkdownEditor'
    import MDinput from '@/components/MDinput'
    import Sticky from '@/components/Sticky' // 粘性header组件
    import { fetchArticle, createArticle, updateArticle } from '@/api/blog'

    const defaultForm = {
        title: '', // 文章题目
        content: '', // 文章内容
        abstract: '', // 文章摘要
        id: undefined,
    };

    export default {
        name: 'articleDetail',
        components: { MarkdownEditor, MDinput, Sticky },
        props: {
            isEdit: {
                type: Boolean,
                default: false
            }
        },
        data() {
            const validateRequire = (rule, value, callback) => {
                if (value === '') {
                    this.$message({
                        message: rule.field + '为必传项',
                        type: 'error'
                    });
                    callback(null)
                } else {
                    callback()
                }
            };
            return {
                postForm: Object.assign({}, defaultForm),
                loading: false,
                rules: {
                    title: [{ validator: validateRequire }],
                    content: [{ validator: validateRequire }],
                }
            }
        },
        computed: {
            contentShortLength() {
                return this.postForm.abstract.length
            }
        },
        created() {
            if (this.isEdit) {
                const id = this.$route.params && this.$route.params.id;
                this.fetchData(id)
            } else {
                this.postForm = Object.assign({}, defaultForm)
            }
        },
        methods: {
            fetchData(id) {
                fetchArticle(id).then(response => {
                    this.postForm = response.data;
                }).catch(err => {
                    console.log(err)
                })
            },
            createBlog(){
                createArticle(this.postForm).then(response => {
                    const obj = {};
                    if (response.success) {
                        obj.title = '成功';
                        obj.type = 'success';
                    } else {
                        obj.title = '失败';
                        obj.type = 'warning';
                    }
                    this.$notify({
                        title: obj.title,
                        message: response.message,
                        type: obj.type,
                        duration: 2000
                    });
                    this.$router.push({ path: '/blog/list' })
                }).catch(err => {
                    console.log(err);
                });
            },
            editBlog(){
                updateArticle(this.postForm).then(response => {
                    const obj = {};
                    if (response.success) {
                        obj.title = '成功';
                        obj.type = 'success';
                    } else {
                        obj.title = '失败';
                        obj.type = 'warning';
                    }
                    this.$notify({
                        title: obj.title,
                        message: response.message,
                        type: obj.type,
                        duration: 2000
                    });
                    this.$router.push({ path: '/blog/list' })
                }).catch(err => {
                    console.log(err);
                });
            },
            submitForm() {
                console.log(this.postForm);
                this.$refs.postForm.validate(valid => {
                    if (valid) {
                        this.loading = true;
                        if(this.isEdit){
                            this.editBlog();
                        }else {
                            this.createBlog();
                        }
                        this.loading = false
                    } else {
                        console.log('error submit!!');
                        return false
                    }
                })
            },
        }
    }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
    @import "src/styles/mixin.scss";

    .createPost-container {
        position: relative;
        .createPost-main-container {
            padding: 40px 45px 20px 50px;
            .editor-container {
                min-height: 300px;
                margin: 0 0 30px;
            }
        }
        .word-counter {
            width: 40px;
            position: absolute;
            right: -10px;
            top: 0px;
        }
    }
</style>
