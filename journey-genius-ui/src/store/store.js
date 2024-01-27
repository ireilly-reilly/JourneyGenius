// store.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    selectedActivities: [],
    selectedLandmarks: [],
    selectedFoods: [],
    selectedShops: [],
  },
  mutations: {
    updateSelectedActivities(state, selectedActivities) {
      state.selectedActivities = selectedActivities;
    },
    updateSelectedLandmarks(state, selectedLandmarks) {
      state.selectedLandmarks = selectedLandmarks;
    },
    updateSelectedFoods(state, selectedFoods) {
      state.selectedFoods = selectedFoods;
    },
    updateSelectedShops(state, selectedShops) {
      state.selectedShops = selectedShops;
    },
  },
});
