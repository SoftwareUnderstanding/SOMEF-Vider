<template>
  <v-tooltip top>
    <template v-slot:activator="{ on, attrs }">
      <v-chip
          v-bind="attrs"
          v-on="on"
          class="ma-2"
          :color="colorRenderer()"
          text-color="black"
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
  data: () => ({
    dateTime: null,
  }),
  methods:{
    colorRenderer(){
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
  },
  created(){
    this.dateTime = new Date(this.value).toUTCString()
  }
}
</script>

<style scoped>
</style>