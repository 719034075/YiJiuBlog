<template>
  <div class="createPost-container">
    <el-form class="form-container" :model="postForm" :rules="rules" ref="postForm">
      <sticky :className="'sub-navbar'">
        <el-button v-loading="loading" style="margin-left: 10px;" type="success" @click="submitForm">保存
        </el-button>
      </sticky>
      <div class="createPost-main-container">
        <el-form-item style="margin-bottom: 40px;" prop="title">
          <MDinput name="name" v-model="postForm.title" required :maxlength="100">
            标题
          </MDinput>
        </el-form-item>
        <el-row class="postInfo-container">
          <el-col :span="4">
            <el-form-item label-width="45px" label="作者:" class="postInfo-container-item">
              <el-input placeholder="请输入作者" v-model="postForm.author" clearable>
              </el-input>
            </el-form-item>
          </el-col>
          <el-col :span="5">
            <el-form-item label-width="80px" label="分类:" class="postInfo-container-item">
              <el-select v-model="postForm.catalog" placeholder="请选择分类">
                <el-option v-for="item in catalog" :key="item.id" :label="item.name" :value="item.id"/>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="5">
            <el-form-item label-width="80px" label="状态:" class="postInfo-container-item">
              <el-select v-model="postForm.status" placeholder="请选择状态">
                <el-option v-for="item in status" :key="item.value" :label="item.label" :value="item.value"/>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
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
  import {fetchArticle, createArticle, updateArticle} from '@/api/article'
  import {fetchCatalogs} from '@/api/catalog'

  const defaultForm = {
    status: 'draft',
    title: '', // 文章题目
    content: '', // 文章内容
    abstract: '', // 文章摘要
    author: '',
    catalog: '',
    id: undefined,
  };

  export default {
    name: 'articleDetail',
    components: {MarkdownEditor, MDinput, Sticky},
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
        status: [{
          value: 'draft',
          label: '草稿'
        }, {
          value: 'published',
          label: '发布'
        }],
        catalog: [],
        rules: {
          title: [{validator: validateRequire}],
          content: [{validator: validateRequire}],
        }
      }
    },
    computed: {
      contentShortLength() {
        return this.postForm.abstract.length
      }
    },
    created() {
      this.fetchCatalog();
      if (this.isEdit) {
        const id = this.$route.params && this.$route.params.id;
        this.fetchData(id);
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
      fetchCatalog() {
        fetchCatalogs().then(response => {
          this.catalog = response.data.results;
        }).catch(err => {
          console.log(err)
        })
      },
      createBlog() {
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
          this.$router.push({path: '/article/list'})
        }).catch(err => {
          console.log(err);
        });
      },
      editBlog() {
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
          this.$router.push({path: '/article/list'})
        }).catch(err => {
          console.log(err);
        });
      },
      submitForm() {
        this.$refs.postForm.validate(valid => {
          if (valid) {
            this.loading = true;
            if (this.isEdit) {
              this.editBlog();
            } else {
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
      .postInfo-container {
        position: relative;
        @include clearfix;
        margin-bottom: 10px;
        .postInfo-container-item {
          float: left;
        }
      }
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
