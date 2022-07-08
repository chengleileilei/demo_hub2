<template>
  <div>
    <!-- {{baseUrl}} -->

    <div class="main-wrap centered lr-padding border">
      <div class="index-logo">
        <img src="@/assets/img/logo.png" alt="" />
        <p>DemoHub</p>
      </div>
      <div class="short-line"></div>
      <MyIntro :introData="allData.index.introduction"></MyIntro>
      <div v-for="(typeData, type) in allData.model_type" :key="type">

        <ModelType :typeData="typeData" :type="type"></ModelType>
      </div>
        <!-- <img src="http://127.0.0.1:5000/image?path=3.JPG" alt="" class="myimg"> -->
      <!-- {{ indexData }} -->
    </div>
  </div>
</template>

<script>

import MyIntro from "@/components/indexComponents/Intro.vue";
import ModelType from "@/components/indexComponents/ModelType.vue";
// import mockData from "@/assets/mockData/mockData.json";
import configData from "@/assets/config.json"

export default {
  name: "Index",
  components: { MyIntro, ModelType },
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      allData:"",
      baseUrl:configData.base_url
    };
  },
  created(){
    this.$axios.get(this.baseUrl+"data").then((response)=>{
      this.allData = response.data
      this.$store.setMessageAction(this.allData)
    })
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.index-logo {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.index-logo > img {
  height: 42px;
  width: 42px;
  margin: 12px;
}
.index-logo > p {
  font-size: 36px;
  font-family: Arial Black;
  font-weight: 400;
  color: #333333;
}

.short-line {
  border-bottom: 4px solid black;
  width: 5%;
  min-width: 50px;
  margin: 20px 5px;
}

.myimg{
  width: 50%;
}
</style>
