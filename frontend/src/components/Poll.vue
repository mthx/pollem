<template>
  <div class="Poll">
    <div class="Poll-question">
      {{poll.question_text}}
    </div>
    <div>
      <ul>
        <li v-for="choice in poll.choices" :key="choice.id">
          <div class="Poll-choice">
            <span class="Poll-text">{{choice.choice_text}}</span>
            <span class="Poll-votes">{{choice.votes}}</span>
            <button class="Poll-action" @click="onVote(poll, choice)">➕</button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Poll",
  props: {
    poll: Object,
    onVote: Function
  }
};
</script>

<style scoped>
.Poll ul {
  list-style-type: none;
  padding: 0;
}
.Poll {
  border-left: 5px solid #dee2f2;
  padding-left: 0.5em;
  margin-bottom: 2em;
}
.Poll-choice {
  display: flex;
  width: 300px;
  justify-content: space-between;
  align-items: center;
}
.Poll-text {
  width: 200px;
}
.Poll-question {
  margin-bottom: 1em;
}
.Poll button {
  border: none;
  outline: inherit;
  font-size: 20px;
}
</style>
