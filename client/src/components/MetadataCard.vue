<template>
      <v-card>
        <!-- Card Title -->
        <v-card-title>
          <v-container>
            <v-row justify="space-between">
              <v-col>
                <confidence-chip :value="0.35"></confidence-chip>
                <confidence-chip :value="55"></confidence-chip>
                <confidence-chip :value="1222"></confidence-chip>
              </v-col>
              <v-col>
                TITLE
              </v-col>
              <v-col cols="1">
                <v-btn icon>
                  <v-icon>mdi-download</v-icon>
                </v-btn>
              </v-col>
            </v-row>
            <v-row align="center">
                <v-rating
                    v-model="rating"
                    color="amber"
                    dense
                    half-increments
                    readonly
                    size="17"
                ></v-rating>
                <div class="grey--text ms-4 text-caption">
                  ({{ rating }})
                </div>
            </v-row>
          </v-container>
        </v-card-title>

        <!-- Tab Headers -->
        <v-tabs
            v-model="tab"
            show-arrows
        >
          <v-tab
              v-for="item in tabItems"
              :key="item.tab"
          >
            {{ item.tab }}
          </v-tab>
        </v-tabs>

        <!-- Tab Content -->
        <v-tabs-items v-model="tab">
          <v-tab-item
              v-for="item in tabItems"
              :key="item.tab"
          >
            <v-card flat>
              <v-card-text>{{ item.content }}</v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs-items>

      </v-card>
</template>

<script>
import ConfidenceChip from "@/components/ConfidenceChip";

export default {
  name: "MetadataCard",
  components:{
    ConfidenceChip
  },
  props: {
    metadata: null,
  },
  data: () => ({
    tab: null,
    tabItems: [],
    rating: 3,
    confidence: 40
  }),
  methods:{
    generateTabs(rawMetadata) {
      for(let item in rawMetadata){
        this.tabItems.push({
          tab: item,
          content: rawMetadata[item]
        })
      }
    }
  },
  created() {
    this.generateTabs(this.metadata)
  }
}
</script>

<style scoped>

</style>