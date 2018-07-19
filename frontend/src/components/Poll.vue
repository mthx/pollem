<template>
  <div class="poll">
    {{poll.question_text}}
    <div>
      <ul>
        <li v-for="choice in poll.choices" :key="choice.id"><button @click="vote(choice)">{{choice.choice_text}}</button></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Poll",
  props: {
    poll: Object
  },
  methods: {
    vote(choice) {
      alert(`Voting for ${choice.choice_text}`);
    }
  }
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
</style>
