<template>
  <div>
    <el-breadcrumb separator="/" class="bread-tag">
      <el-breadcrumb-item :to="{ path: '/' }">{{
        $t("message.home")
      }}</el-breadcrumb-item>
      <el-breadcrumb-item>{{
        allData["model_type"][modelType]["name"][this.$i18n.locale]
      }}</el-breadcrumb-item>
      <el-breadcrumb-item>{{
        allData["model_type"][modelType]["models"][modelId]["name"][
          this.$i18n.locale
        ]
      }}</el-breadcrumb-item>
    </el-breadcrumb>
          <MyIntro :introData="allData['model_type'][modelType]['models'][modelId]['introduction']"></MyIntro>

    <h2>{{ modelType }}->{{ modelId }}</h2>
    {{ allData }}
    <!-- {{ allData[modelType]["models"][modelId] }} -->
  </div>
</template>

<script>
import configData from "@/assets/config.json";
import MyIntro from "@/components/indexComponents/Intro.vue";


export default {
  name: "Model",
  components:{MyIntro},
  data() {
    return {
      baseUrl: configData.base_url,
      modelType: this.$route.params.model_type,
      modelId: this.$route.params.model_id,
      allData: this.$store.state.message,
    };
  },
  created() {
    // 处理在浏览器直接打开model页的情况，此时session不存在，无模型数据，需要重新请求
    if (this.allData == null || JSON.stringify(this.allData) == "{}") {
      this.$axios.get(this.baseUrl + "data").then((response) => {
        console.log(response);
        this.allData = response.data;
        this.$store.setMessageAction(this.allData);
      });
    }
  },
};
</script>

<style>
.bread-tag{
      font-size: 16px;
    font-family: Arial;
    font-weight: bold;
    margin-top: 20px;
}
</style>