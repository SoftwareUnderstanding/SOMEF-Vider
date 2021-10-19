<template>
  <v-card>
    <v-card-title class="text-center justify-center">
      Software Metadata Extraction
    </v-card-title>
    <v-container>
      <v-row justify="space-between">

        <v-col cols="6">
          <v-text-field
              placeholder="https://github.com/KnowledgeCaptureAndDiscovery/somef/"
              :outlined="true"
              v-model="url"
          >
          </v-text-field>
        </v-col>

        <v-col cols="2">
          <v-text-field
              placeholder="Threshold"
              v-model="threshold"
              :disabled="true"
              type='number'
              :outlined="true"
          >
          </v-text-field>
        </v-col>

        <v-spacer></v-spacer>

        <v-col cols="3">
          <v-btn
              color="primary"
              @click="clickSubmit"
              :loading="loading"
          >
            SUBMIT
          </v-btn>
        </v-col>

      </v-row>
    </v-container>
  </v-card>
</template>
<script>
export default {
  name: 'form-card',
  props: {
    clickSubmit: {},
    loading: {},
    threshold: {},
    url: {}
  }
}
</script>