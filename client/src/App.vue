<template>
  <v-app>

    <!-- Header -->
    <v-app-bar app>
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
    </v-app-bar>

    <!-- Body -->
    <v-main>
        <router-view/>
    </v-main>

    <!-- Footer -->
    <v-footer>
      <v-spacer></v-spacer>
      <v-row justify="center" no-gutters>
        <v-col md="auto" align-self="center">
          <a href="https://oeg.fi.upm.es/">
            <v-img max-width="65px" max-heigh="65px" contain src="./assets/OEG-logo.png"/>
          </a>
        </v-col>
        <v-col md="auto" align-self="center">
          <a href="http://fi.upm.es/">
            <v-img max-width="65px" max-heigh="65px" contain src="./assets/ETSIINF-logo.png"/>
          </a>
        </v-col>
        <v-col md="auto" align-self="center">
          <a href="https://www.upm.es/">
            <v-img max-width="65px" max-heigh="65px" contain src="./assets/UPM-logo.png"/>
          </a>
        </v-col>
        <v-col class="text-center" align-self="center">
          2021 —
          <a href="https://github.com/SoftwareUnderstanding/SOMEF-Vider">
            <strong>SOMEF Vider</strong>
          </a>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
    </v-footer>

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
