import axios from 'axios';

const config = {
    baseURL:`${process.env.REACT_APP_SERVER_URL}`,
    headers: {
		Accept: 'application/json',
    }
}
const axiosInstance = axios.create(config);
export default axiosInstance;