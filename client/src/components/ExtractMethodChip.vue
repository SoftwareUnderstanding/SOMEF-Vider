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
        name: 'Unknown',
        color: 'inherit'
      },
      {
        idName: 'github',
        icon: 'mdi-github',
        name: 'GitHub',
        color: 'blue'
      },
      {
        idName: 'regular-expression',
        icon: 'mdi-regex',
        name: 'Regular Expression',
        color: 'yellow'
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