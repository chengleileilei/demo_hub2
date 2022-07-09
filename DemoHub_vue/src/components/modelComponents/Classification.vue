<template>
  <div>
    <h1>classification</h1>
    <el-row class="show-wrap">
      <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
        <p>Input Image:</p>
        <div class="input-wrap" @click="moveClick()">
          <p class="before-p">Drop Image Here</p>
          <p class="before-p">- OR -</p>
          <p class="before-p">Click to Upload</p>
          <p class="loading-p hidden">uploading......</p>
          <input
            ref="filebutton"
            type="file"
            v-show="0"
            @change="fileChange()"
          />
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
        <p>Result:</p>
        <img :src="imageUrl" alt="">
      </el-col>
    </el-row>

    <el-row> </el-row>
  </div>
</template>

<script>
import configData from "@/assets/config.json";

export default {
  name: "classification",
  props: [],
  data() {
    return {
      baseUrl: configData.base_url,
      imageUrl:""
    };
  },
  methods: {
    //   点击事件转移
    moveClick() {
      // https://blog.csdn.net/youdu0213/article/details/122825179
      this.$nextTick(() => {
        this.$refs.filebutton.dispatchEvent(new MouseEvent("click"));
        // console.log(this.$refs.filebutton.files)
        //   this.$refs.filebutton.click();
      });
      //   return
    },
    fileChange() {
      this.$nextTick(() => {
        console.log(this.$refs.filebutton.files);
        const formData = new FormData();
        formData.append("image", this.$refs.filebutton.files[0]);
        this.$axios
          .post(this.baseUrl+"upload", formData, {
            "Content-type": "multipart/form-data",
          })
          .then(
            (res) => {
              console.log(res.data)
              this.imageUrl = this.baseUrl+'sourceimage?name='+res.data
            },
            (err) => {
                alert("上传图片失败！")
              // 出现错误时的处理
            }
          );
      });
    },
  },
};
</script>

<style>
.show-wrap {
  padding: 10px;
  background-color: #f4f4f4;
}
.input-wrap {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 280px;
  border: 2px dashed #202020;
  cursor: pointer;
}
</style>