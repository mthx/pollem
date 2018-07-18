<template>
  <div id="app">
    <PollList />
  </div>
</template>

<script>
import PollList from "./components/PollList.vue";

export default {
  name: "app",
  components: {
    PollList
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-top: 60px;
}
</style>
