<template>

<div>
  <div>
    <el-button v-if="user_type==2" @click="fileUploadDia()" type="primary"  round style="float:left;margin:20px">上传资源</el-button>
</div>
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
      prop="name"
      label="资源名"
      width="220"
      >
    </el-table-column>

    <el-table-column
      prop="create_time"
      label="上传时间"
      >
    </el-table-column>
    <el-table-column
      fixed="right"
      label="操作"
      width="400">
      <template slot-scope="scope">
        <el-button @click="downloadClick(scope.row)" type="warning" size="mini" round>下载</el-button>
        <el-button v-if="user_type==2" @click="deleteClick(scope.row)" size="mini" type="danger" round>删除</el-button>
      </template>
    </el-table-column>
  </el-table>
  <el-dialog title="公益资源上传" :visible.sync="avatarVisible">
    <el-form>
      <ResourceUpload @onUpload="uploadFile" ref="resourceUpload"></ResourceUpload>
    </el-form>
  </el-dialog>

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
        this.loadApplicants();
        this.user_type = this.$store.state.user_type;
        console.log(this.user_type)
    },
    methods: {
    //文件上传弹出
      fileUploadDia(){
        this.avatarVisible = true
      },
      uploadFile(){
        this.$refs.resourceUpload.$refs.upload.submit()
        this.avatarVisible = false
      },

      downloadClick(row){
        this.$axios.get('api/resource/' + row.id).then(resp => {
          window.location.href ="http://127.0.0.1:8000/media/"+ resp.data.detail
        })
      },
      deleteClick(row){
        this.$axios.delete('api/resource/' + row.id).then(resp => {
            this.$message({
                    message: resp.data.msg,
                    showClose: true,
                    type: 'success'
            });
            this.loadApplicants();
        })
      },
      loadApplicants(){
          this.$axios.get('api/resource').then(resp => {
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