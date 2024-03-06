import { mount } from '@vue/test-utils';
import StartPlanning from '@/views/StartPlanning.vue';

describe('StartPlanning.vue', () => {
  it('should render the component with Google Autocomplete', async () => {
    // Mount the StartPlanning component
    const wrapper = mount(StartPlanning);

    // Find the input field for Google Autocomplete
    const inputField = wrapper.find('input[type="text"]');

    // Simulate user input
    inputField.setValue('New York');

    // Wait for the autocomplete event to fire
    await wrapper.vm.$nextTick();

    // Check if the autocomplete functionality is working
    expect(wrapper.vm.city).toBe('New York');
    // You can add more assertions here based on your specific requirements
  });
});
