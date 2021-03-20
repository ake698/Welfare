<template>
  <el-upload
    name="files"
    class="img-upload"
    ref="upload"
    accept=".doc,.xls,.csv,.txt,.xlsn"
    action="http://localhost:8000/upload"
    :auto-upload="false"
    :on-preview="handlePreview"
    :headers="headers"
    :on-remove="handleRemove"
    :on-success="handleSuccess"
    multiple
    :limit="1"
    :on-exceed="handleExceed"
    :file-list="fileList"
    >
    <el-button slot="trigger" size="small" type="primary">选择文件</el-button>
    <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
    <div slot="tip" class="el-upload__tip">只能上传文档</div>
  </el-upload>
</template>

<script>
  export default {
    name: 'resourceUpload',
    data () {
      return {
        avatar: "/media/default.jpg",
        fileList: [],
        headers:{
          "Authorization":"aa"
        },
      }
    },
    mounted(){
      this.headers["Authorization"] = this.$store.state.token
    },
    methods: {
      handleRemove (file, fileList) {
      },
      handlePreview (file) {
      },
      handleExceed (files, fileList) {
        this.$message.warning(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`)
      },
      handleSuccess (response) {
        this.$message.success('上传成功')
        this.filepath = response.detail.file_path
        this.clear()
        this.addResourceRecord(this.filepath)
        window.location.reload();
      },
      submitUpload(){
        this.$emit('onUpload')
      },
      clear () {
        this.$refs.upload.clearFiles()
      },
      addResourceRecord(filepath){
        this.$axios.post('api/resource',{"name":filepath,"link":filepath}).then(resp => {
        })
      }
    }
  }
</script>
