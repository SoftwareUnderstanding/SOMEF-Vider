<template>
  <v-tooltip top>
    <template v-slot:activator="{ on, attrs }">
      <v-chip
          v-bind="attrs"
          v-on="on"
          class="ma-2"
          :color="colorRenderer()"
          text-color="white"
      >
        <v-icon>
          mdi-alpha-c-circle
        </v-icon>
        {{value}}%
      </v-chip>
    </template>
    <span>Confidence</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "ConfidenceChip",
  props:{
    value: {
      type: Number,
      default: 0,
    }
  },
  methods: {
    colorRenderer(){
      if(this.value < 50){
        return 'red'
      }
      else if(50 < this.value  && this.value < 75){
        return 'orange'
      }
      else if(75 < this.value){
        return 'green'
      }
      else{
        return 'inherit'
      }
    }
  }
}
</script>

<style scoped>
</style>