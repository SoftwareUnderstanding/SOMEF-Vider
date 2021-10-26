<template>
  <v-container>
    <v-card flat>
      <v-card-title class="text-center justify-center">
        Software Metadata Extraction
      </v-card-title>
      <v-form ref="form">
        <v-row justify="space-between">

          <v-col align-self="center">
            <v-text-field
                placeholder="example: https://github.com/KnowledgeCaptureAndDiscovery/somef/"
                :outlined="true"
                v-model="url"
                :rules="urlRules"
                required
                label="GitHub URL"
            >
            </v-text-field>
          </v-col>

          <v-col cols="2" align-self="center" md="auto">
            <v-text-field
                placeholder="Threshold"
                required
                v-model="threshold"
                :disabled="true"
                type='number'
                :outlined="true"
                label="Threshold"
            >
            </v-text-field>
          </v-col>

          <v-col cols="2" md="auto">
            <v-btn
                color="primary"
                @click="clickSubmit"
                :loading="loading"
            >
              SUBMIT
            </v-btn>
          </v-col>

        </v-row>
      </v-form>
    </v-card>
    <metadata-card v-if="showMetadataCard"
                   :metadata="testMetadata"
    >
    </metadata-card>

    <!-- Button to top -->
    <v-btn
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

  </v-container>
</template>

<script>
import MetadataCard from "@/components/MetadataCard";
import axiosService from "@/service/axiosService";

export default {
  name: 'Home',
  components: {
    MetadataCard,
  },

  data: () => ({
    testMetadata: {"long_title": {"excerpt": "Software Metadata Extraction Framework (SOMEF)", "confidence": [1.0], "technique": "Regular expression"}, "citation": [{"excerpt": "```\n@INPROCEEDINGS{9006447, \nauthor={A. {Mao} and D. {Garijo} and S. {Fakhraei}}, \nbooktitle={2019 IEEE International Conference on Big Data (Big Data)}, \ntitle={SoMEF: A Framework for Capturing Scientific Software Metadata from its Documentation}, \nyear={2019},\ndoi={10.1109/BigData47090.2019.9006447}, \nurl={http://dgarijo.com/papers/SoMEF.pdf},\npages={3032-3037}\n} \n```\n\n", "confidence": [1], "technique": "Header extraction"}, {"excerpt": "@INPROCEEDINGS{9006447, \nauthor={A. {Mao} and D. {Garijo} and S. {Fakhraei}}, \nbooktitle={2019 IEEE International Conference on Big Data (Big Data)}, \ntitle={SoMEF: A Framework for Capturing Scientific Software Metadata from its Documentation}, \nyear={2019},\ndoi={10.1109/BigData47090.2019.9006447}, \nurl={http://dgarijo.com/papers/SoMEF.pdf},\npages={3032-3037}\n}", "confidence": [1.0], "technique": "Regular expression"}], "identifier": [{"excerpt": "https://zenodo.org/badge/latestdoi/190487675", "confidence": [1.0], "technique": "Regular expression"}], "executable_example": [{"excerpt": "https://mybinder.org/v2/gh/KnowledgeCaptureAndDiscovery/somef/HEAD?filepath=notebook%2FSOMEF%20Usage%20Example.ipynb", "confidence": [1.0], "technique": "Regular expression"}], "documentation": [{"excerpt": "See full documentation at [https://somef.readthedocs.io/en/latest/](https://somef.readthedocs.io/en/latest/)\n\n", "confidence": [1], "technique": "Header extraction"}, {"excerpt": "https://somef.readthedocs.io/", "confidence": [1.0], "technique": "Regular expression"}], "installation": [{"excerpt": "To run SOMEF, please follow the next steps:\n\nClone this GitHub repository\n\n```\ngit clone https://github.com/KnowledgeCaptureAndDiscovery/somef.git\n```\n\nInstall somef (you should be in the folder that you just cloned). Note that for Python 3.7 and 3.8 the module Cython should be installed in advanced (through the command: `pip install Cython`). \n\n```\ncd somef\npip install -e .\n```\n\nTest SOMEF installation\n\n```bash\nsomef --help\n```\n\nIf everything goes fine, you should see:\n\n```bash\nUsage: somef [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  -h, --help  Show this message and exit.\n\nCommands:\n  configure  Configure credentials\n  describe   Running the Command Line Interface\n  version    Show somef version.\n```\n\n", "confidence": [1], "technique": "Header extraction"}, {"excerpt": "We provide a Docker image with SOMEF already installed. To run through Docker, you may build the Dockerfile provided in the repository by running:\n\n```bash\ndocker build -t somef .\n```\nOr just use the Docker image already built in [DockerHub](https://hub.docker.com/r/kcapd/somef):\n\n```bash\ndocker pull kcapd/somef\n```\n\nThen, to run your image just type:\n\n```bash\ndocker run -it kcapd/somef /bin/bash\n```\n\nAnd you will be ready to use SOMEF (see section below). If you want to have access to the results we recommend [mounting a volume](https://docs.docker.com/storage/volumes/). For example, the following command will mount the current directory as the `out` folder in the Docker image:\n\n```bash \ndocker run -it --rm -v $PWD/:/out kcapd/somef /bin/bash\n```\nIf you move any files produced by somef into `/out`, then you will be able to see them in your current directory.\n\n\n", "confidence": [1], "technique": "Header extraction"}], "requirement": [{"excerpt": "- Python 3.9\n\n", "confidence": [1], "technique": "Header extraction"}], "run": [{"excerpt": "```bash\n$ somef describe --help\n  SOMEF Command Line Interface\nUsage: somef describe [OPTIONS]\n\n  Running the Command Line Interface\n\nOptions:\n  -t, --threshold FLOAT           Threshold to classify the text  [required]\n  Input: [mutually_exclusive, required]\n    -r, --repo_url URL            Github Repository URL\n    -d, --doc_src PATH            Path to the README file source\n    -i, --in_file PATH            A file of newline separated links to GitHub\n                                  repositories\n\n  Output: [required_any]\n    -o, --output PATH             Path to the output file. If supplied, the\n                                  output will be in JSON\n\n    -c, --codemeta_out PATH       Path to an output codemeta file\n    -g, --graph_out PATH          Path to the output Knowledge Graph export\n                                  file. If supplied, the output will be a\n                                  Knowledge Graph, in the format given in the\n                                  --format option chosen (turtle, json-ld)\n\n  -f, --graph_format [turtle|json-ld]\n                                  If the --graph_out option is given, this is\n                                  the format that the graph will be stored in\n\n  -p, --pretty                    Pretty print the JSON output file so that it\n                                  is easy to compare to another JSON output\n                                  file.\n\n  -m, --missing                   JSON report with the missing metadata fields\n                                  SOMEF was not able to find. The report will\n                                  be placed in  $PATH_missing.json, where\n                                  $PATH is -o, -c or -g.\n\n  -h, --help                      Show this message and exit.\n```\n\n", "confidence": [1], "technique": "Header extraction"}], "usage": [{"excerpt": "The following command extracts all metadata available from [https://github.com/dgarijo/Widoco/](https://github.com/dgarijo/Widoco/). \n\n```bash\nsomef describe -r https://github.com/dgarijo/Widoco/ -o test.json -t 0.8\n```\n\nTry SOMEF in Binder with our sample notebook: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/KnowledgeCaptureAndDiscovery/somef/HEAD?filepath=notebook%2FSOMEF%20Usage%20Example.ipynb)\n\n", "confidence": [1], "technique": "Header extraction"}], "codeRepository": {"excerpt": "https://github.com/KnowledgeCaptureAndDiscovery/somef", "confidence": [1.0], "technique": "GitHub API"}, "owner": {"excerpt": "KnowledgeCaptureAndDiscovery", "confidence": [1.0], "technique": "GitHub API"}, "ownerType": {"excerpt": "Organization", "confidence": [1.0], "technique": "GitHub API"}, "dateCreated": {"excerpt": "2019-06-06T00:30:12Z", "confidence": [1.0], "technique": "GitHub API"}, "dateModified": {"excerpt": "2021-10-25T08:49:41Z", "confidence": [1.0], "technique": "GitHub API"}, "license": {"excerpt": {"name": "MIT License", "url": "https://api.github.com/licenses/mit"}, "confidence": [1.0], "technique": "GitHub API"}, "description": [{"excerpt": "SOftware Metadata Extraction Framework: A tool for automatically extracting relevant software information from readme files", "confidence": [1.0], "technique": "GitHub API"}], "name": {"excerpt": "somef", "confidence": [1.0], "technique": "GitHub API"}, "fullName": {"excerpt": "KnowledgeCaptureAndDiscovery/somef", "confidence": [1.0], "technique": "GitHub API"}, "issueTracker": {"excerpt": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/issues{/number}", "confidence": [1.0], "technique": "GitHub API"}, "forks_url": {"excerpt": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/forks", "confidence": [1.0], "technique": "GitHub API"}, "stargazers_count": {"excerpt": {"count": 12, "date": "Tue, 26 Oct 2021 19:00:33 GMT"}, "confidence": [1.0], "technique": "GitHub API"}, "forks_count": {"excerpt": {"count": 13, "date": "Tue, 26 Oct 2021 19:00:33 GMT"}, "confidence": [1.0], "technique": "GitHub API"}, "downloadUrl": {"excerpt": "https://github.com/KnowledgeCaptureAndDiscovery/somef/releases", "confidence": [1.0], "technique": "GitHub API"}, "languages": {"excerpt": ["Jupyter Notebook", "Python", "Dockerfile"], "confidence": [1.0], "technique": "GitHub API"}, "readme_url": {"excerpt": "https://github.com/KnowledgeCaptureAndDiscovery/somef/blob/master/README.md", "confidence": [1.0], "technique": "GitHub API"}, "license_file": {"excerpt": "https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/LICENSE", "confidence": [1.0], "technique": "File Exploration"}, "hasExecutableNotebook": {"excerpt": ["https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/notebook/SOMEF%20Usage%20Example.ipynb", "https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/Classifier%20Pipelines.ipynb", "https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/TFidf-NB.ipynb", "https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/TFidf-Logistic.ipynb", "https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/initial_baseline.ipynb", "https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/header_analysis/Wordnet.ipynb"], "confidence": [1.0], "technique": "File Exploration"}, "hasBuildFile": {"excerpt": ["https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/Dockerfile"], "confidence": [1.0], "technique": "File Exploration"}, "hasDocumentation": {"excerpt": ["https://github.com/KnowledgeCaptureAndDiscovery/somef/tree/master/docs"], "confidence": [1.0], "technique": "File Exploration"}, "releases": {"excerpt": [{"tag_name": "0.5.1", "name": "SOMEF 0.5.1: Codemeta export bug fixes", "author_name": "dgarijo", "authorType": "User", "body": "This release addresses small bug fixes for making the codemeta export more robust. For example, when a repository does not have a code release, now the program will not fail.", "tarball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/tarball/0.5.1", "zipball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/zipball/0.5.1", "html_url": "https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.5.1", "url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/releases/40786403", "dateCreated": "2021-03-31T21:17:39Z", "datePublished": "2021-03-31T21:24:41Z"}, {"tag_name": "0.5.0", "name": "SOMEF 0.5.0", "author_name": "dgarijo", "authorType": "User", "body": "This release addresses the following issues:\r\n- Automated evaluation reports for header analysis, so we can compare improvements without having to re-annotate corpus.\r\n- Fixed errors in annotation of fields being GitHub API (they were a custom file exploration)\r\n- Now we export a new category: Acknowledgements\r\n- Fixed errors on empty exported metadata fields. \r\n- Disambiguated category `Issues`\r\n- See https://github.com/KnowledgeCaptureAndDiscovery/somef/milestone/3?closed=1 for more details.", "tarball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/tarball/0.5.0", "zipball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/zipball/0.5.0", "html_url": "https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.5.0", "url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/releases/39608249", "dateCreated": "2021-03-10T17:47:06Z", "datePublished": "2021-03-10T17:51:34Z"}, {"tag_name": "0.4.0", "name": "SOMEF 0.4.0", "author_name": "dgarijo", "authorType": "User", "body": "This release improves on the following aspects of SOMEF:\r\n- Notebooks and Dockerfiles are recognized.\r\n- Docs folders are extracted.\r\n- License is discovered through file inspection.\r\n- New Codemeta specific export\r\n- Fixed the `technique` in the JSON output to accommodate the new types of techniques supported\r\n- MyBinder links extraction\r\n- Zenodo DOIs extraction\r\n- Tests\r\n- Attempt at extracting a long title of a repo ", "tarball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/tarball/0.4.0", "zipball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/zipball/0.4.0", "html_url": "https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.4.0", "url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/releases/39133343", "dateCreated": "2021-03-02T17:40:16Z", "datePublished": "2021-03-02T17:44:55Z"}, {"tag_name": "v0.3.0", "name": "SOMEF 0.3.0: Code reorganization and bug fixes", "author_name": "dgarijo", "authorType": "User", "body": "This version of SOMEF includes full documentation and provides the following features:\r\n- Cleanup and reorganization of repository contents.\r\n- Synchronized package with GitHub releases\r\n- Prepared package release.\r\n- Bug fixes and code refactoring\r\n- Export in JSON-LD and Turtle", "tarball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/tarball/v0.3.0", "zipball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/zipball/v0.3.0", "html_url": "https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/v0.3.0", "url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/releases/27769149", "dateCreated": "2020-06-22T02:04:07Z", "datePublished": "2020-06-22T02:06:55Z"}, {"tag_name": "0.2.0", "name": "SoMEF 0.2.0: Updates in CLI", "author_name": "dgarijo", "authorType": "User", "body": "This version of the system is more robust and includes:\r\n * Answer in JSON format\r\n * Configuration allowing to make authentication optional\r\n * Initial integration of the header analysis.\r\n \r\n", "tarball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/tarball/0.2.0", "zipball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/zipball/0.2.0", "html_url": "https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.2.0", "url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/releases/24726720", "dateCreated": "2020-03-04T06:06:21Z", "datePublished": "2020-03-20T21:56:02Z"}, {"tag_name": "0.1.0", "name": "SoMEF 0.1.0: First release of the CLI", "author_name": "dgarijo", "authorType": "User", "body": "This version of SM2KG incorporates the following features:\r\n * Ranking of classifiers (ordered by accuracy) with the best pipelines to be used by SM2KG.\r\n * First version of the CLI for using the classifiers, creating a JSON result file\r\n * First analysis on detecting commonly used words for the different sections.", "tarball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/tarball/0.1.0", "zipball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/zipball/0.1.0", "html_url": "https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.1.0", "url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/releases/23892997", "dateCreated": "2020-02-21T22:28:36Z", "datePublished": "2020-02-21T22:36:51Z"}, {"tag_name": "0.0.1", "name": "SoMEF 0.0.1: First release of the framework", "author_name": "dgarijo", "authorType": "User", "body": "SoMEF is a software metadata extraction framework designed to automatically distinguish the description, installation instructions, invocation and citation of scientific software metadata from a README file", "tarball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/tarball/0.0.1", "zipball_url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/zipball/0.0.1", "html_url": "https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.0.1", "url": "https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/releases/20570778", "dateCreated": "2019-07-26T22:46:42Z", "datePublished": "2019-10-09T08:17:48Z"}], "confidence": [1.0], "technique": "GitHub API"}},
    metadata: {},
    loading: false,
    showMetadataCard: false,
    url: null,
    threshold: 0.8,
    ignoreClassifiers: true,
    urlRules: [
        v => !!v || 'GitHub URL is required',
        //v => /^(https?:\\)?([\da-z.-]+)\.([a-z.]{2,6})([\\w .-]*)*\?$/.test(v) || 'Must be valid url',
      ],
  }),
  methods:{
    fetchMetadata(url, threshold, ignoreClassifiers) {
      axiosService.getMetadata(url, threshold, ignoreClassifiers)
          .then(response => {
            console.log(response.data)
            this.metadata = response.data
            this.loading = false
            this.showMetadataCard = true
          })
          .catch(error => {
            console.log(error)
          })
    },
    clickSubmit(){
      // TODO: uncomment to use service
      // if (!this.$refs.form.validate()) return
      //
      // this.loading = true
      // this.showMetadataCard = false
      // this.fetchMetadata(this.url, this.threshold, this.ignoreClassifiers)

      this.showMetadataCard = true
    }
  }
}
</script>
