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

    <MyIntro
      :introData="
        allData['model_type'][modelType]['models'][modelId]['introduction']
      "
    ></MyIntro>

    <component :is="currentView"></component>

    <h2>{{ modelType }}->{{ modelId }}</h2>
    {{ allData }}
  </div>
</template>

<script>
import configData from "@/assets/config.json";
import MyIntro from "@/components/indexComponents/Intro.vue";
// import Classification from "@/components/modelComponents/Classification.vue";
export default {
  name: "Model",
  components: {
    MyIntro,
    classification: () =>
      import("@/components/modelComponents/Classification.vue"),
    image_process: () =>
      import("@/components/modelComponents/ImageProcess.vue"),
  },
  data() {
    return {
      currentView: this.$route.params.model_type,
      baseUrl: configData.base_url,
      modelType: this.$route.params.model_type,
      modelId: this.$route.params.model_id,
      allData: this.$store.state.message,
    };
  },
  created() {
    // 更新模型访问量
    this.$axios
      .get(this.baseUrl + "pageviews", {
        params: {
          type: this.modelType,
          model: this.modelId,
        },
      })
      .then((response) => {
        console.log("Current model pageviews: ", response.data);
      });
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
.bread-tag {
  font-size: 16px;
  font-family: Arial;
  font-weight: bold;
  margin-top: 20px;
}
</style>