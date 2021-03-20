<template>

  <el-table
    :data="tableData"
    border
    style="width: 100%">
    <el-table-column
      fixed
      prop="id"
      label="ID"
      width="80"
      >
    </el-table-column>
    <el-table-column
      prop="user_name"
      label="发送人"
      >
    </el-table-column>
    <el-table-column
      prop="content"
      label="内容"
      >
    </el-table-column>
    <el-table-column
      prop="activity_name"
      label="所属活动"
      >
    </el-table-column>
    <el-table-column
      prop="create_time"
      label="申请时间"
      >
    </el-table-column>
    <el-table-column
      fixed="right"
      label="操作"
      width="300">
      <template slot-scope="scope">
        <el-button @click="deleteClick(scope.row)" type="warning" size="mini" round>删除</el-button>
      </template>
    </el-table-column>
  </el-table>

</template>

<script>
  export default {
    data() {
      return {
        tableData: []
      }
    },
    mounted(){
        this.loadApplicants();
        this.user_type = this.$store.state.user_type;
    },
    methods: {
      deleteClick(row){
        console.log(row.id);
        this.$axios.delete('api/message/' + row.id).then(resp => {
            this.$message({
                    message: resp.data.msg,
                    showClose: true,
                    type: 'success'
            });
            this.loadApplicants();
        })
      },
      loadApplicants(){
          this.$axios.get('api/message').then(resp => {
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