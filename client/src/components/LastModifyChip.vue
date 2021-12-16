<template>
  <v-tooltip top>
    <template v-slot:activator="{ on, attrs }">
      <v-chip
          v-bind="attrs"
          v-on="on"
          class="ma-2"
          :color="color"
          :text-color="$vuetify.theme.dark ? 'white' : 'black'"
          label
          outlined
      >
        <v-icon>
          mdi-calendar
        </v-icon>
        {{dateTime}}
      </v-chip>
    </template>
    <span>Last update of the repository</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "LastModifyDateChip",
  props:{
    value: {
      type: Date,
      default: null,
    }
  },
  computed:{
    dateTime: function (){
      return new Date(this.value).toUTCString()
    },
    color: function (){
      let dateMs = new Date(this.value).setHours(0)
      let todayMs = new Date().setHours(0)
      let diffDays = (todayMs - dateMs) / (1000 * 3600 * 24)

      if(diffDays > 90){
        return 'red'
      }
      else if(90 > diffDays && diffDays > 30){
        return 'orange'
      }
      else if(30 > diffDays){
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