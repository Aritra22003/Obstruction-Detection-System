import axios from 'axios'
const API_URL = 'http://localhost:5000/api/predict'

export const getPrediction = async (sensorData) => {
  const res = await axios.post(API_URL, sensorData)
  return res.data
}
