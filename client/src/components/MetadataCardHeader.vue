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
      <v-card-text>
        {{ description }}
      </v-card-text>

      <v-row align-content="center" class="mx-0 my-0">
        <v-subheader class="subheader">Last Release:</v-subheader>
        <v-row justify="space-around" align-content="center">
          <v-col>
            {{lastRelease}}
          </v-col>
        </v-row>
      </v-row>

      <v-row align-content="center" class="mx-0 my-0">
        <v-subheader class="subheader">Releases:</v-subheader>
        <v-row justify="space-around" align-content="center">
          <v-col>
            {{totalReleases}}
          </v-col>
        </v-row>
      </v-row>

      <v-row align-content="center" class="mx-0 my-0">
        <v-subheader class="subheader">Last Update:</v-subheader>
        <v-row justify="space-around" align-content="center">
          <v-col>
            <last-modify-chip :value="lastModify"/>
          </v-col>
        </v-row>
      </v-row>

      <v-row align-content="center" class="mx-0 my-0">
        <v-subheader class="subheader">License:</v-subheader>
        <v-row justify="space-around" align-content="center">
          <v-col>
            {{license}}
          </v-col>
        </v-row>
      </v-row>

      <v-row align-content="space-around" class="mx-0 my-0">
        <v-spacer/>
        <v-btn
            icon
            :href="repo" target="_blank"
            :disabled="!repo"
            color="#4078c0"
        >
          <v-icon>mdi-github</v-icon>
        </v-btn>

        <v-btn
            icon
            :href="docker" target="_blank"
            :disabled="!docker"
            color="#0db7ed"
        >
          <v-icon>mdi-docker</v-icon>
        </v-btn>

        <v-btn
            icon
            :href="notebooks" target="_blank"
            :disabled="!notebooks"
            color="#f37726"
        >
          <v-icon>mdi-notebook</v-icon>
        </v-btn>

        <v-spacer/>
      </v-row>
    </v-card-subtitle>

  </v-container>
</template>

<script>

import DownloadSelector from "@/components/DownloadSelector";
export const NO_DATA_AVAILABLE = "NO DATA AVAILABLE"

export default {
  name: "MetadataCardHeader",
  components: {DownloadSelector},
  props: {
    title: {
      type: String,
      default: "Default title"
    },
    stars: {
      type: Number,
      default: 696969669
    },
    lastRelease: {
      type: String,
      default: "696969.696969"
    },
    totalReleases: {
      type: Number,
      default: 69696
    },
    description: {
      type: String,
      default: "Default description"
    },
    license: {
      type: String,
      default: "Default license"
    },
    lastModify: {
      type: Date,
      default: new Date()
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
    },



  }
}
</script>

<style scoped>
.subheader{
  width: 150px;
}

</style>