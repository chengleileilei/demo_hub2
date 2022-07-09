<template>
  <div>
    <h1>imageprocess</h1>
    <el-row class="show-wrap">
      <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
        <p>Input Image:</p>
        <img :src="imageUrl" alt="" class="source-image" />
        <div class="input-wrap" v-show="imageUrl == ''" @click="moveClick()">
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
        <!-- <img :src="imageUrl" alt="" /> -->
      </el-col>
    </el-row>

    <el-row :gutter="10">
      <el-col :xs="12" :sm="6" :md="6" :lg="6" :xl="6">
        <a
          href="javascript:void(0);"
          class="clear upload-btn"
          @click="imageClear()"
          >CLEAR</a
        >
      </el-col>
      <el-col :xs="12" :sm="6" :md="6" :lg="6" :xl="6">
        <a href="javascript:void(0);" class="submit upload-btn">SUBMIT</a>
      </el-col>
    </el-row>
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
      imageUrl: "",
    };
  },
  methods: {
    //   点击事件转移
    moveClick() {
      // https://blog.csdn.net/youdu0213/article/details/122825179
      this.$nextTick(() => {
        this.$refs.filebutton.dispatchEvent(new MouseEvent("click"));
        // console.log(this.$refs.filebutton.files)
      });
    },
    imageVerification(file) {
      /*判断文件后缀类型*/
      var strs = new Array(); //定义一数组
      var pic1 = file.value; //获取input框的值，文件路径
      strs = pic1.split("."); //分成数组存储
      var suffix = strs[strs.length - 1]; //获取文件后缀

      if (
        suffix != "jpg" &&
        suffix != "gif" &&
        suffix != "jpeg" &&
        suffix != "png"
      ) {
        alert("您选择的不是图片，请上传一个图片"); //不是图片，做处理
        return false;
      }
      var fileSize = 0; //文件大小默认为0
      /*获取文件大小，以Kb为单位*/
      fileSize = file.files[0].size / 1024;
      if (fileSize > 10000) {
        alert("您选择的图片太大，请选择小于10M的图片");
        return flase;
      } else {
        return true;
      }
    },
    fileChange() {
      if (this.imageVerification(this.$refs.filebutton)) {
        this.$nextTick(() => {
        console.log(this.$refs.filebutton.files);
        const formData = new FormData();
        formData.append("image", this.$refs.filebutton.files[0]);
        this.$axios
          .post(this.baseUrl + "upload", formData, {
            "Content-type": "multipart/form-data",
          })
          .then(
            (res) => {
              console.log(res.data);
              this.imageUrl = this.baseUrl + "sourceimage?name=" + res.data;
            },
            (err) => {
              alert("上传图片失败！");
              // 出现错误时的处理
            }
          );
      });
      } else {
        console.log("图片校验失败！")
      }

      
    },
    imageClear() {
      (this.imageUrl = ""), (this.$refs.filebutton.value = "");
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
.source-image {
  width: 95%;
}
.upload-btn {
  text-align: center;
  display: inline-block;
  width: 100%;
  font-size: 16px;
  font-family: Microsoft YaHei;
  font-weight: 400;
  line-height: 33px;
  margin-top: 10px;
}
.upload-btn:hover {
  text-decoration-line: underline;
}
.clear {
  background: #333333;
  color: #ffffff;
}
.submit {
  border: 1px solid #cccccc;
  color: #333333;
}
</style>