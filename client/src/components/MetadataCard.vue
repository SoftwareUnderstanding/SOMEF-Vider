<template>
  <v-container>

    <v-card>
      <!-- Card Header -->
      <metadata-card-header :logo="header.logo"
                            :title="header.title"
                            :stars="header.stars"
                            :description="header.sortDescription"
                            :last-modify="header.dateLastModify"
                            :last-release="header.releaseLast"
                            :total-releases="header.releaseTotal"
                            :license="header.license"
                            :docker="header.docker"
                            :notebooks="header.notebooks"
                            :repo="header.repoURL"
                            @download="(filetype) => $emit('download',filetype)"
      />

      <!-- Tabs Names -->
      <v-tabs
          v-model="tabIndex"
          show-arrows
      >
        <v-tab
            v-for="item in panelItemsList"
            :key="item.title"
            @click="$vuetify.goTo('#'+item.title)"
        >
          {{item.title}}
        </v-tab>
      </v-tabs>

      <!-- Expansion panels -->
      <v-expansion-panels focusable v-model="tabIndex">
        <metadata-card-panel v-for="panel in panelItemsList"
                             :key="panel.title"
                             :id="panel.title"
                             :threshold="threshold"
                             :title="panel.title"
                             :content="panel.content"
        />
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

import FilterDialog from "@/components/FilterDialog";
import Cite from "citation-js";
import MetadataCardHeader from "@/components/MetadataCardHeader";
import MetadataCardPanel from "@/components/MetadataCardPanel";

// Fields to include in the header
const HEADER_FIELDS_MAPPINGS = {
  LOGO: "logo",
  NAME: "name",
  TITLE: "long_title",
  STARTS: "stargazers_count",
  DESCRIPTION: "description",
  RELEASE: "releases",
  LAST_UPDATE: "dateModified",
  LICENSE: "license",
  REPOSITORY: "codeRepository",
  DOCKER: "hasBuildFile",
  NOTEBOOKS: "hasExecutableNotebook",
}

// Fields to exclude from the panel view
const FILTERED_FIELDS_MAPPINGS = {
  FULL_NAME: "fullName",
  CREATION_DATE: "dateCreation",
  OWNER: "owner",
  OWNER_TYPE: "owner",
}

export default {
  name: "MetadataCard",
  components:{
    MetadataCardPanel,
    MetadataCardHeader,
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
    showFilterDialog: false,
    header: {
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
    mapMetadataFields(rawMetadata) {
      for(let item in rawMetadata){
        let isHeaderField = Object.values(HEADER_FIELDS_MAPPINGS).includes(item)
        let isFilteredField = Object.values(FILTERED_FIELDS_MAPPINGS).includes(item)

        if(isHeaderField){
          this.buildHeaderItem(item, rawMetadata[item])
        }
        else if(!isFilteredField){
          this.panelItemsList.push(this.buildPanelItem(item, rawMetadata[item]))
        }
      }
    },
    buildHeaderItem(name, somefItem){
      switch (name) {
        case HEADER_FIELDS_MAPPINGS.LOGO:
          this.header.logo = somefItem.excerpt
          break
        case HEADER_FIELDS_MAPPINGS.TITLE:
          this.header.title = somefItem.excerpt
          break
        case HEADER_FIELDS_MAPPINGS.NAME:
          if(!this.header.title){
            this.header.title = somefItem.excerpt
          }
          break
        case HEADER_FIELDS_MAPPINGS.STARTS:
          this.header.stars = somefItem.excerpt.count
          break
        case HEADER_FIELDS_MAPPINGS.DESCRIPTION:
          if(Array.isArray(somefItem)){
            this.header.sortDescription = somefItem.reduce((a, b) => a.value > b.value ? a : b).excerpt;
          }
          else {
            this.header.sortDescription = somefItem.excerpt
          }
          break
        case HEADER_FIELDS_MAPPINGS.RELEASE:
          this.header.releaseTotal = somefItem.excerpt.length
          this.header.releaseLast = somefItem.excerpt[0].tag_name
          break
        case HEADER_FIELDS_MAPPINGS.LAST_UPDATE:
          this.header.dateLastModify = new Date(somefItem.excerpt)
          break
        case HEADER_FIELDS_MAPPINGS.LICENSE:
          this.header.license = somefItem.excerpt.name + ' (' + somefItem.excerpt.url + ')'
          break
        case HEADER_FIELDS_MAPPINGS.DOCKER:
          this.header.docker = Array.isArray(somefItem) ?
              somefItem[0].excerpt[0] :
              Array.isArray(somefItem.excerpt) ? somefItem.excerpt[0] : somefItem.excerpt
          break
        case HEADER_FIELDS_MAPPINGS.NOTEBOOKS:
          this.header.notebooks = somefItem.excerpt[0]
          break
        case HEADER_FIELDS_MAPPINGS.REPOSITORY:
          this.header.repoURL = somefItem.excerpt
          break
      }
    },
    buildPanelItem(name, somefItem){
      let panelItem = {
        title: this.stringToTitleCase(name),
        content: [],
      }

      if(Array.isArray(somefItem)){
        panelItem.content = somefItem.map(item => {
          return {
            confidence: Array.isArray(item.confidence) ? item.confidence[0] : item.confidence,
            extractionMethod: item.technique,
            excerpt: this.excerptToString(item.excerpt)
          }
        })
      }
      else{
        panelItem.content = [{
          confidence: Array.isArray(somefItem.confidence) ? somefItem.confidence[0] : somefItem.confidence,
          extractionMethod: somefItem.technique,
          excerpt: this.excerptToString(somefItem.excerpt)
        }]
      }

      return panelItem
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
    },

    stringToTitleCase(str) {
      return str.replace("_"," ").replace(/([a-z])([A-Z])/g, '$1 $2').toLowerCase().split(' ').map(function (word) {
        return (word.charAt(0).toUpperCase() + word.slice(1));
      }).join(' ');
    },
  },
  created() {
    this.mapMetadataFields(this.metadata)
  }
}
</script>

<style>
</style>