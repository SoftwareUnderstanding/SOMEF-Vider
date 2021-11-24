<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="290"
    >
      <v-card>
        <v-card-title class="text-h5">
          {{title}}
        </v-card-title>
        <v-card-text>
          {{body}}
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Accept
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  name: "ServerResponseDialog",
  props:{
    response: {
      default(){
        return{
          data: null,
          status: null,
          statusText: null,
        }
      }
    },
    showDialog:{
      type: Boolean,
      default: false,
    }
  },
  data () {
    return {
      dialog: this.showDialog
    }
  },
  computed:{
    title: function (){
      switch (this.response.status){
        case 400:
          return "Bad Request"
        case 500:
          return "Server Error"
        default:
          return "Unknown Error"
      }
    },
    body: function(){
      return this.response.data
    },
  }
}
</script>

<style scoped>

</style>