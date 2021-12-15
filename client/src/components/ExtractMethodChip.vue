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
    <span>{{ methodItem.name }}</span>
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
        color: 'purple',
        name: 'Regular Expression',
      },
      {
        idName: 'Header extraction',
        icon: 'mdi-xml',
        color: 'pink',
        name: 'Header Extraction',
      },
      {
        idName: 'File Exploration',
        icon: 'mdi-file-find',
        color: 'brown',
        name: 'File Exploration',
      },
      {
        idName: 'Supervised classification',
        icon: 'mdi-robot',
        color: '#8DB3E2',
        name: 'Supervised Classification',
      },

    ],
  }),
  computed:{
    methodItem: function (){
      let method = this.methodItemsList.find(item => item.idName === this.value)
      if(method === undefined){
        method = this.methodItemsList[0]
      }
      return method
    }
  }
}
</script>

<style scoped>
</style>