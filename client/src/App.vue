<template>
  <v-app>
    <v-main>
      <v-breadcrumbs
          :items="navBar"
          divider="|"
      >
      </v-breadcrumbs>
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
};
</script>
