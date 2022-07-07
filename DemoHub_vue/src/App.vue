<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
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
