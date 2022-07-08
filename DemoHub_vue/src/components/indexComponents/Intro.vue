<template>
  <div class="intro-wrap">
          <div class="short-line"></div>

    <p class="intro-tittle">{{ introData.tittle[this.$i18n.locale] }}</p>
    <div
      v-for="(text, index) in introData.text[this.$i18n.locale]"
      :key="index"
    >
      <p class="intro-text">
        {{ text }}
        <span v-show="introData.text.en.length == index + 1"
          ><a :href="introData.link.url">{{ introData.link.text.en }}</a></span
        >
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "myIntro",
  props: ["introData"],
  data() {
    return {};
  },
};
</script>

<style>
.short-line {
  border-bottom: 4px solid black;
  width: 5%;
  min-width: 40px;
  margin: 20px 0;
}
.inline {
  display: inline;
}

.intro-wrap {
  text-align: left;
  margin-bottom:20px;

}
.intro-tittle {
  font-size: 20px;
  font-family: Microsoft YaHei;
  font-weight: bold;
  color: #000000;
  margin: 15px 0;
}
.intro-text {
    font-size: 14px;
    font-family: Microsoft YaHei;
    font-weight: 400;
    color: #000000;
    line-height: 24px;
    text-indent: 2em;
    margin-bottom: 5px;
}
.intro-text a{
    color: #337ab7;
}
.intro-text a:hover{
        color: #23527c;
        text-decoration-line: underline;
}
</style>