<template>
  <div>
    <el-row>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="footer-wrap">
        <el-row class="centered footer">
          <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="footer-l">
            <p class="with-logo-left">
              <img
                class="footer-logo"
                src="@/assets/icon/arcoDesign-location.svg"
                alt=""
              />
              {{ $t("message.address")
              }}{{ allData.message.footer.address[$i18n.locale] }}
            </p>
            <p class="with-logo-left">
              <img
                class="footer-logo"
                src="@/assets/icon/fas-fa-phone.svg"
                alt=""
              />
              {{ $t("message.phone") }}{{ allData.message.footer.phone }}
            </p>
            <p class="with-logo-left">
              <img
                class="footer-logo"
                src="@/assets/icon/arcoDesign-email.svg"
                alt=""
              />{{ $t("message.email") }}{{ allData.message.footer.email }}
            </p>
            <br />
            <a :href="allData.message.footer.related_links.url"
              ><p class="small-p">
                {{
                  $t("message.related_links")
                }}{{ allData.message.footer.related_links.text[$i18n.locale] }}
              </p></a
            >
          </el-col>

          <!-- <el-col :xs="24" :sm="24" :md="8" :lg="10" :xl="10" class="footer-r">
            <img src="@/assets/wechat.jpg" alt="" />

            <p>
              <a href="https://github.com/chengleileilei/graduation"
                >项目仓库：<br />https://github.com/chengleileilei/graduation</a
              >
            </p>
          </el-col> -->

          <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="footer-b">
            <p class="with-logo-center">
              <img
                class="footer-logo"
                src="@/assets/icon/fas-fa-copyright.svg"
                alt=""
              />
              DemoHub
            </p>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      allData: this.$store.state,
    };
  },
};
</script>

<style>
.footer-wrap {
  background-color: #333333;
}
.footer-wrap p {
  color: rgba(255, 255, 255, 1);
  font-size: 18px;
}
.footer {
  padding: 0px 10px;
}

.footer-l {
  margin-top: 40px;

  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
}
.footer-l .small-p {
  font-size: 18px;
}

.footer-l .with-logo-left {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.footer-r {
  margin-top: 40px;

  display: flex;
  align-items: center;
}
.footer-r img {
  width: 150px;
  margin-right: 35px;
}
.footer-r p {
  text-align: left;
}
.footer-r a {
  color: white;
}

.footer-b {
  margin-top: 30px;
  padding-bottom: 10px;
}
.footer-b p {
  color: rgba(189, 192, 193, 1);
  font-size: 16px;
  font-family: SourceHanSansSC-regular;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.footer-logo {
  margin-right: 10px;
  width: 20px;
  height: 20px;
}
</style>