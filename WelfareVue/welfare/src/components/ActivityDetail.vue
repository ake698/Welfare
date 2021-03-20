<template>
<div>
  
<el-card style="margin-top:4%">
     <!-- <el-container> -->

    <el-main v-loading="loading">
      <h2>{{form.name}}</h2>
      <h3>{{form.sponsor_name}}</h3>
      <p>{{form.create_time}}</p>
      <hr><br><br>
      <div v-html="form.des"></div>

    </el-main>

     <!-- </el-container> -->
</el-card>

<el-card>
     <!-- <el-container> -->
<div slot="header" class="clearfix">
    <h4 style="float:left">留言</h4>
  </div>
    <el-main v-loading="loading">
      
    <div id="messageboard">
        <el-form ref="form">
            <el-form-item>
                <el-input type="textarea"  v-model="content" :placeholder="placeholder" :rows="8"></el-input>
            </el-form-item>
                <el-button type="primary" @click="leaveMessage">留言</el-button>
                <el-button @click="reset">重置</el-button>
        </el-form>
      <div style="width:100%;margin-top:10px" v-for="message in messages" :key="message.id">
        <!--头像和信息-->
        <el-row>
          <el-col :span="4">
            <el-image
                style="margin:18px 0 0 30px;width:40px;height: 40px;float:left"
                :src="'http://localhost:8000/media/default.jpg'" round
                fit="cover">
              </el-image>
            <h4 style="margin:25px 0 0 20px;float:left">{{message.user_name}}:</h4>
          </el-col>
          <el-col :span="18">
            <p style="float:left;margin:25px 0" v-html="message.content"></p>
          </el-col>
          <el-col :span="2">
            <el-button type="primary" icon="el-icon-edit" circle title="回复" @click="atSomeOne(message.content)"></el-button>
          </el-col>
        </el-row>
    </div>
    </div>

    </el-main>

     <!-- </el-container> -->
</el-card>

<el-footer style="margin-top:20%"><a href="#" @click="back()">返回</a></el-footer>
 </div>
</template>

<script>
  export default {
    name: 'activity',
    data () {
      return {
        form:{
            
          },
        placeholder:"请输入要回复的内容！",
        id:0,
        loading:true,
        messages:[],
        content:"",
      }
    },
    mounted: function () {
      this.loadParams()
      this.loading = false
      this.loadMessages()
    },
    methods: {
      loadMessages(){
        this.$axios.get('api/message?activity_id='+this.id,).then(resp =>{
          this.messages = resp.data.detail
          console.log(this.messages)
        })
      },
      atSomeOne(e){
        this.content = " < " + e + "> 回复：  " 
      },
      reset(){
        this.content = ""
      },
      leaveMessage(){
        this.$axios.post('api/message',{"activity": this.id,"content":this.content}).then(resp =>{
            this.$message({
                    message: resp.data.msg,
                    showClose: true,
                    type: 'success'
            });
            this.loadMessages();
        })
      },

      back(){
        history.go(-1)
      },
      loadParams(){
        this.id = this.$route.params.id
        console.log(this.id)
        var id = this.id
        if(id != undefined && id != ""){
          this.getDairy();
        }else{
          this.$router.push("/index")
        }

      },
      getDairy(){
        this.$axios.get('/api/activity/'+this.id).then(resp => {
          if(resp.status == 200){
            this.form = resp.data.detail
             this.form.create_time = resp.data.detail.create_time.replace("T"," ")
          }
        }).catch(err => {
            this.$message({
                message: "没有权限查看！！！",
                type: 'error'
              });
            this.$router.push("/index")
        })
      },
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

  .author {
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

