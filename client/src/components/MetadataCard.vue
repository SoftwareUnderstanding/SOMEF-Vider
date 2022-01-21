<template>
  <v-container>

      <v-card>
        <!-- Card Header -->
          <v-container>
            <v-card-title>
              <v-row justify="space-between">
                <v-img
                    v-show="header.logo !== '(NO DATA AVAILABLE)'"
                    max-width="100px"
                    max-height="100px"
                    contain
                    :src="header.logo"
                ></v-img>
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
                <!-- UNCOMMENT WHEN THE FUNCTIONALITY IS FINISH
                <v-col align-self="center" md="auto">
                  <v-btn
                      icon
                  >
                    <v-icon>mdi-card-bulleted</v-icon>
                  </v-btn>
                </v-col>
                <v-col align-self="center" md="auto">
                  <v-btn
                      icon
                      @click="showFilterDialog = true"
                  >
                    <v-icon>mdi-filter</v-icon>
                  </v-btn>
                </v-col>
                -->
              </v-row>
            </v-card-title>

            <v-divider></v-divider>

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
                <v-row dense no-gutters justify="center">
                  <v-col align-self="center" md="auto">
                    <v-btn
                        icon
                        :href="header.repoURL" target="_blank"
                        :disabled="header.repoURL === '(NO DATA AVAILABLE)'"
                        color="#4078c0"
                    >
                      <v-icon>mdi-github</v-icon>
                    </v-btn>
                  </v-col>
                  <v-col align-self="center" md="auto">
                    <v-btn
                        icon
                        :href="header.docker" target="_blank"
                        :disabled="header.docker === '(NO DATA AVAILABLE)'"
                        color="#0db7ed"
                    >
                      <v-icon>mdi-docker</v-icon>
                    </v-btn>
                  </v-col>
                  <v-col align-self="center" md="auto">
                    <v-btn
                        icon
                        :href="header.notebooks" target="_blank"
                        :disabled="header.notebooks === '(NO DATA AVAILABLE)'"
                        color="#f37726"
                    >
                      <v-icon>mdi-notebook</v-icon>
                    </v-btn>
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
            {{ stringToTitleCase(item.name) }}
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
                  {{ stringToTitleCase(item.name) }}
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
                  <v-container fluid>
                    <v-row justify="center">
                      <v-col cols="11">
                        <confidence-chip
                            :value="subItem.confidence"
                            :threshold="threshold"
                        ></confidence-chip>
                        <extract-method-chip :value="subItem.extractionMethods.values().next().value"></extract-method-chip>
                        <editor
                            mode="viewer"
                            v-model="subItem.body"
                        />
                      </v-col>
                    </v-row>
                    <br/>
                  </v-container>
                </v-carousel-item>
              </v-carousel>

              <!-- String Content -->
              <v-container v-else>
                <v-row justify="center">
                  <v-col cols="11">
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

    <!--Filter Dialog-->
    <filter-dialog
        :show-dialog="showFilterDialog"
        @cancel="showFilterDialog=false"
        @apply="showFilterDialog=false"
    />

  </v-container>
</template>

<script>
import ConfidenceChip from "@/components/ConfidenceChip";
import ExtractMethodChip from "@/components/ExtractMethodChip";
import LastModifyChip from "@/components/LastModifyChip";
import FilterDialog from "@/components/FilterDialog";
import { Editor } from "vuetify-markdown-editor";
import Cite from "citation-js";

const METADATA_FIELDS_FOR_HEADER = [
  'codeRepository',
  'dateModified',
  'description',
  'hasBuildFile',
  'hasExecutableNotebook',
  'license',
  'logo',
  'long_title',
  'name',
  'stargazers_count',
  'releases',
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
  'stargazers_count',
];

const NO_DATA_AVAILABLE = "(NO DATA AVAILABLE)"

export default {
  name: "MetadataCard",
  components:{
    ConfidenceChip,
    ExtractMethodChip,
    LastModifyChip,
    Editor,
    FilterDialog,
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
    showFilterDialog: false,
    header:{
      title: null,
      stars: null,
      releaseLast: null,
      releaseTotal: null,
      sortDescription: null,
      license: null,
      dateLastModify: null,
      repoURL: null,
      docker: null,
      notebooks: null,
      logo: null,
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
        case 'hasBuildFile':
          this.header.docker = somefItem.excerpt[0]
          break
        case 'hasExecutableNotebook':
          this.header.notebooks = somefItem.excerpt[0]
          break
        case 'codeRepository':
          this.header.repoURL = somefItem.excerpt
          break
        case 'logo':
          this.header.logo = somefItem.excerpt
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
          panelItem.body = this.excerptToString(somefItem[0].excerpt)
          panelItem.confidence = somefItem[0].confidence[0]
          panelItem.extractionMethods = new Set().add(somefItem[0].technique)
        }
      }
      else{
        panelItem.name = name
        panelItem.body = this.excerptToString(somefItem.excerpt)
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
            template: 'citation-apa',
            lang: 'en-US',
            type: 'string'
          })
        }
      }
    },
    downloadMetadata(fileType){
      this.toggleDownloadSelector = false
      this.$emit('click-download', fileType)
    },
    stringToTitleCase(str){
      return str.replace("_"," ").replace(/([a-z])([A-Z])/g, '$1 $2').toLowerCase().split(' ').map(function (word) {
        return (word.charAt(0).toUpperCase() + word.slice(1));
      }).join(' ');
    },
    excerptToString(excerpt){
      let str = ''
      if(Array.isArray(excerpt)){
        for(let i=0; i<excerpt.length; i++){
          str += this.excerptToString(excerpt[i]) + ' | '
        }
      }
      else if(typeof excerpt === 'object'){
        for (const [key, value] of Object.entries(excerpt)) {
          str += key + ': ' + value + "\n"
        }
      }
      else{
        // Check if it is bibtex
        if(excerpt.charAt(0) === '@' && excerpt.charAt(excerpt.length-1) === '}'){
          str = "### APA Style\n" + this.parseCitation(excerpt) + "\n\n" +
              "### Bibtex\n" + excerpt
        }
        else{
          str = excerpt.toString()
        }
      }
      return str
    }
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