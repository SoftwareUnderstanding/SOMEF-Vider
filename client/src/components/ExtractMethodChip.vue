<template>
  <v-tooltip top>
    <template v-slot:activator="{ on, attrs }">
      <v-chip
          v-bind="attrs"
          v-on="on"
          class="ma-2"
          :color="methodItem.color"
          text-color="white"
      >
        <v-icon>
          {{ methodItem.icon }}
        </v-icon>
      </v-chip>
    </template>
    <span>Extraction Method: {{ methodItem.name }}</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "ExtractMethodChip",
  props:{
    value: {
      type: String,
      default: '',
    }
  },
  data: () => ({
    methodItemsList: [
      {
        idName: 'unknown',
        icon: 'mdi-help-rhombus',
        color: 'inherit',
        name: 'Unknown',
      },
      {
        idName: 'GitHub API',
        icon: 'mdi-github',
        color: 'blue',
        name: 'GitHub API',
      },
      {
        idName: 'Regular expression',
        icon: 'mdi-regex',
        color: 'yellow',
        name: 'Regular Expression',
      },
      {
        idName: 'Header extraction',
        icon: 'mdi-xml',
        color: 'green',
        name: 'Header Extraction',
      },
      {
        idName: 'File Exploration',
        icon: 'mdi-file-find',
        color: 'brown',
        name: 'File Exploration',
      },

    ],
    methodItem:{
      icon: null,
      name: null,
      color: null
    }
  }),
  created(){
    this.methodItem = this.methodItemsList.find(item => item.idName === this.value)
    if(this.methodItem === undefined){
      this.methodItem = this.methodItemsList[0]
    }
  }
}
</script>

<style scoped>
</style>