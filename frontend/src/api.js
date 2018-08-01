export const getPolls = () => fetch("/api/polls").then(r => r.json());

export const castVote = (pollId, choiceId) =>
  fetch(`/api/polls/${pollId}/vote/`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      choice: choiceId
    })
  }).then(r => r.json());
