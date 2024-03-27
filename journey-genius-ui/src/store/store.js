// store/index.js

import { createStore } from "vuex";

const store = createStore({
  state: {
    city: null,
    state: "",
    dates: null,
    budget: null,
    activities: [],
    landmarks: [],
    shops: [],
    foods: [],
    hotels: [],


  },
  // directly update the state properties when committed 
  // We currently only use mutations for the Itinerary Page (the checkboxes are stored in vuex using mutation)
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
    // setBudget(state, budget) {
    //   state.budget = budget;
    // },
    // setActivities(state, activities) {
    //   state.activities = activities;
    // },
    // setLandmarks(state, landmarks) {
    //   state.landmarks = landmarks;
    // },


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
    updateHotels(state, hotels) {
      state.hotels = hotels;
    },
    updateBudget(state, budget) {
      state.budget = budget;
    },
    updateDates(state, dates) {
      state.dates = dates;
    },
    updateCity(state, city) {
      state.city = city;
    },

  },

  //used to commit the mutations.
  actions: {
    // Not needed
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
    
    // updateActivities({ commit }, activities) {
    //   commit("setActivities", activities);
    // },
    // updateLandmarks({ commit }, landmarks) {
    //   commit("setLandmarks", landmarks);
    // },
    // updateShopping({ commit }, shopping) {
    //   commit("setShopping", shopping);
    // },
    // updateDining({ commit }, dining) {
    //   commit("setDining", dining);
    // },

    // New actions to dispatch mutations for updating activities, landmarks, foods, and shops
    updateActivities({ commit }, activities) {
      commit("setActivities", activities);
    },
    updateLandmarks({ commit }, landmarks) {
      commit("setLandmarks", landmarks);
    },
    updateFoods({ commit }, foods) {
      commit("setFoods", foods);
    },
    updateShops({ commit }, shops) {
      commit("setShops", shops);
    },
    updateHotels({ commit }, hotels) {
      commit("setHotels", hotels);
    },
    updateBudget({ commit }, budget) {
      commit("setBudget", budget);
    },
    


  },

  //provide access to the state properties in a computed manner.
  getters: {
    // Not needed
    getCity: (state) => state.city,
    getState: (state) => state.state,
    getDates: (state) => state.dates,
    getBudget: (state) => state.budgets,
    // getActivities: (state) => state.activities,
    // getLandmarks: (state) => state.landmarks,
    // getShopping: (state) => state.shopping,
    // getDining: (state) => state.dining,

    // New getters for getting activities, landmarks, foods, and shops
    getActivities: (state) => state.activities,
    getLandmarks: (state) => state.landmarks,
    getFoods: (state) => state.foods,
    getShops: (state) => state.shops,
    getHotels: (state) => state.hotels,
    getBudget: (state) => state.budget,

  },
});

export default store;
