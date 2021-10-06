<template>
  <v-container>
    <v-card>
      <v-card-title>
        SOMEF WEBAPP
      </v-card-title>
      <v-container>
        <v-row justify="center" align-content="center">
          <v-col>
            <v-text-field
                placeholder="widoco"
                :outlined="true"
            >
            </v-text-field>
          </v-col>
          <v-col cols="2">
            <v-text-field
                placeholder="Thressold"
                :value="0.8"
                :disabled="true"
                type='number'
                :outlined="true"
            >
            </v-text-field>
          </v-col>
          <v-col>
            <v-btn
                color="primary"
                @click="getMetadata"
            >
              SUBMIT
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
  import Axios from "axios";

  export default {
    name: 'HelloWorld',

    data: () => ({

    }),
    methods:{
      getMetadata() {
        Axios.get("http://127.0.0.1:5000/test")
            .then(response => {
              console.log(response.data)
            })
            .catch(error => {
              console.log(error)
            })
      }
    }
  }
</script>
