<template>
  <v-app>
    <v-main>

      <!-- Header -->
      <v-row>
        <v-col>
          <v-breadcrumbs
              :items="navBar"
              divider="|"
          >
          </v-breadcrumbs>
        </v-col>
        <v-col md="auto">
          <v-btn icon @click="toggleDarkMode">
            <v-icon>mdi-theme-light-dark</v-icon>
          </v-btn>
        </v-col>
      </v-row>

      <!-- Body -->
      <router-view/>

      <!-- Footer -->
      <v-footer absolute>
        <v-row justify="center" no-gutters>
          <v-img max-width="75px" max-heigh="75px" contain src="./assets/OEG-logo.png"/>
          <v-img max-width="75px" max-heigh="75px" contain src="./assets/ETSIINF-logo.png"/>
          <v-img max-width="75px" max-heigh="75px" contain src="./assets/UPM-logo.png"/>
          <v-col class="text-center" cols="12">
            <v-divider></v-divider>
            2021 — <strong>SOMEF Vider</strong>
          </v-col>
        </v-row>
      </v-footer>

    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    navBar:[
      {
        text: 'Home',
        disabled: false,
        href: '/#/',
      },
      {
        text: 'About',
        disabled: false,
        href: '/#/about',
      },
    ],
  }),
  methods:{
    toggleDarkMode(){
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
    }
  },
  beforeCreate() {
    document.title = "SOMEF Vider"
  }
};
</script>
