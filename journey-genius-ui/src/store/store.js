// store/index.js

import { createStore } from "vuex";
import createPersistedState from 'vuex-persistedstate';


const store = createStore({
  plugins: [createPersistedState()],

  state: {
    city: null,
    st: null,
    lat: null,
    long: null,
    dates: null,
    budget: null,
    activities: [],
    landmarks: [],
    shops: [],
    foods: [],
    hotels: [],
    cityDescription: null,
    citySlogan: null,
    tripLength: null,
    generated_activities: null,
    generated_hotels: null,
    generated_shops: null,
    generated_foods: null,      
    generated_landmarks: null,
    cityPictures: null,
    activityPictures: null,
    landmarkPictures: null,
    shopPictures: null,
    foodPictures: null,
    hotelPictures: null,
    activityAddresses: null,
    landmarkAddresses: null,
    shopAddresses: null,
    foodAddresses: null,
    hotelAddresses: null,
    sliderValue: null,
    descriptionToggle: false,
    
    tripObject: {
      id: null,
      city: null,
      city_description: null,
      activities: [],
      landmarks: [],
      foods: [],
      shops: [],
      hotels: [],
      state: null,
      dates: null,
      budget: null,
      latitude: null,
      longitude: null,
      city_slogan: null,
      generated_activities: null,
      generated_hotels: null,
      generated_shops: null,
      generated_foods: null,
      generated_landmarks: null,

    },
    
  },
  // directly update the state properties when committed 
  // We currently only use mutations for the Itinerary Page (the checkboxes are stored in vuex using mutation)
  mutations: {
    updateSelectionAmount(state, amount) {
      state.sliderValue = amount;
    },
    updateDescriptionToggle(state, toggle) {
      state.descriptionToggle = toggle;
    },
    updateSelections(state, payload) {
      state.selections = payload;
    },

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
    updateDates(state, datesData) {
      state.datesData = datesData;
    },
    // updateStartDates(state, startDates) {
    //   state.startDates = startDates;
    // },
    // updateEndDates(state, endDates) {
    //   state.endDates = endDates;
    // },
    updateCity(state, city) {
      state.city = city;
    },
    updateState(state, stateData) {
      state.stateData = stateData;
    },
    updateLat(state, lat) {
      state.lat = lat;
    },
    updateLong(state, long) {
      state.long = long;
    },
    updateCityDescription(state, cityDescription) {
      state.cityDescription = cityDescription;
    },
    updateCitySlogan(state, citySlogan) {
      state.citySlogan = citySlogan;
    },
    updateTripLength(state, tripLength) {
      state.tripLength = tripLength;
    },
    updateTripObject(state, tripObject) {
      state.tripObject = tripObject;
    },


    updateGeneratedActivities(state, generated_activities){
      state.generated_activities = generated_activities;
    },
    updateGeneratedLandmarks(state, generated_landmarks){
      state.generated_landmarks = generated_landmarks;
    },
    updateGeneratedShops(state, generated_shops){
      state.generated_shops = generated_shops;
    },
    updateGeneratedFoods(state, generated_foods){
      state.generated_foods = generated_foods;
    },
    updateGeneratedHotels(state, generated_hotels){
      state.generated_hotels = generated_hotels;
    },

    updateCityPictures(state, cityPictures){
      state.cityPictures = cityPictures;
    },
    updateActivityPictures(state, activityPictures){
      state.activityPictures = activityPictures;
    },
    updateLandmarkPictures(state, landmarkPictures){
      state.landmarkPictures = landmarkPictures;
    },
    updateFoodPictures(state, foodPictures){
      state.foodPictures = foodPictures;
    },
    updateShopPictures(state, shopPictures){
      state.shopPictures = shopPictures;
    },
    updateHotelPictures(state, hotelPictures){
      state.hotelPictures = hotelPictures;
    },

    updateActivityAddresses(state, activityAddresses){
      state.activityAddresses = activityAddresses;
    },
    updateLandmarkAddresses(state, landmarkAddresses){
      state.landmarkAddresses = landmarkAddresses;
    },
    updateFoodAddresses(state, foodAddresses){
      state.foodAddresses = foodAddresses;
    },
    updateShopAddresses(state, shopAddresses){
      state.shopAddresses = shopAddresses;
    },
    updateHotelAddresses(state, hotelAddresses){
      state.hotelAddresses = hotelAddresses;
    },

    updateSelectionAmount(state,selections){
      state.sliderValue = selections;
    },
    updateDescriptionToggle(state, toggle){
      state.descriptionToggle = toggle;
    },
  },

  //used to commit the mutations.
  actions: {
    updateSliderValue({ commit }, value) {
      commit('setSliderValue', value);
    },
    updateDescriptionToggle({ commit }, value) {
      commit('setDescriptionToggle', value);
    },
    updateSelections({ commit }, value) {
      commit('setSelections', value);
    },
    // Not needed
    updateCity({ commit }, city) {
      commit("setCity", city);
    },
    updateState({ commit }, stateName) {
      commit("setState", stateName);
    },
    updateDates({ commit }, datesData) {
      commit("setDates", datesData);
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
    getDates: (state) => state.datesData,
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
