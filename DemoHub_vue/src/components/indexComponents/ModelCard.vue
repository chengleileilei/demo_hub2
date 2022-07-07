<template>
  <div>
    <el-col>
      <p>{{ modelData.name[this.$i18n.locale] }}</p>
      <img
        :src="baseUrl +  'image?path=' + modelData.input_image_name"
        alt=""
        class="card-image"
      />
      <img
        :src="baseUrl +  'image?path=' + modelData.output_image_name"
        alt=""
                class="card-image"

      />
      <p @click="like()"><span> likes:</span>{{modelData.likes}}</p>
      <p>views:{{modelData.pageviews}}</p>
      {{type}}

      <!-- {{modelData}} -->
    </el-col>
  </div>
</template>

<script>
import configData from "@/assets/config.json";
export default {
  name: "ModelCard",
  props: ["modelData","type"],
  data() {
    return {
      baseUrl: configData.base_url,
      imageFileName: configData.image_file_name,
    };
  },
//   methods:{
//       like(){
//           this.$axios.get()
//       }
//   }
};
</script>

<style>
.card-image{
    width: 30%;
}
</style>