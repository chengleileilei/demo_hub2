<template>
  <header>
    <div class="nav-background">
      <div class="centered lr-padding3 nav">
        <div class="logo-wrap">
          <img src="@/assets/img/nav-logo.png" alt="" />
          <div class="logo-tittle-wrap">
            <p class="logo-tittle-up">DemoHub</p>
            <p class="logo-tittle-down">
              Try state-of-the-art computer visons models
            </p>
          </div>
        </div>
        <p>{{ $t("message.i1") }}</p>

        <div>
          <a href="javascript:void(0);" @click="changeLang()">{{ nextLang }}</a>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "myHeader",
  data() {
    return {
      nextLang: "",
    };
  },
  created() {
    if (this.$i18n.locale == "cn") {
      this.nextLang = "English";
    } else if (this.$i18n.locale == "en") {
      this.nextLang = "中文";
    }
  },
  methods: {
    changeLang() {
      console.log(this.$i18n.locale);
      if (this.$i18n.locale == "cn") {
        this.$i18n.locale = "en";
        this.nextLang = "中文";
      } else if (this.$i18n.locale == "en") {
        this.$i18n.locale = "cn";
        this.nextLang = "English";
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.nav-background {
  background-color: #f8f8f8;
  border: 1px solid #e7e7e7;
}
.nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  /* border: 1px solid black; */
  padding: 10px 0;
}

.logo-wrap {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.logo-wrap > img {
  width: 45px;
  margin: 0px 13px;
}
.logo-tittle-wrap {
  display: flex;
  flex-direction: column;
  /* justify-content: left; */
  align-items: flex-start;
}
.logo-tittle-up {
  font-size: 24px;
  font-family: Arial Black;
}
.logo-tittle-down {
  font-size: 12px;
  font-family: Arial;
  padding-bottom: 5px;
}
</style>
