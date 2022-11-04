<template>
  <v-container>
    <v-select
        dense
        :items="downloadTypes"
        v-show="toggleSelector"
        :menu-props="{value:toggleSelector}"
        @change="changeHandler"
    />
    <v-btn
        icon
        @click="toggleSelector = !toggleSelector"
    >
      <v-icon>mdi-download</v-icon>
    </v-btn>
  </v-container>
</template>

<script>
export default {
  name: "DownloadSelector",
  data: () => ({
    toggleSelector: false,
    downloadTypes: [
      {text:'JSON', value:'json'},
      {text:'CodeMeta', value: 'codemeta'},
      {text:'Turtle', value: 'turtle'},
    ]
  }),
  methods: {
    changeHandler(fileType){
      this.$emit("download", fileType)
      this.toggleSelector = false
    }
  },
}
</script>

<style scoped>

</style>