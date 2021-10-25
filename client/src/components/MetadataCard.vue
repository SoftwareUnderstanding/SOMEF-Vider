<template>
      <v-card>
        <!-- Card Header -->
        <v-card-title>
          <v-container>

            <v-row justify="space-between">
              <v-col align-self="center">
                {{ header.title }}
                <v-icon color="yellow" size="30">mdi-star-circle</v-icon>
                <a class="grey--text text-caption">
                  ({{ header.stars }})
                </a>
              </v-col>

              <v-col align-self="center" md="auto">
                <last-modify-chip :value="header.lastModify"></last-modify-chip>
              </v-col>
              <v-col align-self="center" md="auto">
                <v-btn icon>
                  <v-icon>mdi-download</v-icon>
                </v-btn>
              </v-col>
            </v-row>

            <v-row>
              <v-card-subtitle>
                LAST RELEASE
              </v-card-subtitle>
            </v-row>
            <v-row>
              <v-card-text>
                <div>
                  {{header.owner}}
                </div>
                <div>
                  {{header.license}}
                </div>
                <div>
                  {{header.downloadLink}}
                </div>
              </v-card-text>
            </v-row>
          </v-container>
        </v-card-title>

        <!-- Tab Name -->
        <v-tabs
            v-model="tabIndex"
            show-arrows
        >
          <v-tab
              v-for="item in tabItemsList"
              :key="item.title"
              @click="$vuetify.goTo('#'+item.title)"
          >
            {{ item.title }}
          </v-tab>
        </v-tabs>

        <!-- Expansion panels -->
        <v-expansion-panels focusable v-model="tabIndex">
          <v-expansion-panel
              v-for="item in tabItemsList"
              :key="item.title"
              :id="item.title"
          >
            <v-expansion-panel-header>
              <v-row justify="space-between">
                <v-col md="auto" align-self="center">
                  {{item.title}}
                </v-col>
                <v-col cols="3" md="auto">
                  <confidence-chip :value="item.confidence"></confidence-chip>
                  <extract-method-chip :value="item.extractionMethod"></extract-method-chip>
                </v-col>
              </v-row>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <editor v-if="item.title === 'citation'"
                  mode="viewer"
                  v-model="item.body"
              />
              <div v-else>
                {{item.body}}
              </div>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>

      </v-card>
</template>

<script>
import ConfidenceChip from "@/components/ConfidenceChip";
import ExtractMethodChip from "@/components/ExtractMethodChip";
import LastModifyChip from "@/components/LastModifyChip";
import { Editor } from "vuetify-markdown-editor";

const METADATA_FIELDS_FOR_HEADER = ['codeRepository','dateModified','downloadUrl','license','license_file','long_title','name','owner','ownerType'];

export default {
  name: "MetadataCard",
  components:{
    ConfidenceChip,
    ExtractMethodChip,
    LastModifyChip,
    Editor
  },
  props: {
    metadata: null,
  },
  data: () => ({
    tabIndex: null,
    tabItemsList: [],
    header:{
      title: "Default Tittle",
      stars: 150,
      downloadLink: "https://example.com",
      owner: "Owner",
      lastModify: new Date(),
      license: "LICENSE EXAMPLE",
    }
  }),
  methods:{
    generateTabs(rawMetadata) {
      let headerItemsList = []
      for(let item in rawMetadata){
        if(this.isHeaderITem(item)){
          headerItemsList.push(rawMetadata[item])
        }
        else{
          this.tabItemsList.push(this.buildTabItem(item, rawMetadata[item]))
        }
      }
      this.buildHeader(headerItemsList)
    },
    buildHeader(headerItemsList){
      // TODO finish method
      this.header.testList = headerItemsList
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
    },
    isHeaderITem(name){
      let find = false;
      for(let i=0; i<METADATA_FIELDS_FOR_HEADER.length && !find; i++){
        find = METADATA_FIELDS_FOR_HEADER[i] === name
      }
      return find
    },
  },
  created() {
    this.generateTabs(this.metadata)
  }
}
</script>

<style scoped>

</style>