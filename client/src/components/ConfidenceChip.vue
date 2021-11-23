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
    },
    threshold:{
      type: Number,
      default: 0,
    }
  },
  computed:{
    color: function () {
      let low = ((1-this.threshold)/3) + this.threshold
      let high = (((1-this.threshold)/3)*2) + this.threshold

      if(this.value <= low){
        return 'red'
      }
      else if(low < this.value  && this.value <= high){
        return 'orange'
      }
      else if(high < this.value){
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