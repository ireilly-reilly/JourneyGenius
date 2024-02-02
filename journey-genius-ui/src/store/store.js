// store.js
import { createStore } from 'vuex';
import Vue from 'vue';
import Vuex from 'vuex';



export default createStore({
  state: {
    selectedActivities: [],
    selectedLandmarks: [],
    selectedFoods: [],
    selectedShops: [],
    isLoggedOn: false, //Global variable for login state
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
    //mutation to update the isLoggedOn variable
    updateIsLoggedOn(state, isLoggedOn) {
      state.isLoggedOn = isLoggedOn;
    },
  },
});
