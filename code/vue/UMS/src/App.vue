<script setup>
// import HelloWorld from './components/HelloWorld.vue'
</script>


<template>
  <!-- vuetifyのコンポーネントはv-appで囲う -->
  <v-app>
    <header>
      <v-app-bar app theme="dark">
        <v-toolbar-title>Tomoeda Academy</v-toolbar-title>
      </v-app-bar>
    </header>

    <v-main>
      <!-- メイン表示　ルーティングページ -->
      <router-view />
    </v-main>

  </v-app>

</template>

<style>

</style>
