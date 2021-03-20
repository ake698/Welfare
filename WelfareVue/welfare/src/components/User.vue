<template>

<div>

  <el-table
    :data="tableData"
    border
    style="width: 100%">
    <el-table-column
      fixed
      prop="id"
      label="ID"
      width="200"
      >
    </el-table-column>
    <el-table-column
      prop="username"
      label="用户账号"
      width="160"
      >
    </el-table-column>
    <el-table-column
      prop="password"
      label="用户密码"
      width="160"
      >
    </el-table-column>
    <el-table-column
      prop="user_type_name"
      label="用户状态"
      width="160"
      >
    </el-table-column>
    <el-table-column
      prop="create_time"
      label="注册时间"
      >
    </el-table-column>
    <el-table-column
      fixed="right"
      label="操作"
      width="400">
      <template slot-scope="scope">
        <el-button v-if="user_type==2" @click="deleteClick(scope.row)" size="mini" type="danger" round>删除</el-button>
      </template>
    </el-table-column>
  </el-table>

</div>
</template>

<script>
import ResourceUpload from './common/ResourceUpload'
  export default {
    components:{ResourceUpload},
    data() {
      return {
        tableData: [],
        user_type: 1,
        avatarVisible: false,
      }
    },
    mounted(){
        this.users();
        this.user_type = this.$store.state.user_type;
        console.log(this.user_type)
    },
    methods: {
      deleteClick(row){
        this.$axios.delete('api/user/' + row.id).then(resp => {
            this.$message({
                    message: resp.data.msg,
                    showClose: true,
                    type: 'success'
            });
            this.users();
        })
      },
      users(){
          this.$axios.get('api/user').then(resp => {
              if(resp.data.status == "200"){
                  this.tableData = resp.data.detail;
                  this.tableData.forEach(element => {
                    element.create_time = element.create_time.replace("T"," ");
                    });
              }else{
                  this.$message({
                    message: resp.data.msg,
                    showClose: true,
                    type: 'error'
                });
              }
          })
        }
    },
    

    
  }
</script>