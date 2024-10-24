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
      
      <metadata-card-footer :provenance_v="footer.provenance_v"
                            :provenance_s="footer.provenance_s"
                            :provenance_d="footer.provenance_d"
                            @download="(filetype) => $emit('download',filetype)"
                        
      />
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
import MetadataCardFooter from "@/components/MetadataCardFooter";
// Fields to include in the header
const HEADER_FIELDS_MAPPINGS = {
  LOGO: "logo",
  NAME: "name",
  TITLE: "full_title",
  STARTS: "stargazers_count",
  DESCRIPTION: "description",
  RELEASE: "releases",
  PROVENANCE: "somef_provenance",
  LAST_UPDATE: "date_updated",
  LICENSE: "license",
  REPOSITORY: "code_repository",
  DOCKER: "has_build_file",
  NOTEBOOKS: "executable_example",
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
    MetadataCardFooter,
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
    },
    footer: {
      provenance_v: null,
      provenance_s: null,
      provenance_d: null
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
          this.sortPanelItemsList()
        }
      }
    },
    buildHeaderItem(name, somefItem){
      switch (name) {
        case HEADER_FIELDS_MAPPINGS.LOGO:
          if(Array.isArray(somefItem)){
            this.header.logo = somefItem.reduce((a, b) => a.value > b.value ? a : b).result.value;
          }
          else {
            this.header.logo = somefItem.result.value
          }
          break
        case HEADER_FIELDS_MAPPINGS.TITLE:
          if(Array.isArray(somefItem)){
            this.header.title = somefItem.reduce((a, b) => a.value > b.value ? a : b).result.value;
          }
          else {
            this.header.title = somefItem.result.value
          }      
          break
        case HEADER_FIELDS_MAPPINGS.NAME:
          if(!this.header.title){
            if(Array.isArray(somefItem)){
              this.header.title = somefItem.reduce((a, b) => a.value > b.value ? a : b).result.value;
            }
            else {
              this.header.title = somefItem.result.value
            }  
          }
          break
        case HEADER_FIELDS_MAPPINGS.STARTS:
          if(Array.isArray(somefItem)){
            this.header.stars = somefItem.reduce((a, b) => a.value > b.value ? a : b).result.value;
          }
          else {
            this.header.stars = somefItem.result.value
          }   
          break
        case HEADER_FIELDS_MAPPINGS.DESCRIPTION:
          if(Array.isArray(somefItem)){
            this.header.sortDescription = somefItem.find(item => item.technique === 'GitHub_API').result.value;
          }
          else {
            this.header.sortDescription = somefItem.result.value
          }
          //Descripción es un caso especial porque además de header es panel
          //como para para el header obtenemos el item de descripción que tenga GitHub_API, para el resto nos quedamos 
          //con el resto de items
          this.panelItemsList.push(this.buildPanelItem(name,somefItem.filter(item => item.technique !== 'GitHub_API')))
          this.sortPanelItemsList()
          break
        case HEADER_FIELDS_MAPPINGS.RELEASE:
          this.header.releaseTotal = somefItem.length
          this.header.releaseLast = somefItem[0].result.name 
          // this.header.dateLastModify = new Date(somefItem[0].result.date_published)
          this.panelItemsList.push(this.buildPanelItem(name,somefItem))
          this.sortPanelItemsList()
          break
        case HEADER_FIELDS_MAPPINGS.PROVENANCE:
          this.footer.provenance_v = somefItem.somef_version
          console.log('Provenance version: ' + somefItem.somef_version)
          this.footer.provenance_s = somefItem.somef_schema_version
          console.log('Provenance schema: ' +somefItem.somef_schema_version)
          this.footer.provenance_d = somefItem.date
          console.log('Provenance extracted on: ' +somefItem.date)
          break
        case HEADER_FIELDS_MAPPINGS.LAST_UPDATE:
          if(Array.isArray(somefItem)){
            this.header.dateLastModify = new Date(somefItem.reduce((a, b) => a.value > b.value ? a : b).result.value);
          }
          else {
            this.header.dateLastModify = new Date(somefItem.result.value)
          }
          break
        case HEADER_FIELDS_MAPPINGS.LICENSE:
          this.header.license = somefItem[0].result.name + ' (' + somefItem[0].result.url + ')'
          break
        case HEADER_FIELDS_MAPPINGS.DOCKER:
          if (Array.isArray(somefItem)){
            this.header.docker = somefItem[0].result.value 
          }
          else {
            this.header.docker = somefItem.result.value
          }
          break
        case HEADER_FIELDS_MAPPINGS.NOTEBOOKS:
          if(Array.isArray(somefItem)){
            this.header.notebooks = somefItem.reduce((a, b) => a.value > b.value ? a : b).result.value;
          }
          else {
            this.header.notebooks = somefItem.result.value
          }
          break
        case HEADER_FIELDS_MAPPINGS.REPOSITORY:
          if(Array.isArray(somefItem)){
            this.header.repoURL = somefItem.reduce((a, b) => a.value > b.value ? a : b).result.value;
          }
          else {
            this.header.repoURL = somefItem.result.value
          }
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
            result: this.excerptToString(item.result,name)
          }
        })
      }
      else{
        panelItem.content = [{
          confidence: Array.isArray(somefItem.confidence) ? somefItem.confidence[0] : somefItem.confidence,
          extractionMethod: somefItem.technique,
          result: this.excerptToString(String(somefItem.result),name)
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
    excerptToString(result, name){
      let str = ''
      if(Array.isArray(result)){
        for(let i=0; i<result.length; i++){
          str += this.excerptToString(result[i], name) + ' | '
        }
      }
      else if(typeof result === 'object'){
        str = this.processObject(result,name)
      }
      else{
        // Check if it is bibtex
        if(result.charAt(0) === '@' && result.charAt(result.length-1) === '}'){
          str = "### APA Style\n" + this.parseCitation(result) + "\n\n" +
              "### Bibtex\n" + result
        }
        else{
          str = result.toString()
        }
      }
      return str
    },
    processObject(obj,name) {
      let str = "";

      if (name == 'releases' || name == 'citation') {
        for (const [key, value] of Object.entries(obj)) {
          if (typeof value === 'object') {
            str += this.processObject(value);
          } else {
            if (key != 'type') {
              if (key == 'value')
                str += value + "\n"      
              else 
                str += key + ': ' + value + "\n"
            }
          }
        }
      } else {
        for (const [key, value] of Object.entries(obj)) {
          if (key == 'value') {
            str += value +  "\n"
          }
        }   
      }

      return str;
    },
    sortPanelItemsList() {
      this.panelItemsList.sort((a, b) => {
        if (a.title < b.title) return -1;
        if (a.title > b.title) return 1;
        return 0;
      });
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