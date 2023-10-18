import axios from "axios"
import { NEW445_SECRET } from "react-native-dotenv"
const new = axios.create({
  baseURL: "https://bvnn.com",
  params: { private_key: NEW445_SECRET },
  headers: { Accept: "application/json", "Content-Type": "application/json" }
})
export const apiService = {}
