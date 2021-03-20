import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
      username:window.localStorage.getItem("username"),
      token:window.localStorage.getItem("token"),
      avatar:window.localStorage.getItem("avatar"),
      user_type:window.localStorage.getItem("user_type"),
    },
    mutations: {
      login (state, form) {
        state.username = form.username
        state.token = form.token
        var avatarPath = "http://localhost:8000/media/" + form.avatar
        state.avatar = avatarPath
        window.localStorage.setItem('username', form.username)
        window.localStorage.setItem('token', form.token)
        window.localStorage.setItem('avatar', avatarPath)
        window.localStorage.setItem('user_type', form.user_type)
      },
      logout(state){
        state.username = ""
        state.token = ""
        state.avatar = ""
        window.localStorage.removeItem("username")
        window.localStorage.removeItem("token")
        window.localStorage.removeItem("avatar")
        window.localStorage.removeItem("user_type")
      },
      avatarChange(state,avatar){
        var avatarPath = "http://localhost:8000/media/" + avatar
        state.avatar = avatarPath
        window.localStorage.setItem('avatar', avatarPath)
      }
    }
  })

