<template>
  <div class="poll-list">
    <div class="loading" v-if="loading">
      Loading...
    </div>
    <div v-if="error" class="error">
      {{ error }}
    </div>
    <ul>
      <li v-for="poll in polls" :key="poll.id">
        <Poll :poll="poll" />
      </li>
    </ul>
  </div>
</template>

<script>
import Poll from "./Poll.vue";

export default {
  name: "PollList",
  data() {
    return {
      loading: false,
      error: undefined,
      polls: []
    };
  },
  components: {
    Poll
  },
  created() {
   this.fetchData(); 
  },
  methods: {
    fetchData() {
      this.loading = true;
      fetch("/api/questions")
        .then(r => r.json())
        .then(j => {
          this.loading = false;
          this.polls = j;
        })
        .catch(e => {
          this.loading = false;
          this.error = e.toString();
        })
    }
  }
};
</script>

<style scoped>
.poll-list {
  display: flex;
  justify-content: center;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
}
</style>
