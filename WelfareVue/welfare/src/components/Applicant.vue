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
     :width=140
      prop="user_name"
      label="申请人"
      >
    </el-table-column>
    <el-table-column
      prop="status_name"
      :width=140
      label="状态"
      :filters="[{ text: '申请中', value: '申请中' }, { text: '已同意', value: '已同意' }, { text: '已拒绝', value: '已拒绝' }]"
      filter-placement="bottom-end"
      :filter-method="filter_status"
      >
      <template slot-scope="scope">
        <el-tag
          :type="scope.row.status === 2 ? 'success':'primary' "
          disable-transitions>{{scope.row.status_name}}</el-tag>
      </template>
    </el-table-column>
    <el-table-column
      prop="activity_name"
      label="申请活动"
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
      width="400">
      <template slot-scope="scope">
        <el-button @click="deleteClick(scope.row)" type="warning" size="mini" round>删除</el-button>
        <el-button v-if="user_type==2" @click="approveClick(scope.row)" type="success" size="mini" round>通过</el-button>
        <el-button v-if="user_type==2" @click="rejectClick(scope.row)" size="mini" type="danger" round>拒绝</el-button>
      </template>
    </el-table-column>
  </el-table>

</template>

<script>
  export default {
    data() {
      return {
        tableData: [],
        user_type:1,
      }
    },
    mounted(){
        this.loadApplicants();
        this.user_type = this.$store.state.user_type;
    },
    methods: {
      deleteClick(row){
        console.log(row.id);
        this.$axios.delete('api/applicant/' + row.id).then(resp => {
            this.$message({
                    message: resp.data.msg,
                    showClose: true,
                    type: 'success'
            });
            this.loadApplicants();
        })
      },
      approveClick(row){
          this.putHttp(row.id, 2);
      },
      rejectClick(row){
          this.putHttp(row.id, 3);
      },
      putHttp(id, status){
        this.$axios.put('api/applicant/' + id,{"status": status}).then(resp =>{
            this.$message({
                    message: resp.data.msg,
                    showClose: true,
                    type: 'success'
            });
            this.loadApplicants();
        })
      },
      filter_status(value, row) {
        return row.status_name === value;
      },
      filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },
      loadApplicants(){
          this.$axios.get('api/applicant').then(resp => {
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