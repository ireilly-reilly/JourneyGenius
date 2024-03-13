// store/index.js

import { createStore } from "vuex";

const store = createStore({
  state: {
    city: "",
    state: "",
    dates: "",
    budget: "",
    activities: [],
    landmarks: [],
    shopping: [],
    dining: [],
  },
  mutations: {
    setCity(state, city) {
      state.city = city;
    },
    setState(state, stateName) {
      state.state = stateName;
    },
    setDates(state, dates) {
      state.dates = dates;
    },
    setBudget(state, budget) {
      state.budget = budget;
    },
    setActivities(state, activities) {
      state.activities = activities;
    },
    setLandmarks(state, landmarks) {
      state.landmarks = landmarks;
    },
    setShopping(state, shopping) {
      state.shopping = shopping;
    },
    setDining(state, dining) {
      state.dining = dining;
    },

    // New mutations to update activities, landmarks, foods, and shops
    updateActivities(state, activities) {
      state.activities = activities;
    },
    updateLandmarks(state, landmarks) {
      state.landmarks = landmarks;
    },
    updateFoods(state, foods) {
      state.foods = foods;
    },
    updateShops(state, shops) {
      state.shops = shops;
    },
  },
  actions: {
    updateCity({ commit }, city) {
      commit("setCity", city);
    },
    updateState({ commit }, stateName) {
      commit("setState", stateName);
    },
    updateDates({ commit }, dates) {
      commit("setDates", dates);
    },
    updateBudget({ commit }, budget) {
      commit("setBudget", budget);
    },
    updateActivities({ commit }, activities) {
      commit("setActivities", activities);
    },
    updateLandmarks({ commit }, landmarks) {
      commit("setLandmarks", landmarks);
    },
    updateShopping({ commit }, shopping) {
      commit("setShopping", shopping);
    },
    updateDining({ commit }, dining) {
      commit("setDining", dining);
    },
    // New actions to dispatch mutations for updating activities, landmarks, foods, and shops
    updateActivities({ commit }, activities) {
      commit("updateActivities", activities);
    },
    updateLandmarks({ commit }, landmarks) {
      commit("updateLandmarks", landmarks);
    },
    updateFoods({ commit }, foods) {
      commit("updateFoods", foods);
    },
    updateShops({ commit }, shops) {
      commit("updateShops", shops);
    },
  },
  getters: {
    getCity: (state) => state.city,
    getState: (state) => state.state,
    getDates: (state) => state.dates,
    getBudget: (state) => state.budget,
    getActivities: (state) => state.activities,
    getLandmarks: (state) => state.landmarks,
    getShopping: (state) => state.shopping,
    getDining: (state) => state.dining,
    // New getters for getting activities, landmarks, foods, and shops
    getActivities: (state) => state.activities,
    getLandmarks: (state) => state.landmarks,
    getFoods: (state) => state.foods,
    getShops: (state) => state.shops,
  },
});

export default store;
