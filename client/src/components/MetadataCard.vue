<template>
      <v-card>
        <!-- Card Title -->
        <v-card-title>
          <v-container>
            <v-row justify="space-between">
              <v-col>
                TITLE
              </v-col>
              <v-col cols="1">
                <v-btn icon>
                  <v-icon>mdi-download</v-icon>
                </v-btn>
              </v-col>
            </v-row>

            <v-row align="center">
                <v-rating
                    value="4"
                    color="amber"
                    dense
                    half-increments
                    readonly
                    size="17"
                ></v-rating>
                <div class="grey--text ms-4 text-caption">
                  ({{ 4 }})
                </div>
            </v-row>
          </v-container>
        </v-card-title>

        <!-- Tab Headers -->
        <v-tabs
            v-model="tabIndex"
            show-arrows
        >
          <v-tab
              v-for="item in tabItemsList"
              :key="item.title"
          >
            {{ item.title }}
          </v-tab>
        </v-tabs>

        <!-- Tab Content -->
        <v-tabs-items v-model="tabIndex">
          <v-tab-item
              v-for="item in tabItemsList"
              :key="item.title"
          >
            <v-card flat>
              <v-card-text>{{ item.body }}</v-card-text>
              <confidence-chip :value="item.confidence"></confidence-chip>
              <extract-method-chip :value="item.extractionMethod"></extract-method-chip>

            </v-card>
          </v-tab-item>
        </v-tabs-items>

        <!-- TEST AREA-->
        <confidence-chip :value="0.35"></confidence-chip>
        <confidence-chip :value="63.2"></confidence-chip>
        <confidence-chip :value="90"></confidence-chip>
        <extract-method-chip value="github"></extract-method-chip>
        <extract-method-chip value="regular-expression"></extract-method-chip>
        <extract-method-chip value="asdf"></extract-method-chip>

      </v-card>
</template>

<script>
import ConfidenceChip from "@/components/ConfidenceChip";
import ExtractMethodChip from "@/components/ExtractMethodChip";

export default {
  name: "MetadataCard",
  components:{
    ConfidenceChip,
    ExtractMethodChip,
  },
  props: {
    metadata: null,
  },
  data: () => ({
    tabIndex: null,
    tabItemsList: [],
  }),
  methods:{
    generateTabs(rawMetadata) {
      for(let item in rawMetadata){
        this.tabItemsList.push(this.buildTabItem(item, rawMetadata[item]))
      }
    },
    buildTabItem(name, content){
      let tabItem = {
        title: null,
        body: null,
        confidence: null,
        extractionMethod: null,
      }

      if(Array.isArray(content)){
        tabItem.title = name
        tabItem.body = content[0].excerpt
        tabItem.confidence = content[0].confidence[0]*100
        tabItem.extractionMethod = content[0].technique
      }
      else{
        tabItem.title = name
        tabItem.body = content.excerpt
        tabItem.confidence = content.confidence[0]*100
        tabItem.extractionMethod = content.technique
      }
      return tabItem
    }
  },
  created() {
    this.generateTabs(this.metadata)
  }
}
</script>

<style scoped>

</style>