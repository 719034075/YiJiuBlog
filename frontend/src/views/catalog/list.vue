<template>
    <div class="app-container">
        <sticky :className="'sub-navbar'">
            <el-button style="margin-left: 10px;" type="success" @click="createCatalog">新建
            </el-button>
        </sticky>
        <el-table :data="list" v-loading.body="listLoading" border fit highlight-current-row style="width: 100%">

            <el-table-column min-width="300px" label="名称">
                <template slot-scope="scope">
                    <span>{{ scope.row.name }}</span>
                </template>
            </el-table-column>

            <el-table-column width="120px" align="center" label="数量">
                <template slot-scope="scope">
                    <span>{{ scope.row.amount }}</span>
                </template>
            </el-table-column>

            <el-table-column align="center" label="操作" width="240">
                <template slot-scope="scope">
                    <el-button type="primary" size="small" icon="el-icon-edit" @click="editCatalog(scope.row.id)">编辑
                    </el-button>
                    <el-button type="danger" size="small" icon="el-icon-delete" @click="deleteCatalog(scope.row.id)">
                        删除
                    </el-button>
                </template>
            </el-table-column>
        </el-table>

        <div class="pagination-container">
            <el-pagination background @size-change="handleSizeChange" @current-change="handleCurrentChange"
                           :current-page="listQuery.page"
                           :page-sizes="[10,20,30, 50]" :page-size="listQuery.page_size"
                           layout="total, sizes, prev, pager, next, jumper" :total="total">
            </el-pagination>
        </div>
        <el-dialog title="分类" :visible.sync="dialogFormVisible" width="450px">
            <el-form :model="dialogForm">
                <el-form-item label="名称" label-width="50px" prop="name">
                    <el-input placeholder="请输入名称" v-model="dialogForm.name"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="submitCatalog">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import { fetchList, deleteCatalog, fetchCatalog, createCatalog, updateCatalog } from '@/api/catalog'
    import Sticky from '@/components/Sticky' // 粘性header组件

    const defaultForm = {
        name: '',
        id: undefined
    };
    export default {
        name: 'catalogList',
        components: { Sticky },
        data() {
            return {
                list: null,
                total: 0,
                listLoading: true,
                dialogForm: Object.assign({}, defaultForm),
                isEdit: false,
                dialogFormVisible: false,
                listQuery: {
                    page: 1,
                    page_size: 10
                }
            }
        },
        filters: {
            statusFilter(status) {
                const statusMap = {
                    published: 'success',
                    draft: 'info',
                    deleted: 'danger'
                };
                return statusMap[status]
            }
        },
        created() {
            this.getList()
        },
        methods: {
            getList() {
                this.listLoading = true;
                fetchList(this.listQuery).then(response => {
                    this.list = response.data.results;
                    this.total = response.data.total;
                    this.listLoading = false
                }).catch(err => {
                    console.log(err)
                })
            },
            createCatalog() {
                this.dialogFormVisible = true;
                this.isEdit = false;
            },
            editCatalog(id) {
                this.dialogFormVisible = true;
                this.isEdit = true;
                fetchCatalog(id).then(response => {
                    this.dialogForm = response.data;
                }).catch(err => {
                    console.log(err)
                })
            },
            submitCatalog() {
                this.dialogFormVisible = false;
                if (this.isEdit) {
                    updateCatalog(this.dialogForm).then(response => {
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
                        location.reload()
                    }).catch(err => {
                        console.log(err);
                    });
                } else {
                    createCatalog(this.dialogForm).then(response => {
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
                        location.reload()
                    }).catch(err => {
                        console.log(err);
                    });
                }
            },
            deleteCatalog(id) {
                this.$confirm('此操作将永久删除该分类, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    deleteCatalog(id).then(response => {
                        this.$message({
                            type: 'success',
                            message: response.data.message
                        });
                        location.reload()
                    }).catch(err => {
                        console.log(err)
                    })
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
            },
            handleSizeChange(val) {
                this.listQuery.page_size = val;
                this.getList()
            },
            handleCurrentChange(val) {
                this.listQuery.page = val;
                this.getList()
            }
        }
    }
</script>

<style scoped>
    .edit-input {
        padding-right: 100px;
    }

    .cancel-btn {
        position: absolute;
        right: 15px;
        top: 10px;
    }
</style>
