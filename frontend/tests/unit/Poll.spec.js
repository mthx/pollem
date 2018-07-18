import { shallowMount } from "@vue/test-utils";
import Poll from "@/components/Poll.vue";

describe("Poll.vue", () => {
  it("renders the given poll", () => {
    const question_text = "A or B?";
    const poll = { question_text };
    const wrapper = shallowMount(Poll, {
      propsData: { poll }
    });
    expect(wrapper.text()).toMatch(question_text);
  });
});
