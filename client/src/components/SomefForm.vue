<template>
  <v-form ref="form">
    <v-row justify="space-between">

      <v-col align-self="center">
        <v-text-field
            id="url-input"
            placeholder="https://github.com/KnowledgeCaptureAndDiscovery/somef/"
            :outlined="true"
            v-model="url"
            :rules="rules.urlRules"
            required
            label="GitHub URL"
            @keydown="autocomplete"
        >
        </v-text-field>
      </v-col>

      <v-col cols="2" align-self="center" md="auto">
        <v-text-field
            id="threshold-input"
            hint="Numeric value between 0 and 1"
            placeholder="0.7"
            :max="1"
            :min="0"
            :step="0.1"
            required
            v-model="threshold"
            :rules="rules.thresholdRules"
            type="number"
            :outlined="true"
            label="Threshold"
            @keydown="autocomplete"
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
      if (!this.$refs.form.validate()) {
        setTimeout(() => {this.$refs.form.resetValidation();}, 5000);
      }
      else{
        this.$emit('submit', this.url, Number(this.threshold), this.ignoreClassifiers)
      }
    },
    autocomplete(keydown){
      if(keydown.key === "Tab") {
        switch (keydown.explicitOriginalTarget.id){
          case 'url-input':
            if(this.url === null || this.url === ""){
              this.url = "https://github.com/KnowledgeCaptureAndDiscovery/somef/"
            }
            break
          case 'threshold-input':
            if(this.threshold === null || this.threshold === "") {
              this.threshold = 0.7
            }
            break
        }
      }
    }
  }
}
</script>
