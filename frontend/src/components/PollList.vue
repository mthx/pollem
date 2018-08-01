<template>
  <div class="PollList">
    <div class="loading" v-if="loading">
      Loading...
    </div>
    <div v-if="error" class="error">
      {{ error }}
    </div>
    <ul>
      <li v-for="poll in polls" :key="poll.id">
        <Poll :poll="poll" :onVote="onVote" />
      </li>
    </ul>
  </div>
</template>

<script>
import Poll from "./Poll.vue";
import { castVote, getPolls } from "../api";

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
     this.fetchData(true);
  },
  methods: {
    fetchData(initial) {
      this.loading = initial;
      getPolls()
        .then(j => {
          this.loading = false;
          this.polls = j;
        })
        .catch(e => {
          this.loading = false;
          this.error = e.toString();
        });
    },
    onVote(poll, choice) {
      castVote(poll.id, choice.id)
        .then(this.fetchData(false))
    }
  }
};
</script>

<style scoped>
.PollList {
  display: flex;
  justify-content: center;
}
.PollList ul {
  list-style-type: none;
  padding: 0;
}
</style>
