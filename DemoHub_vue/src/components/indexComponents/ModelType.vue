<template>
  <div class="model-type-wrap">
    <div class="type-tittle-wrap">
      <p class="type-tittle">{{ typeData.name[this.$i18n.locale] }}</p>
      <p class="type-more">
        {{ typeData.more.text[this.$i18n.locale] + ">>" }}
      </p>
    </div>
    <!-- {{typeData}} -->
    <el-row :gutter="10" class="type-main">
      <el-col
        :xs="24"
        :sm="12"
        :md="8"
        :lg="8"
        :xl="8"
        v-for="(model, index) in typeData.models"
        :key="index"
      >
        <ModelCard :modelData="model" :type="type" :model="index"></ModelCard>
      </el-col>
    </el-row>
    <!-- <div class="type-main">
          <div v-for="(model,index) in typeData.models" :key="index">

          <ModelCard :modelData="model" :type="type" :model="index"></ModelCard>
          </div>
      </div> -->
  </div>
</template>

<script>
import ModelCard from "@/components/indexComponents/ModelCard.vue";
export default {
  name: "ModelType",
  props: ["typeData", "type"],
  components: { ModelCard },
  data() {
    return {
      modelType: "",
      modelMore: "#",
    };
  },
};
</script>

<style>
.model-type-wrap {

}
.type-tittle-wrap {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin: 10px 0;
}
.type-tittle {
  font-size: 18px;
  font-family: Microsoft YaHei;
  font-weight: bold;
  color: #000000;
  padding: 10px;
  float: left;
  background: linear-gradient(
    90deg,
    #d4d4d4 0%,
    rgba(240, 243, 245, 0.01) 100%
  );
}
.type-more {
  cursor: pointer;
  background: #333333;
  float: right;
  font-size: 16px;
  font-family: Microsoft YaHei;
  font-weight: bold;
  color: #ffffff;
  padding: 10px;
}
.type-main {
  /* display: flex; */
  margin: 0 5px;
}
</style>