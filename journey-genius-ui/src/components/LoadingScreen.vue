<template>
  <v-layout align-center justify-center>

  <div center class="loading-screen text-center">
    <v-row justify="center" style="height: 100vh; align-content: center;">
      <v-col cols="12">
        <div center class="d-flex justify-center loading-spinner"></div>
      </v-col>
      <v-col cols="12">
        <div class="loading-text">{{ progress }}%</div>
      </v-col>
      <v-col cols="12">
        <div class="loading-text2">Loading...</div>
      </v-col>
    </v-row>
  </div>
</v-layout>

</template>

<script>
export default {
  props: {
    isLoading: Boolean,
    progress: Number
  }
};
</script>

<style>
.loading-screen {
  display: flex;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.loading-spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #7c4dff;
  border-radius: 50%;
  width: 80px;
  height: 80px;
  animation: spin 1s linear infinite;
  /* display: inline-block; Remove inline-block */
  text-align: center;
  /* align-items: center; justify-content: center; Remove these */
  display: flex; /* Add this */
  align-items: center; /* Add this */
  justify-content: center; /* Add this */
  margin-left: 50%;
  margin-right: 50%;
  margin-top: 15px;
}


@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-text {
  color: #f3f3f3;
  margin-bottom: 40px;
  align-content: center;
  font-size: 20px;
}

.loading-text2 {
  color: #f3f3f3;
  /* margin-top: 15px; */
  font-size: 25px;
  align-content: center;
  margin-bottom: 60px;
}
</style>
