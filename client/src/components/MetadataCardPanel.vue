<template>
  <v-expansion-panel :id="id">

    <!-- Panel Header -->
    <v-expansion-panel-header>
      {{title}}
      <v-row justify="end" class="mr-3">
          <confidence-chip v-if="content.length===1"
                           :value="content[0].confidence"
                           :threshold="threshold"
          />
          <extract-method-chip v-for="(method, index) in extractionMethodList"
                               :value="method"
                               :key="index"
          />
      </v-row>
    </v-expansion-panel-header>

    <!-- Panel Content -->
    <v-expansion-panel-content v-if="content.length>1">
      <!-- Array Content -->
      <v-carousel height="auto"
                  show-arrows hide-delimiter-background
      >
        <v-carousel-item v-for="(item, index) in content"
                         :key="index"
        >
          <v-container fluid>
            <v-row justify="center">
              <v-col cols="11">
                <confidence-chip
                    :value="item.confidence"
                    :threshold="threshold"
                />
                <extract-method-chip :value="item.extractionMethod"/>
                <editor
                    mode="viewer"
                    v-model="item.excerpt"
                />
              </v-col>
            </v-row>
            <br/>
          </v-container>
        </v-carousel-item>
      </v-carousel>
    </v-expansion-panel-content>

    <!-- String Content -->
    <v-expansion-panel-content v-if="content.length===1">
      <v-container>
        <v-row justify="center">
          <v-col cols="11">
            <editor mode="viewer"
                    v-model="content[0].excerpt"
            />
          </v-col>
        </v-row>
      </v-container>
    </v-expansion-panel-content>

  </v-expansion-panel>
</template>

<script>
import { Editor } from "vuetify-markdown-editor";
import ConfidenceChip from "@/components/ConfidenceChip";
import ExtractMethodChip from "@/components/ExtractMethodChip";

export default {
  name: "MetadataCardPanel",
  components: {
    Editor, ConfidenceChip, ExtractMethodChip
  },
  props: {
    id: String,
    title: {
      type: String,
      default: ""
    },
    threshold: Number,
    content: Array
  },
  computed: {
    extractionMethodList(){
      return new Set(this.content.map(item => {
        return item.extractionMethod
      }))
    }
  },
  methods: {

  }
}
</script>

<style scoped>

</style>