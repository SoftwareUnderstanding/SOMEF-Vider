<template>
  <v-form ref="form">
    <v-row justify="space-between">

      <v-col align-self="center">
        <v-text-field
            placeholder="https://github.com/KnowledgeCaptureAndDiscovery/somef/"
            :outlined="true"
            v-model="url"
            :rules="rules.urlRules"
            required
            label="GitHub URL"
        >
        </v-text-field>
      </v-col>

      <v-col cols="2" align-self="center" md="auto">
        <v-text-field
            placeholder="Threshold"
            :max="1"
            :min="0"
            :step="0.1"
            required
            v-model="threshold"
            :rules="rules.thresholdRules"
            type='number'
            :outlined="true"
            label="Threshold"
        >
        </v-text-field>
      </v-col>

      <v-col cols="2" md="auto">
        <v-btn
            height="56px"
            color="primary"
            @click="submit"
        >
          SUBMIT
        </v-btn>
      </v-col>

    </v-row>
  </v-form>
</template>

<script>

export default {
  name: 'SomefForm',

  data: () => ({
    url: null,
    threshold: null,
    ignoreClassifiers: false,
    rules:{
      urlRules: [
        v => !!v || 'GitHub URL is required',
        //v => /^(https?:\\)?([\da-z.-]+)\.([a-z.]{2,6})([\\w .-]*)*\?$/.test(v) || 'Must be valid url',
      ],
      thresholdRules:[
        v => !!v || 'Threshold is required',
        v => (0 <= v && v <= 1) || 'Threshold must be between 0 and 1',
      ],
    },
  }),
  methods:{
    submit(){
      if (!this.$refs.form.validate()) return

      this.$emit('submit', this.url, this.threshold, this.ignoreClassifiers)
    },
  }
}
</script>
