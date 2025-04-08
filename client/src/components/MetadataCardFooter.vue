<template>
    <v-container>
        <v-card-subtitle>
            <div class="info-row">
                <span class="label">Provenance: Extracted with somef {{ provenance_v }} and schema {{ provenance_s }} </span>
        </div>
        </v-card-subtitle>
  
    </v-container>
  </template>
  
  <script>
  
  export const NO_DATA_AVAILABLE = "NO DATA AVAILABLE"
  
  export default {
    name: "MetadataCardFooter",
    props: {  
      provenance_v: String,
      provenance_s: String,
      provenance_d: String
    },
    data: () => ({
      unavailable: NO_DATA_AVAILABLE
    })
  }
  </script>
  
  <style scoped>
  .info-row {
    display: flex;
    margin-bottom: 5px;
    justify-content: center;
  }
  .label {
    font-weight: bold;
  }
  .value {
    margin-left: 5px; 
  }
  </style>