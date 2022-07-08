<template>
  <div id="app">
        <Header></Header>
    <router-view class="centered lr-padding"/>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "@/components/structure/Header.vue";
import Footer from "@/components/structure/Footer.vue";
export default {
  name: 'App',
    components: { Header,Footer },
    mounted() {
    // 监听当浏览器窗口关闭或者刷新时
    // window.addEventListener('unload', this.saveSharedState)
    window.addEventListener('beforeunload', this.saveSharedState)
},
methods: {
    saveSharedState() {
        window.sessionStorage.setItem('sharedState', JSON.stringify(this.$store.state))
    }
}


}
</script>

<style>
*{
  margin: 0;
}
a{
  text-decoration-line: none;
  color: black;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.centered {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 5px;
}
.border{
  outline: 1px solid rgba(87, 87, 87, 0.26);
}


  .lr-padding1 {
    padding-left: 80px;
    padding-right: 80px;
  }
.lr-padding2 {
  padding-left: 40px;
  padding-right: 40px;
}
.lr-padding3 {
  padding-left: 30px;
  padding-right: 30px;
}

@media screen and (max-width: 1200px) {
  .top2-r {
    height: 60px;
  }
}
@media screen and (max-width: 992px) {
  .top2-l {
    height: 80px;
  }
    .lr-padding1 {
      padding-left: 15px;
      padding-right: 15px;
    }
  .lr-padding2 {
    padding-left: 10px;
    padding-right: 10px;
  }
  .lr-padding3 {
    padding-left: 2px;
    padding-right: 2px;
  }
  .top-wrap p {
    margin: 15px 3px 15px 3px;
  }
  .backcolor-blue {
    padding-top: 40px;
    padding-bottom: 10px;
  }
}
</style>
