<template>
  <v-app>
    <v-main>
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
      <router-view/>
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
  }
};
</script>
