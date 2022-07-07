<template>
  <div class="model-type-wrap">
      <div class="type-tittle-wrap">
          <p class="type-tittle">{{typeData.name[this.$i18n.locale]}}</p>
          <p class="type-more">{{typeData.more.text[this.$i18n.locale]+">>"}}</p>
      </div>
          <!-- {{typeData}} -->
      <div class="type-main">
          <div v-for="(model,index) in typeData.models" :key="index">
              <!-- {{model}} -->

          <ModelCard :modelData="model" :type="type"></ModelCard>
          </div>
      </div>

  </div>

</template>

<script>
import ModelCard from "@/components/indexComponents/ModelCard.vue";
export default {
    name:"ModelType",
    props:["typeData","type"],
    components:{ModelCard},
    data(){
        return{
            modelType:"",
            modelMore:"#"

        }
    }

}
</script>

<style>
.model-type-wrap{
    margin: 20px 0;
}
.type-tittle-wrap{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    margin:0 5px;
}
.type-tittle{
    font-size: 18px;
    font-family: Microsoft YaHei;
    font-weight: bold;
    color: #000000;
    padding: 10px;
    float: left;
    background: linear-gradient(90deg, #D4D4D4 0%, rgba(240, 243, 245, 0.01) 100%);
}
.type-more{
    cursor: pointer;
    background: #333333;
    float: right;
    font-size: 16px;
    font-family: Microsoft YaHei;
    font-weight: bold;
    color: #FFFFFF;
    padding: 10px;
}
.type-main{
    display: flex;
}

</style>