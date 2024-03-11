// store/store.js
import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      hotelData: null,

      // selectedActivities: [],
      // selectedLandmarks: [],
      // selectedFoods: [],
      // selectedShops: [],
      isLoggedOn: false, // Global variable for login state
      selectedBudget: null,
    };
  },
  mutations: {
    setHotelData(state, data) {
      state.hotelData = data;
    },
    // updateSelectedActivities(state, selectedActivities) {
    //   state.selectedActivities = selectedActivities;
    // },
    // updateSelectedLandmarks(state, selectedLandmarks) {
    //   state.selectedLandmarks = selectedLandmarks;
    // },
    // updateSelectedFoods(state, selectedFoods) {
    //   state.selectedFoods = selectedFoods;
    // },
    // updateSelectedShops(state, selectedShops) {
    //   state.selectedShops = selectedShops;
    // },
    // Mutation to update the isLoggedOn variable
    updateIsLoggedOn(state, isLoggedOn) {
      state.isLoggedOn = isLoggedOn;
    },
    setSelectedBudget(state, budget) {
      state.selectedBudget = budget;
    },

  },
  getters: {
    selectedBudget(state) {
      return state.selectedBudget;
    },
  },
});

export default store;
