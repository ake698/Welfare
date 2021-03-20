<template>
<div>
     <el-container>
<el-page-header style="margin-top:3%" @back="goBack" content="文章管理">
</el-page-header>
    <el-main>

<el-form ref="acForm" :model="form"  label-width="80px">
  <el-form-item label="文章标题" prop="title" :rules="[{required:true,message:'不能为空！'}]">
    <el-input v-model="form.title"></el-input>
  </el-form-item>

 <el-form-item label="活动组织" prop="org" :rules="[{required:true,message:'不能为空！'}]">
    <el-select style="width:100%" v-model="form.org" placeholder="请选择活动区域" >
      <el-option v-for="o in orgs" :key="o.id" :label="o.name" :value=o.id>{{o.name}}</el-option>
    </el-select>
  </el-form-item>

  <Editor v-model="form.content" :isClear="isClear" @change="change"></Editor>


  <el-form-item>
    <el-button type="primary" round @click="saveAc" >{{btn}}</el-button>
    <el-button round @click="resetForm">重置</el-button>
  </el-form-item>

</el-form>
    </el-main>
<el-footer>Code By ShiQing</el-footer>
     </el-container>
 </div>
</template>

<script>
  import Editor from './common/Editor'
  export default {
    name: 'Index',
    components:{Editor},
    data () {
      return {
        form:{
          title:"",
          username:"",
          content:"",
          org:"",
          },
        btn:"立即创建",
        id:0,
        isClear: false,
        detail:"",
        orgs:[]
      }
    },
    mounted: function () {
      this.loadParams();
      this.loadOrg();
    },
    methods: {
      goBack(){
        history.go(-1);
      },
      change(val){
          console.log(val)
          this.form.content = val
      },
      loadOrg(){
        this.$axios.get('/api/org').then(resp => {
          this.orgs = resp.data.detail
        })
      },
      loadParams(){
        this.id = this.$route.query.uid
        var id = this.id
        if(id != undefined && id != ""){
          this.getActivity();
        }
      },
      getActivity(){
        this.$axios.get('/api/activity/'+this.id).then(resp => {
          if(resp.status == 200){
            var fd = this.form
            fd.title = resp.data.title
            fd.username = resp.data.username
            fd.content = resp.data.content
            fd.isPublic = resp.data.isPublic
            this.btn = "立即更新"
          }
        })
      },
      resetForm(formName) {
        this.$refs['acForm'].resetFields();
        this.form.content = ""
      },

      saveAc(){
        console.log(this.form.org)
        this.$refs['acForm'].validate(
          (valid) => {
            if(valid){
              if(this.form.content.length < 6){
                this.$message({
                    message: "请填写日记内容！",
                    type: 'error'
                  });
                return;
              }
              var id = this.id
              if(id != undefined && id != ""){
                this.modifyAc()
              }else{
                this.createAc()
              }
            }else{
              return false;
            }
          }
        )

      },
      createAc(){
        this.$axios.post('/api/activity',
        {
          "name":this.form.title,
          "des":this.form.content,
          "sponsor":this.form.org
        }
        ).then(resp=>{
          console.log(resp)
          if(resp && resp.data.status === 200){
            this.$message({
              message: "添加成功！！！",
              type: 'success'
            });
            this.$router.push("/index")
          }
        })
      },
      modifyAc(){
        this.$axios.put('/api/diary/'+this.id,
        {
          "title":this.form.title,
          "content":this.form.content,
          "ispublic":this.form.isPublic
        }
        ).then(resp=>{
          console.log(resp)
          if(resp && resp.status === 201){
            this.$message({
              message: "修改成功！！！",
              type: 'success'
            });
            this.$router.push("/index")
          }
        })
      }

    }
  }
</script>
<style scoped>

  .cover {
    width: 115px;
    height: 172px;
    margin-bottom: 7px;
    overflow: hidden;
    cursor: pointer;
  }

  img {
    width: 115px;
    height: 172px;
    /*margin: 0 auto;*/
  }

  .title {
    font-size: 14px;
    text-align: left;
  }

  .username {
    color: #333;
    width: 102px;
    font-size: 13px;
    margin-bottom: 6px;
    text-align: left;
  }

  .abstract {
    display: block;
    line-height: 17px;
  }

  .el-icon-delete {
    cursor: pointer;
    float: right;
  }

  .switch {
    display: flex;
    position: absolute;
    left: 780px;
    top: 25px;
  }

  a {
    text-decoration: none;
  }

  a:link, a:visited, a:focus {
    color: #3377aa;
  }

</style>

