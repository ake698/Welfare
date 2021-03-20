<template>
  <div style="margin-top: 40px">
    <!--<el-button @click="adddata()">添加文章</el-button>-->
    <div class="datas-area">
      
        <div v-for="data in datas" :key="data.id" style="padding-top:40px">
          <el-card style="text-align: left" v-loading="loading">
            <div>
          <div style="float:left;width:85%;height: 150px;overflow:hidden">
            <router-link class="data-link" :to="{path:'activity/'+data.id}">
              <span style="font-size: 20px"><strong>{{data.name}}</strong></span>
              <strong style="margin-left:10%">组织：{{data.sponsor_name}}</strong>
              <strong style="float:right"><span>发布时间：{{data.create_time}}</span></strong>
              </router-link>
            <br>
            <!-- <el-divider content-position="left">{{data.create_time}}</el-divider> -->
            <router-link class="data-link" :to="{path:'activity/'+data.id}">
              <p><strong>公益活动介绍：</strong>{{data.des}}</p>
              </router-link>
          </div>
          
          </div>
          
          <el-divider></el-divider>
          <div>
              <!-- <div v-html="data.des"></div> -->
              <el-button type="text" class="button" @click="signup(data.id)" style="float:right;margin-left:10px">报名</el-button>
              <el-button type="text" class="button" @click="gotolink(data.id)" style="float:right">查看详情</el-button>
          </div>
          </el-card>
        </div>
        <div style="margin-top:2%">
           <el-row style="text-align:center">
            <el-pagination
              @current-change="handleCurrentChange"
              :current-page="pageInfo.pageIndex"
              :page-size="pageInfo.pageSize"
              :total="pageInfo.total">
            </el-pagination>
            </el-row>
        </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'datas',
  data () {
    return {
      datas: [],
      loading:true,
      pageInfo:{
        pageSize:5,
        pageIndex:1,
        total:200
      }
    }
  },
  mounted () {
    this.loadDiary()
  },
  methods: {
    loadDiary () {
      this.$axios.get('api/activity',{
        params:{
          // "pagesize":this.pageInfo.pageSize,
          "page":this.pageInfo.pageIndex
        }
      }).then(resp => {
        var activities = resp.data.detail
        this.pageInfo = {
          pageSize : 5,
          pageIndex : resp.data.pageIndex,
          total : resp.data.total
        }
        activities.forEach(element => {
          element.create_time = element.create_time.replace("T"," ");
        });
        this.datas=activities;
        // console.log(resp.data.length)
        if(activities.length > 0){
          this.loading = false;
        }else{
          this.$message({
            message: "好可惜，暂时没有人公开日记！",
            showClose: true,
            type: 'warning'
          });
        }
      })
    },
    gotolink(e){
      this.$router.push({path:"/activity/"+e})
    },
    handleCurrentChange(currentPage){
      this.pageInfo.pageIndex = currentPage;
      this.loadDiary()
    },
    signup(id){
      this.$axios.post('api/applicant',{
          "activity" : id}
      ).then(resp => {
        if(resp.data.status == 200){
            this.$message({
                message: resp.data.msg,
                type: 'success'
              });
          }
        else{
          this.$message({
              message: resp.data.msg,
              type: 'error'
            });
        }
      })
    }

  }
}
</script>

<style scoped>
  .datas-area {
    width: 990px;
    height: 750px;
    margin-left: auto;
    margin-right: auto;
  }

  .data-link {
    text-decoration: none;
    color: #606266;
  }

  .data-link:hover {
    color: #409EFF;
  }
</style>

