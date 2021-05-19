<template>
  <div class="Athlete animated">
      <div class="Athlete__rank">
        <h5> {{ rank+1 }} </h5>
      </div>
      <img class="avator" :src="avator[stringToNum(data.user_name) % 6]">
      <h2 class="Athlete__name">{{ data.user_name }}</h2>
      <h4 class="Athlete__reps"> {{ data.score }} </h4>
  </div>
</template>

<script>
  export default {
    name: 'Dashboard',
    props: ['data', 'show', 'rank'],
    methods: {
      stringToNum(word) {
        var sum = 0;
        word.toUpperCase().split('').forEach(function(alphabet) {
          sum += alphabet.charCodeAt(0) - 64;
        });
        return sum;
      }
    },
    data() {
      return {
        avator: [
          'https://image.flaticon.com/icons/png/128/4322/4322992.png',
          'https://image.flaticon.com/icons/png/128/4322/4322991.png',
          'https://image.flaticon.com/icons/png/128/3940/3940403.png',
          'https://image.flaticon.com/icons/png/128/3940/3940404.png',
          'https://image.flaticon.com/icons/png/128/3940/3940402.png',
          'https://image.flaticon.com/icons/png/128/3940/3940401.png'
        ]
      }
    }
  }
</script>
<style>
.avator {
  width: 65px;
  padding: 5px;
}
</style>
