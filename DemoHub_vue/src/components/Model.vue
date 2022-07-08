<template>
  <div>
    <h2>{{ modelType }}->{{ modelId }}</h2>
      {{allData}}
    <!-- {{ allData[modelType]["models"][modelId] }} -->
  </div>
</template>

<script>
import configData from "@/assets/config.json";

export default {
  name: "Model",
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
    if (this.allData == null || JSON.stringify(this.allData) == '{}') {
      this.$axios.get(this.baseUrl + "data").then((response) => {
          console.log(response)
        this.allData = response.data;
        this.$store.setMessageAction(this.allData);
      });
    }
  },
};
</script>

<style>
</style>