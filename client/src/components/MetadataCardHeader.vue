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
          {{ title ? title : unavailable}}
          <v-icon color="yellow" size="30">mdi-star-circle</v-icon>
          <a class="grey--text text-caption">
            ({{ stars ? stars :unavailable }})
          </a>
        </v-col>
        <v-spacer/>
        <v-col md="auto" align-self="center">
          <download-selector @download="(filetype) => $emit('download',filetype)"/>
        </v-col>
      </v-row>
    </v-card-title>

    <v-divider></v-divider>

    <v-card-subtitle>
      <v-card-text>
        {{ description ? description : unavailable}}
      </v-card-text>

      <v-row align-content="center" class="mx-0 my-0">
        <v-subheader class="subheader">Last Release:</v-subheader>
        <v-row justify="space-around" align-content="center">
          <v-col>
            {{lastRelease ? lastRelease : unavailable}}
          </v-col>
        </v-row>
      </v-row>

      <v-row align-content="center" class="mx-0 my-0">
        <v-subheader class="subheader">Releases:</v-subheader>
        <v-row justify="space-around" align-content="center">
          <v-col>
            {{totalReleases ? totalReleases : unavailable}}
          </v-col>
        </v-row>
      </v-row>

      <v-row align-content="center" class="mx-0 my-0">
        <v-subheader class="subheader">Last Update:</v-subheader>
        <v-row justify="space-around" align-content="center">
          <v-col>
            <last-modify-chip v-if="lastModify" :value="lastModify"/>
            <span v-else> {{unavailable}} </span>
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
import LastModifyChip from "@/components/LastModifyChip";

export const NO_DATA_AVAILABLE = "NO DATA AVAILABLE"

export default {
  name: "MetadataCardHeader",
  components: {DownloadSelector, LastModifyChip},
  props: {
    title: String,
    stars: Number,
    lastRelease: String,
    totalReleases: Number,
    description: String,
    license: String,
    lastModify: Date,
    docker: String,
    repo: String,
    notebooks: String,
    logo: String,
  },
  data: () => ({
    unavailable: NO_DATA_AVAILABLE
  })
}
</script>

<style scoped>
.subheader{
  width: 150px;
}

</style>