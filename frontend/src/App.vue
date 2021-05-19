<template>
  <div id="app">
    <nav>
      <img src="@/assets/images/logoo.png">
    </nav>
        <div style="position: relative;">
      <div id="background-extension"></div>
      <div class="CompetitorList">
        <div class="Header">
          <h1 class="Header__title"># Ranking</h1>
          <img class="Header__image" src="@/assets/images/trophy.svg">
        </div>
        <transition-group
          appear
          enter-active-class="animated flipInX"
          leave-active-class="animated fadeOutLeft"
          :key="show"
        >
        <DashBoard v-for="(data, index) in testdata" :key="index" :data="data" :rank="index"/>
        </transition-group>
      </div>
    </div>
        <button @click="updateData">
    Toggle render
    </button>

  </div>
</template>

<script>
import DashBoard from './components/DashBoard.vue'

export default {
  name: 'App',
  components: {
    DashBoard
  },
  mounted() {
    this.initWebSocket();
    //setInterval(this.updateData, 3000);
  },
  methods: {
    initWebSocket() { //初始化weosocket
      const wsuri = "ws://127.0.0.1:2700";
      this.websocket = new WebSocket(wsuri);
      this.websocket.onmessage = this.websocketonmessage;
    },
    websocketonmessage(e) {
      //const redata = JSON.parse(e.data);
      console.log(e.data);
    },
    updateData() {
      this.show = !this.show;
      this.testdata = [
        {
          'user_name': 'daniel',
          'score': 10
        },
        {
          'user_name': 'kent',
          'score': 50
        },
        {
          'user_name': 'raix',
          'score': 30
        }
      ].sort(function (a, b) {
         return a.score < b.score ? 1 : -1;
      });
    },
  },
  data() {
    return {
      websocket: null,
      show: true,
      testdata: [],
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
