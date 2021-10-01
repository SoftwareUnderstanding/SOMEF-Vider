<template>
<p>{{data}}</p>

</template>

<script>
import somefWebAppService from "@/service/somefWebAppService";
import axios from 'axios';

export default {
  data(){
    return{
          data: null
    }
  },
  methods:{
    getTest(){
      somefWebAppService.getTest()
          .then((response) => {
            this.data = response.data
          })
          .catch(error => {
            console.log(error);
          });
    },
    getTest2(){
      axios.get("http://127.0.0.1:5000/test")
          .then((response) => {
            this.data = response.data
          })
          .catch(error => {
            console.log(error);
          });
    }
  },
  created() {
    this.getTest2()
  }
}
</script>
