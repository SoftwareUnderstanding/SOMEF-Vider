<template>
  <v-tooltip top>
    <template v-slot:activator="{ on, attrs }">
      <v-chip
          v-bind="attrs"
          v-on="on"
          class="ma-2"
          :color="color"
          text-color="white"
      >
        <v-icon>
          mdi-alpha-c-circle
        </v-icon>
        {{percentageValue}}
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
  computed:{
    color: function () {
      if(this.value < 0.5){
        return 'red'
      }
      else if(0.5 < this.value  && this.value < 0.75){
        return 'orange'
      }
      else if(0.75 < this.value){
        return 'green'
      }
      else{
        return 'inherit'
      }
    },
    percentageValue: function (){
      return new Intl.NumberFormat('en-IN', { maximumSignificantDigits: 4 }).format(this.value*100) + '%'
    }
  }
}
</script>

<style scoped>
</style>