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
                  v-model="currFilters.techniques"
                  active-class="grey darken-4--text"
              >
                <extract-method-chip
                    v-for="tag in techniques"
                    :key="tag"
                    :value="tag"
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
      techniques:['GitHub API', 'Regular expression', 'Header extraction', 'File Exploration', 'Supervised classification'],
      prevFilters: {
        techniques: [],
        threshold: null,
      },
      currFilters: {
        techniques:['GitHub API', 'Regular expression', 'Header extraction', 'File Exploration', 'Supervised classification'],
        threshold: null,
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
      let filter = []
      for(let index in this.currFilters.techniques){
        filter.push(this.techniques[index])
      }
      this.$emit('apply', filter);
    }
  }
}
</script>

<style scoped>

</style>