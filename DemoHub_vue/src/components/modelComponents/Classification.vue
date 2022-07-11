<template>
  <div>
    <h1>classification</h1>
    <h2>{{ modelData.modelType }}->{{ modelData.modelId }}</h2>
    <!-- <h1>{{ modelData }}</h1> -->

    <el-row class="show-wrap">
      <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
        <p>{{ $t("message.input_image") }}</p>
        <img :src="imageUrl" alt="" class="source-image" />
        <div class="input-wrap" v-show="imageUrl == ''" @click="moveClick()">
          <p v-show="isLoading == false">{{ $t("message.drop_image") }}</p>
          <p v-show="isLoading == false">{{ $t("message.or") }}</p>
          <p v-show="isLoading == false">{{ $t("message.click_upload") }}</p>
          <p v-show="isLoading">uploading......</p>
          <input
            ref="filebutton"
            type="file"
            v-show="0"
            @change="fileChange()"
          />
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
        <p>{{ $t("message.result") }}</p>
        <div>
          <p v-show="isLoading2">uploading......</p>
          {{ modelResult }}
        </div>
        <!-- <img :src="imageUrl" alt="" /> -->
      </el-col>
    </el-row>
    <el-row
      :gutter="10"
      v-if="
        JSON.stringify(modelData.args) != '{}' ||
        getType(modelData.args) != 'undefined'
      "
    >
      <el-col
        :xs="24"
        :sm="12"
        :md="12"
        :lg="6"
        :xl="6"
        v-for="(arg_data, arg_name) in modelData.args"
        :key="arg_name"
      >
        <div class="arg-wrap">
          <p>{{ arg_name }}:</p>
          <el-select v-model="arg_data.default" placeholder="请选择">
            <el-option
              v-for="item in arg_data.values"
              :key="item"
              :label="item"
              :value="item"
            >
            </el-option>
          </el-select>
        </div>
      </el-col>
    </el-row>

    <el-row :gutter="10">
      <el-col :xs="12" :sm="6" :md="6" :lg="6" :xl="6">
        <a
          href="javascript:void(0);"
          class="clear upload-btn"
          @click="imageClear()"
          >{{ $t("message.clear") }}</a
        >
      </el-col>
      <el-col :xs="12" :sm="6" :md="6" :lg="6" :xl="6">
        <a
          href="javascript:void(0);"
          class="submit upload-btn"
          @click="submit()"
          >{{ $t("message.submit") }}</a
        >
      </el-col>
    </el-row>
  </div>
</template>

<script>
import configData from "@/assets/config.json";

export default {
  name: "classification",
  props: ["modelData"],
  data() {
    return {
      baseUrl: configData.base_url,
      imageUrl: "",
      isLoading: false,
      isLoading2: false,
      modelResult: "",
    };
  },
  methods: {
    getType(data) {
      return typeof data;
    },
    //   点击事件转移
    moveClick() {
      // https://blog.csdn.net/youdu0213/article/details/122825179
      this.$nextTick(() => {
        this.$refs.filebutton.dispatchEvent(new MouseEvent("click"));
        // console.log(this.$refs.filebutton.files)
      });
    },
    // imageLoad() {
    //   this.isLoading = false;
    // },
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
        this.isLoading = true;
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
        this.$message({
          message: "图片校验失败！",
          type: "warning",
        });
        // console.log("图片校验失败！");
      }
    },
    imageClear() {
      (this.imageUrl = ""), (this.$refs.filebutton.value = "");
      this.isLoading = false;
      this.isLoading2 = false;
      this.modelResult = "";
    },
    submit() {
      if (this.imageUrl == "") {
        this.$message({
          message: "请先上传图片！",
          type: "warning",
        });
      } else {
        this.isLoading2 = true;
        this.modelResult = "";
        let post_data = {
          image_url: this.imageUrl,
          conda_env: this.modelData.condaEnv,
          args: {},
        };
        for (var arg_name in this.modelData.args) {
          post_data["args"][arg_name] =
            this.modelData.args[arg_name]["default"];
        }
        console.log(post_data);
        this.$axios.post(this.baseUrl + "submit", post_data).then((res) => {
          this.modelResult = res.data;
          console.log("res=>", res);
          this.isLoading2 = false;
        });
      }
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
.arg-wrap {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.arg-wrap > * {
  margin: 5px 15px;
}
</style>