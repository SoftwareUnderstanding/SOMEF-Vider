<template>
  <v-container>

    <div class="about-section">
      <div class="jumbotron">
        <h1 class = "display-4">SOMEF Vider</h1>
        <hr class = "my-4">
        <p>
          With an increase of complex scientific software, researchers need to spend a large portion of their time
          searching for available software documentation and source code, and reading it to understand the software used
          and the proper way to cite it.
        </p>
        <p>
          Somef Vider is a web application that retrieves the metadata of the given GitHub repository through the
          Software Metadata Extraction Framework (SOMEF) and shows it in a user-friendly way.
        </p>
        <p>
          To use this tool the user must provide a valid GitHub URL and click the submit button, wait for the server response,
          and a table with all the metadata extracted will appear below the form.
          The most relevant metadata will show at the header of the table, such as title, license, las update, etc. For the rest
          of the fields, each one will be enclosed in a drop down card with the extraction method used and the confidence of the value.
        </p>
        <p>
          Source code is available at this <a href="https://github.com/SoftwareUnderstanding/SOMEF-Vider">GitHub repository</a>
        </p>
      </div>
    </div>

    <h2 class="center">Developers</h2>

    <div class="row">
      <div class="col-sm-4">
        <div class = card>
          <div class="card-body">
            <h5 class="card-title h5">Victor Fernandez-Lancha Aranda</h5>
            <p class="card-text">v.faranda@alumnos.upm.es</p>
          </div>
        </div>
      </div>
    </div>

    <h2 class="center">Mentor</h2>

    <div class="row">
      <div class="col-sm-4">
        <div class = card>
          <div class="card-body">
            <h5 class="card-title h5">Daniel Garijo</h5>
            <p class="card-text" >daniel.garijo@upm.es</p>
          </div>
        </div>
      </div>
    </div>
  </v-container>

</template>

<script>
export default {
  name: "About"
}
</script>

<style scoped>

</style>