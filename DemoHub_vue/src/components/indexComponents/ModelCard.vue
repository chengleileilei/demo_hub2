<template>
  <div class="card">
    <!-- {{model}} -->
    <div class="image-wrap">
      <div class="card-image">
        <img
          :src="baseUrl + 'image?path=' + modelData.input_image_name"
          alt=""
        />
      </div>
      <div class="card-image">
        <img
          :src="baseUrl + 'image?path=' + modelData.output_image_name"
          alt=""
        />
      </div>
    </div>
    <p class="model-name">{{ modelData.name[this.$i18n.locale] }}</p>
    <div class="model-info">
      <p class="author">{{ modelData.author }}</p>
      <div class="info">
        <div
          class="heart-shaped"
          @click="like()"
          :style="{ '--heartColor': heartColor }"
        ></div>
        <p>{{ modelData.likes }}</p>
        <span class="el-icon-view"></span>
        <p>{{ modelData.pageviews }}</p>
      </div>
    </div>

    <!-- {{type}} -->

    <!-- {{modelData}} -->
  </div>
</template>

<script>
import configData from "@/assets/config.json";
export default {
  name: "ModelCard",
  props: ["modelData", "type", "model"],
  data() {
    return {
      baseUrl: configData.base_url,
      imageFileName: configData.image_file_name,
      // heartColor:{n:""}
      heartColor: "#747474",
    };
  },
  mounted() {
    if (
      localStorage.getItem(this.type+this.model + "_like") == null ||
      localStorage.getItem(this.type+this.model + "_like") == 0
    ) {
      this.heartColor = "#747474";
    } else {
      this.heartColor = "#ff6347";
    }
  },
  methods: {
    like() {
      if (
        localStorage.getItem(this.type+this.model + "_like") == null ||
        localStorage.getItem(this.type+this.model + "_like") == 0
      ) {
        this.heartColor = "#ff6347";
        localStorage[this.type+this.model + "_like"] = 1;
        this.$axios
          .get(this.baseUrl + "like", {
            params: {
              type: this.type,
              model: this.model,
            },
          })
          .then((response) => {
            this.modelData.likes = response.data;
          });
      } else {
        this.heartColor = "#747474";
        this.$axios
          .get(this.baseUrl + "dislike", {
            params: {
              type: this.type,
              model: this.model,
            },
          })
          .then((response) => {
            this.modelData.likes = response.data;
          });
        localStorage[this.type+this.model + "_like"] = 0;
      }
    },
  },
};
</script>

<style scoped>
.card {
  width: 500px;
  margin-bottom: 40px;
}
.image-wrap {
  display: flex;
  flex-direction: row;
}
.card-image {
  width: 50%;
  height: 185px;
  display: flex;
  overflow: hidden;
  justify-content: center;
}
.card-image > img {
  /* width: 100%; */
}
.model-name {
  text-align: left;
  font-size: 18px;
  font-family: Microsoft YaHei;
  font-weight: bold;
  color: #333333;
  margin: 10px 0;
}
.model-info {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  /* align-i; */
}
.info {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.info p {
  margin-left: 5px;
}
.info span {
  margin-left: 10px;
  font-size: 24px;
}

/* 心形 */
.heart-shaped {
  cursor: pointer;
  width: 10px;
  height: 10px;
  background-color: var(--heartColor);
  transform: rotate(-45deg);
}

.heart-shaped:before {
  content: "";
  position: absolute;
  top: -50%;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: var(--heartColor);
}

.heart-shaped:after {
  content: "";
  position: absolute;
  top: 0px;
  left: 50%;
  width: 100%;
  height: 100%;
  background-color: var(--heartColor);
  border-radius: 50%;
}
</style>