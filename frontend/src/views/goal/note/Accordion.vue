<template>
  <div>
    <div class="accordion">
      <div class="header" v-on:click="toggle">
        <div class="header-contents-wrapper">
          <div class="source"><slot name="source"></slot></div>
          <div class="header-title"><slot name="header"></slot></div>
        </div>
      </div>

      <transition
        name="accordion"
        v-on:before-enter="beforeEnter"
        v-on:enter="enter"
        v-on:before-leave="beforeLeave"
        v-on:leave="leave"
      >

        <div class="body" v-show="show">
               <div class="body-inner">
            <slot name="body"></slot>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  // props: ["theme"],

  data() {
    return {
      show: false
    };
  },

  methods: {
    toggle: function () {
      this.show = !this.show;
    },
    beforeEnter: function (el) {
      el.style.height = "0";
    },
    enter: function (el) {
      el.style.height = el.scrollHeight + "px";
    },
    beforeLeave: function (el) {
      el.style.height = el.scrollHeight + "px";
    },
    leave: function (el) {
      el.style.height = "0";
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Lato");

.accordion {
  max-width: auto;
  /* font-family: Lato; */
  margin-bottom: 30px;
  background-color:#354779;
  border-radius: 27.5px;
  position: relative;
  box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
  height: 100%;

}

.header-contents-wrapper {
  padding: 20px 20px;
}

.source {
  font-size: 14px;
}

.accordion .header {
  height: auto;
  /* line-height: 20px; */
  font-size: 20px;
  position: relative;
  color: rgb(241, 241, 241);
  cursor: pointer;
  z-index: 10;

}

.accordion .body {
  /* The content is displayed as it expands. */
  overflow: hidden;
  background-color: #f0f0f0;
  transition: 150ms ease-out;
  border-radius: 27.5px;

  /*  It looks like on the board/ */
  z-index: 20;
  position: relative;
  box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
  right: 3px;
  top: -3px;
}

.accordion .body-inner {
  padding: 10px 60px;
  position: relative;
  z-index: 25px;

}

.accordion .header-icon.rotate {
  transform: rotate(180deg);
  transition-duration: 0.3s;
}

@media only screen and (max-width: 600px) {

.col-7 {
    flex: 0 0 100%;
    max-width: 100%;
}
.col-8 {
    flex: 0 0 100%;
    max-width: 100%;
}
.category-title{
  padding-left: 0px;
}
.accordion .header{
  font-size: 18px;
}
.accordion .body-inner {
  padding: 20px;
  position: relative;
  z-index: 25px;
}
}
@media only screen and (max-width: 600px) {

.col-7 {
    flex: 0 0 100%;
    max-width: 100%;
}
.col-6 {
    flex: 0 0 100%;
    max-width: 100%;
}
.category-title{
  padding-left: 0px;
}
}



</style>
