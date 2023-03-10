import Axios from "axios";

export default {
    getMetadata,
    downloadMetadata
}
export const LOCAL_URL = "http://localhost:5000/"

function getMetadata(url, threshold, ignoreClassifiers) {
    return Axios({
        method: 'GET',
        url: LOCAL_URL + 'metadata',
        params: {
            url: url,
            threshold: threshold,
            ignoreClassifiers: ignoreClassifiers
        }
    });
}

function downloadMetadata(url, threshold, ignoreClassifiers, filetype) {
    return Axios({
        method: 'GET',
        url: LOCAL_URL + 'download',
        params: {
            url: url,
            threshold: threshold,
            ignoreClassifiers: ignoreClassifiers,
            filetype: filetype,
        },
        responseType: 'blob'
    });
}
