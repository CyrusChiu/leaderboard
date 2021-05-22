<template>
  <div id="app">
    <nav>
      <img src="@/assets/images/logoo.png">
    </nav>
    <div style="padding: 30px; position: relative;">
      <div id="background-extension"></div>
      <div class="CompetitorList">
        <div class="Header">
          <h1 class="Header__title"># Ranking</h1>
          <img class="Header__image" src="@/assets/images/trophy.svg">
          <h4 :class="{label: true, connect: isActive, close: !isActive}">{{ label_status }}</h4>
        </div>
        <transition-group
          appear
          enter-active-class="animated flipInX"
          leave-active-class="animated fadeOutLeft"
          :key="show"
        >
        <DashBoard v-for="(info, index) in data" :key="index" :data="info" :rank="index"/>
        </transition-group>
      </div>
    </div>
  </div>
</template>

<script>
import DashBoard from './components/DashBoard.vue'

export default {
  name: 'App',
  data() {
    return {
      show: true,
      data: [],
      label_status: "",
      isActive: false
    }
  },
  components: {
    DashBoard
  },
  mounted: function() {
    this.initWebSocket();
  },
  methods: {
    initWebSocket() { //初始化weosocket
      var _this = this;

      const wsuri = "ws://127.0.0.1:5000";
      let ws = new WebSocket(wsuri);

      ws.onopen = function() {
        console.log("Open");
        _this.label_status = "Connected";
        _this.isActive = true;
      };

      ws.onerror = function() {
        console.error('Socket encountered error, Closing socket');
        ws.close();
        _this.label_status = "Closed";
        _this.isActive = false;
      };

      ws.onclose = function() {
        _this.label_status = "Connection Closed, Reconnect will be attempted in 1 second...";
        _this.isActive = false;
        setTimeout(_this.initWebSocket(), 1000);
      };

      ws.onmessage = this.updateData;
    },
    updateData(e) {
      this.show = !this.show;

      const redata = Object.values(JSON.parse(e.data));
      this.data = redata.sort(function (a, b) {
         return a.score < b.score ? 1 : -1;
      });
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.label {
  text-align: end;
  margin: 0;
  padding: 5px;
}

.connect {
  color: green;
}

.close {
  color: red;
  animation: 1.5s blink alternate;
  animation-iteration-count: infinite;
}

@keyframes blink {
  to {
    color: transparent;
  }
}
</style>
