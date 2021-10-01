import Axios from "axios";

export default {
    getTest
}
export const localPath = "http://127.0.0.1:5000/"

function getTest(){
    return Axios.get(localPath + 'test')
}