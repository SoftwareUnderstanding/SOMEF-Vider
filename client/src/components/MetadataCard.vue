<template>
      <v-card>
        <!-- Card Header -->
          <v-container>

            <v-card-title>
              <v-row justify="space-between">
                <v-col align-self="center">
                  {{ header.title }}
                  <v-icon color="yellow" size="30">mdi-star-circle</v-icon>
                  <a class="grey--text text-caption">
                    ({{ header.stars }})
                  </a>
                </v-col>
                <v-col align-self="center" md="auto">
                  <v-btn icon>
                    <v-icon>mdi-download</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-card-title>

            <v-card-subtitle>
              <v-container fluid>
                <v-row>
                  <v-col>
                    <v-card-text>
                      {{ header.sortDescription }}
                    </v-card-text>
                  </v-col>
                </v-row>
                <v-row dense no-gutters>
                  <v-col cols="2" align-self="center">
                    <v-subheader>Last Release:</v-subheader>
                  </v-col>
                  <v-col align-self="center">
                    {{header.releaseLast}}
                  </v-col>
                </v-row>
                <v-row dense no-gutters>
                  <v-col cols="2" align-self="center">
                    <v-subheader>Releases:</v-subheader>
                  </v-col>
                  <v-col align-self="center">
                    {{header.releaseTotal}}
                  </v-col>
                </v-row>
                <v-row dense no-gutters>
                  <v-col cols="2" align-self="center">
                    <v-subheader>Last Update:</v-subheader>
                  </v-col>
                  <v-col align-self="center">
                    <last-modify-chip :value="header.dateLastModify"></last-modify-chip>
                  </v-col>
                </v-row>
                <v-row dense no-gutters>
                  <v-col cols="2" align-self="center">
                    <v-subheader>License:</v-subheader>
                  </v-col>
                  <v-col align-self="center">
                    {{header.license}}
                  </v-col>
                </v-row>
              </v-container>
            </v-card-subtitle>

          </v-container>

        <!-- Tab Name -->
        <v-tabs
            v-model="tabIndex"
            show-arrows
        >
          <v-tab
              v-for="item in panelItemsList"
              :key="item.name"
              @click="$vuetify.goTo('#'+item.name)"
          >
            {{ item.name }}
          </v-tab>
        </v-tabs>

        <!-- Expansion panels -->
        <v-expansion-panels focusable v-model="tabIndex">
          <v-expansion-panel
              v-for="item in panelItemsList"
              :key="item.name"
              :id="item.name"
          >
            <v-expansion-panel-header>
              <v-row justify="space-between">
                <v-col md="auto" align-self="center">
                  {{item.name}}
                </v-col>
                <v-col cols="3" md="auto">
                  <confidence-chip :value="item.confidence"></confidence-chip>
                  <extract-method-chip
                      v-for="method in item.extractionMethods"
                      :value="method"
                      :key="item.name+'-'+method"
                      >
                  </extract-method-chip>
                </v-col>
              </v-row>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <editor
                      mode="viewer"
                      v-model="item.body"
              />
              <div v-if="item.title === 'citation'" v-html="parseCitation(item.body)"></div>
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
import Cite from "citation-js";

const METADATA_FIELDS_FOR_HEADER = ['codeRepository','dateModified','description','downloadUrl','license','license_file','long_title','name','owner','ownerType'];

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
    panelItemsList: [],
    header:{
      title: "Default Tittle",
      stars: 150,
      releaseLast: '0.5.2',
      releaseTotal: 7,
      sortDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas venenatis sit amet purus nec pellentesque.verra elementum.",
      owner: "Owner",
      license: "MIT License",
      dateLastModify: new Date(),
      dateCreation: new Date(),
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
          this.panelItemsList.push(this.buildPanelItem(item, rawMetadata[item]))
        }
      }
      this.buildHeader(headerItemsList)
    },
    buildHeader(headerItemsList){
      // TODO finish method
      this.header.testList = headerItemsList
    },
    buildPanelItem(name, somefItem){
      let panelItem = {
        name: null,
        body: [],
        confidence: null,
        extractionMethods: new Set,
      }

      if(Array.isArray(somefItem)){
        let averageConfidence = 0
        for(let i=0; i<somefItem.length; i++){
          panelItem.body.push(this.buildPanelItem(i+'-'+name, somefItem[i]))
          averageConfidence = averageConfidence + Number(somefItem[i].confidence[0])
          panelItem.extractionMethods.add(somefItem[i].technique)
        }
        averageConfidence = averageConfidence / somefItem.length

        panelItem.name = name
        panelItem.confidence = averageConfidence
      }
      else{
        panelItem.name = name
        panelItem.body = [somefItem.excerpt.toString()]
        panelItem.confidence = somefItem.confidence[0]
        panelItem.extractionMethods = new Set().add(somefItem.technique)
      }

      return panelItem
    },

    isHeaderITem(name){
      let find = false;
      for(let i=0; i<METADATA_FIELDS_FOR_HEADER.length && !find; i++){
        find = METADATA_FIELDS_FOR_HEADER[i] === name
      }
      return find
    },
    parseCitation(data){
      let html = new Cite(data).format('bibliography', {
        format: 'html',
        template: 'citation-apa',
        lang: 'en-US'
      })
      return html
    }
  },
  created() {
    this.generateTabs(this.metadata)
  }
}
</script>

<style scoped>

</style>