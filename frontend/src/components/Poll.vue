<template>
  <div class="poll">
    {{poll.question_text}}
  </div>
</template>

<script>
export default {
  name: "Poll",
  props: {
    poll: Object
  }
};
</script>

<style scoped>
</style>
