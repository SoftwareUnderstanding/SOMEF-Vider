<template>
  <v-container>

    <v-card-title>
      <v-row justify="space-between" align-content="center">
        <v-col md="auto">
          <v-img
              v-show="logo"
              max-width="100px"
              max-height="100px"
              contain
              :src="logo"
          />
        </v-col>
        <v-col md="auto" align-self="center">
          {{ title }}
          <v-icon color="yellow" size="30">mdi-star-circle</v-icon>
          <a class="grey--text text-caption">
            ({{ stars }})
          </a>
        </v-col>
        <v-spacer/>
        <v-col md="auto" align-self="center">
          <download-selector/>
        </v-col>
      </v-row>
    </v-card-title>

    <v-divider></v-divider>

    <v-card-subtitle>
      <v-container fluid>
        <v-row>
          <v-col>
            <v-card-text>
              {{ description }}
            </v-card-text>
          </v-col>
        </v-row>
        <v-row dense no-gutters>
          <v-col cols="2" align-self="center">
            <v-subheader>Last Release:</v-subheader>
          </v-col>
          <v-col align-self="center">
            {{lastRelease}}
          </v-col>
        </v-row>
        <v-row dense no-gutters>
          <v-col cols="2" align-self="center">
            <v-subheader>Releases:</v-subheader>
          </v-col>
          <v-col align-self="center">
            {{totalReleases}}
          </v-col>
        </v-row>
        <v-row dense no-gutters>
          <v-col cols="2" align-self="center">
            <v-subheader>Last Update:</v-subheader>
          </v-col>
          <v-col align-self="center">
            <last-modify-chip :value="lastModify"></last-modify-chip>
          </v-col>
        </v-row>
        <v-row dense no-gutters>
          <v-col cols="2" align-self="center">
            <v-subheader>License:</v-subheader>
          </v-col>
          <v-col align-self="center">
            {{license}}
          </v-col>
        </v-row>
        <v-row dense no-gutters justify="center">
          <v-col align-self="center" md="auto">
            <v-btn
                icon
                :href="repo" target="_blank"
                :disabled="!repo"
                color="#4078c0"
            >
              <v-icon>mdi-github</v-icon>
            </v-btn>
          </v-col>
          <v-col align-self="center" md="auto">
            <v-btn
                icon
                :href="docker" target="_blank"
                :disabled="!docker"
                color="#0db7ed"
            >
              <v-icon>mdi-docker</v-icon>
            </v-btn>
          </v-col>
          <v-col align-self="center" md="auto">
            <v-btn
                icon
                :href="notebooks" target="_blank"
                :disabled="!notebooks"
                color="#f37726"
            >
              <v-icon>mdi-notebook</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-card-subtitle>
  </v-container>
</template>

<script>

import DownloadSelector from "@/components/DownloadSelector";
const NO_DATA_AVAILABLE = "NO DATA AVAILABLE"

export default {
  name: "MetadataCardHeader",
  components: {DownloadSelector},
  props: {
    title: {
      type: String,
      default: NO_DATA_AVAILABLE
    },
    stars: {
      type: Number,
      default: NO_DATA_AVAILABLE
    },
    lastRelease: {
      type: String,
      default: NO_DATA_AVAILABLE
    },
    totalReleases: {
      type: Number,
      default: NO_DATA_AVAILABLE
    },
    description: {
      type: String,
      default: NO_DATA_AVAILABLE
    },
    license: {
      type: String,
      default: NO_DATA_AVAILABLE
    },
    lastModify: {
      type: Date,
      default: NO_DATA_AVAILABLE
    },
    docker: {
      type: String,
      default: null
    },
    repo: {
      type: String,
      default: null
    },
    notebooks: {
      type: String,
      default: null
    },
    logo: {
      type: String,
      default: NO_DATA_AVAILABLE
    },



  }
}
</script>

<style scoped>

</style>