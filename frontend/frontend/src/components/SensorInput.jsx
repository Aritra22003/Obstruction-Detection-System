import React, {useState} from 'react'
import { getPrediction } from '../api/detectionAPI'
import ResultCard from './ResultCard'

export default function SensorInput(){
  const [data, setData] = useState({
    distance_cm: 100,
    lidar_intensity: 0.8,
    camera_confidence: 0.3,
    ir_temp_diff: 0.1,
    sonar_echo: 0.8
  })
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleChange = (e) => {
    setData({...data, [e.target.name]: e.target.value})
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    try{
      const res = await getPrediction({
        distance_cm: parseFloat(data.distance_cm),
        lidar_intensity: parseFloat(data.lidar_intensity),
        camera_confidence: parseFloat(data.camera_confidence),
        ir_temp_diff: parseFloat(data.ir_temp_diff),
        sonar_echo: parseFloat(data.sonar_echo)
      })
      setResult(res)
    }catch(err){
      setResult({error: err.message || 'Request failed'})
    }finally{
      setLoading(false)
    }
  }

  return (
    <div className="p-6 bg-white rounded-2xl shadow-md max-w-md w-full">
      <h2 className="text-xl font-semibold mb-4 text-gray-700">Sensor Input</h2>
      <form onSubmit={handleSubmit} className="space-y-3">
        {Object.keys(data).map((key)=> (
          <input key={key} name={key} value={data[key]} onChange={handleChange} className="w-full border p-2 rounded-md" type="number" step="any" />
        ))}
        <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700" disabled={loading}>
          {loading? 'Predicting...':'Predict'}
        </button>
      </form>
      {result && <ResultCard result={result} />}
    </div>
  )
}
