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
        idName: 'GitHub_API',
        icon: 'mdi-github',
        color: 'blue',
        name: 'GitHub API',
      },
      {
        idName: 'regular_expression',
        icon: 'mdi-regex',
        color: 'purple',
        name: 'Regular Expression',
      },
      {
        idName: 'header_analysis',
        icon: 'mdi-xml',
        color: 'pink',
        name: 'Header Extraction',
      },
      {
        idName: 'file_exploration',
        icon: 'mdi-file-find',
        color: 'brown',
        name: 'File Exploration',
      },
      {
        idName: 'supervised_classification',
        icon: 'mdi-robot',
        color: '#8DB3E2',
        name: 'Supervised Classification',
      },
      {
        idName: 'software_type_heuristics',
        icon: 'mdi-lightbulb-on-10',
        color: '#E77D66',
        name: 'Software Type Heuristics',
      },
      {
        idName: 'code_parser',
        icon: 'mdi-code-braces',
        color: '#BFB21D',
        name: 'Code Parser',
      },
      {
        idName: 'GitLab_API',
        icon: 'mdi-gitlab',
        color: 'orange',
        name: 'GitLab',
      }
    ],
  }),
  computed:{
    methodItem: function (){
      // console.log(this.value)
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