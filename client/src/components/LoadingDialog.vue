<template>
    <v-dialog
        v-model="value"
        persistent
        width="300"
    >
      <v-card>
        <v-card-text class="text-center">
          We are analyzing your repository.
          <br>Time may vary depending on its size.
          <br><br>Please be patient.
          <v-progress-linear
              indeterminate
              color="blue"
              class="mb-0"
          ></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
</template>

<script>
export default {
  props:{
    value:{
      type: Boolean,
      default: false,
    }
  },

}
</script>