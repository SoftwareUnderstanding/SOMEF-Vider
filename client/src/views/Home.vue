<template>
  <v-container>
    <v-card-title class="text-center justify-center">
      <h1>SOMEF Vider</h1>
    </v-card-title>

    <somef-form @submit="submitForm"/>

    <loading-dialog :value="showLoadingDialog"/>

    <server-response-dialog
        v-if="showErrorDialog"
        :response="serverResponse"
        :showDialog="showErrorDialog"
    ></server-response-dialog>

    <metadata-card v-if="metadata"
                   :threshold="formData.threshold"
                   :metadata="metadata"
                   @download="downloadMetadata"
    />

    <!-- Button to top -->
    <v-tooltip left v-if="showMetadataCard">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            v-bind="attrs"
            v-on="on"
            fab
            dark
            fixed
            bottom
            right
            color="primary"
            @click="$vuetify.goTo(0)"
        >
          <v-icon>mdi-arrow-up</v-icon>
        </v-btn>
      </template>
      <span>Go to top</span>
    </v-tooltip>

  </v-container>
</template>

<script>
import MetadataCard from "@/components/MetadataCard";
import axiosService from "@/service/axiosService";
import ServerResponseDialog from "@/components/ServerResponseDialog";
import SomefForm from "@/components/SomefForm";
import LoadingDialog from "@/components/LoadingDialog";

export default {
  name: 'Home',
  components: {
    LoadingDialog,
    SomefForm,
    MetadataCard,
    ServerResponseDialog,
  },

  data: () => ({
    metadata: null,
    showLoadingDialog: false,
    showMetadataCard: false,
    showErrorDialog: false,
    serverResponse: null,
    formData: {
      url: null,
      threshold: null,
      ignoreClassifiers: false,
    }
  }),
  methods:{
    submitForm(url, threshold, ignoreClassifiers){
      this.formData = {
        url: url,
        threshold: threshold,
        ignoreClassifiers: ignoreClassifiers,
      }

      this.showErrorDialog = false
      this.showLoadingDialog = true
      this.showMetadataCard = false

      this.fetchMetadata(url, threshold, ignoreClassifiers)
    },
    fetchMetadata(url, threshold, ignoreClassifiers) {
      this.metadata = null
      axiosService.getMetadata(url, threshold, ignoreClassifiers)
          .then(response => {
            this.metadata = response.data
            this.showLoadingDialog = false
            this.showMetadataCard = true
          })
          .catch(error => {
            this.showLoadingDialog = false
            this.serverResponse = error.response
            this.showErrorDialog = true
          })
    },
    downloadMetadata(fileType){
      let filenames = {
        json: "metadata.json",
        codemeta: "codemeta.json",
        turtle: "graph.ttl"
      }
      axiosService.downloadMetadata(this.url, this.threshold, this.ignoreClassifiers, fileType)
          .then(response => {
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', filenames[fileType]);
            document.body.appendChild(link);
            link.click();
          })
          .catch(error => {
            console.log(error.response)
            this.serverResponse = error.response
            this.showErrorDialog = true
          })
    }
  }
}
</script>
