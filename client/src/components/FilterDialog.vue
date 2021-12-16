<template>
    <v-dialog
      v-model="showDialog"
      persistent
      max-width="300px"
    >
      <v-card>
        <v-card-title class="text-h5">
          Filters
        </v-card-title>
        <v-card-text>
          <v-container fluid>
            <v-row dense no-gutters>
              <v-subheader>Techniques</v-subheader>
              <v-chip-group
                  multiple
                  column
                  v-model="currFilters.techniquesIdx"
                  active-class="grey darken-4--text"
              >
                <extract-method-chip
                    v-for="item in techniques"
                    :key="item"
                    :value="item"
                >
                </extract-method-chip>
              </v-chip-group>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="error"
              text
              @click="cancel"
          >
            Cancel
          </v-btn>
          <v-btn
              text
              @click="apply"
          >
          Apply
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
import ExtractMethodChip from "@/components/ExtractMethodChip";

const TECHNIQUES = [
  'GitHub API',
  'Regular expression',
  'Header extraction',
  'File Exploration',
  'Supervised classification'
];

export default {
  components: {
    ExtractMethodChip
  },
  props: {
    showDialog:{
      type: Boolean,
      default: false,
    }
  },
  data() {
    return {
      techniques: TECHNIQUES,
      prevFilters: {
        techniquesIdx: [],
      },
      currFilters: {
        techniquesIdx: [],
      },
    }
  },
  methods:{
    cancel(){
      this.currFilters = Object.assign({}, this.prevFilters)
      this.$emit('cancel');
    },
    apply(){
      this.prevFilters = Object.assign({}, this.currFilters)

      let inactiveTechniques = this.currFilters.techniquesIdx.map(idx => {return TECHNIQUES[idx]})
      let techniques = Array.from(TECHNIQUES).filter(x => !inactiveTechniques.includes(x))

      this.$emit('apply', {techniques: techniques});
    }
  }
}
</script>

<style scoped>

</style>