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
                  <v-select
                      dense
                      :items="downloadFiletypesList"
                      v-show="toggleDownloadSelector"
                      :menu-props="{value:toggleDownloadSelector}"
                      @change="downloadMetadata"
                  />
                </v-col>
                <v-col align-self="center" md="auto">
                  <v-btn
                      icon
                      @click="toggleDownloadSelector = !toggleDownloadSelector"
                  >
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

        <!-- Tabs Names -->
        <v-tabs
            v-model="tabIndex"
            show-arrows
        >
          <v-tab
              v-for="item in panelItemsList"
              :key="item.name"
              @click="$vuetify.goTo('#'+item.name)"
          >
            {{ toTitleCase(item.name) }}
          </v-tab>
        </v-tabs>

        <!-- Expansion panels -->
        <v-expansion-panels focusable v-model="tabIndex">
          <v-expansion-panel
              v-for="item in panelItemsList"
              :key="item.name"
              :id="item.name"
          >

            <!-- Panel Header -->
            <v-expansion-panel-header>
              <v-row justify="space-between">
                <v-col md="auto" align-self="center">
                  {{ toTitleCase(item.name) }}
                </v-col>
                <v-col cols="3" md="auto">
                  <confidence-chip
                      v-if="item.confidence !== null"
                      :value="item.confidence"
                      :threshold="threshold"
                  ></confidence-chip>
                  <extract-method-chip
                      v-for="method in item.extractionMethods"
                      :value="method"
                      :key="item.name+'-'+method"
                  ></extract-method-chip>
                </v-col>
              </v-row>
            </v-expansion-panel-header>

            <!-- Panel Content -->
            <v-expansion-panel-content>
              <!-- Array Content -->
              <v-carousel
                  height="auto"
                  :show-arrows="item.body.length > 1"
                  hide-delimiter-background
                  v-if="Array.isArray(item.body)"
              >
                <v-carousel-item
                    v-for="subItem in item.body"
                    :key="subItem.name"
                >
                  <v-container>
                    <v-row justify="center">
                      <v-col cols="11">
                        <confidence-chip
                            :value="subItem.confidence"
                            :threshold="threshold"
                        ></confidence-chip>
                        <extract-method-chip :value="subItem.extractionMethods.values().next().value"></extract-method-chip>
                        <div v-if="item.name === 'citation'" v-html="parseCitation(subItem.body)"></div>
                        <editor
                            mode="viewer"
                            v-model="subItem.body"
                        />
                      </v-col>
                    </v-row>
                  </v-container>
                </v-carousel-item>
              </v-carousel>

              <!-- String Content -->
              <v-container v-else>
                <v-row justify="center">
                  <v-col cols="11">
                    <div v-if="item.name === 'citation'" v-html="parseCitation(item.body)"></div>
                    <editor
                        mode="viewer"
                        v-model="item.body"
                    />
                  </v-col>
                </v-row>
              </v-container>

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

const METADATA_FIELDS_FOR_HEADER = [
  'dateModified',
  'description',
  'license',
  'long_title',
  'name',
  'stargazers_count',
  'releases'
];

// Fields to exclude from the panel view
const METADATA_FILTERED_FIELDS = [
  'fullName',
  'codeRepository',
  'dateModified',
  'dateCreation',
  'license',
  'long_title',
  'name',
  'owner',
  'ownerType',
  'releases',
  'stargazers_count',
];

const NO_DATA_AVAILABLE = "(NO DATA AVAILABLE)"

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
    threshold:{
      type: Number,
      default: 0,
    }
  },
  data: () => ({
    tabIndex: null,
    panelItemsList: [],
    downloadFiletypesList: [
      {text:'JSON', value:'json'},
      {text:'CodeMeta', value: 'codemeta'},
      {text:'Turtle', value: 'turtle'},
    ],
    toggleDownloadSelector: false,
    header:{
      title: null,
      stars: null,
      releaseLast: null,
      releaseTotal: null,
      sortDescription: null,
      license: null,
      dateLastModify: null,
    }
  }),
  methods:{
    generateTabs(rawMetadata) {
      for(let item in rawMetadata){
        if(this.isHeaderItem(item)){
          this.buildHeaderItem(item, rawMetadata[item])
        }
        if(!this.isFilteredITem((item))){
          this.panelItemsList.push(this.buildPanelItem(item, rawMetadata[item]))
        }
      }
    },
    buildHeaderItem(name, somefItem){
      switch (name) {
        case 'long_title':
          this.header.title = somefItem.excerpt
          break
        case 'name':
          if(this.header.title === null){
            this.header.title = somefItem.excerpt
          }
          break
        case 'stargazers_count':
          this.header.stars = somefItem.excerpt.count
          break
        case 'description':
          if(Array.isArray(somefItem)){
            this.header.sortDescription = somefItem.reduce((a, b) => a.value > b.value ? a : b).excerpt;
          }
          else {
            this.header.sortDescription = somefItem.excerpt
          }
          break
        case 'releases':
          this.header.releaseTotal = somefItem.excerpt.length
          this.header.releaseLast = somefItem.excerpt[0].tag_name
          break
        case 'dateModified':
          this.header.dateLastModify = new Date(somefItem.excerpt)
          break
        case 'license':
          this.header.license = somefItem.excerpt.name + ' (' + somefItem.excerpt.url + ')'
          break
      }

      for (const [key, value] of Object.entries(this.header)) {
        if(!value){
          this.header[key] = NO_DATA_AVAILABLE
        }
      }

    },
    buildPanelItem(name, somefItem){
      let panelItem = {
        name: null,
        body: [],
        confidence: null,
        extractionMethods: new Set,
      }

      if(Array.isArray(somefItem)){
        if(somefItem.length>1){
          for(let i=0; i<somefItem.length; i++){
            panelItem.body.push(this.buildPanelItem(name+'-'+i, somefItem[i]))
            panelItem.extractionMethods.add(somefItem[i].technique)
          }
          panelItem.name = name
        }
        else{
          panelItem.name = name
          panelItem.body = somefItem[0].excerpt.toString()
          panelItem.confidence = somefItem[0].confidence[0]
          panelItem.extractionMethods = new Set().add(somefItem[0].technique)
        }
      }
      else{
        panelItem.name = name
        panelItem.body = somefItem.excerpt.toString()
        panelItem.confidence = somefItem.confidence[0]
        panelItem.extractionMethods = new Set().add(somefItem.technique)
      }

      return panelItem
    },

    isHeaderItem(name){
      return METADATA_FIELDS_FOR_HEADER.find(item => item === name) !== undefined
    },

    isFilteredITem(name){
      return METADATA_FILTERED_FIELDS.find(item => item === name) !== undefined
    },

    parseCitation(data){
      if(typeof data === 'string' || data instanceof String) {
        if(data.charAt(0) === '@'){
          return new Cite(data).format('bibliography', {
            format: 'html',
            template: 'citation-apa',
            lang: 'en-US'
          })
        }
      }
    },
    downloadMetadata(fileType){
      this.toggleDownloadSelector = false
      this.$emit('click-download', fileType)
    },
    toTitleCase(str){
      return str.replace("_"," ").replace(/([a-z])([A-Z])/g, '$1 $2').toLowerCase().split(' ').map(function (word) {
        return (word.charAt(0).toUpperCase() + word.slice(1));
      }).join(' ');
    },
  },
  created() {
    this.generateTabs(this.metadata)
  }
}
</script>

<style>
   .v-carousel__controls__item{
      color: gray !important
   }
</style>