import React from 'react'

export default function ResultCard({result}){
  if(result.error) return <div className="mt-4 text-red-600">{result.error}</div>
  const isObstruction = result.prediction && result.prediction.includes('OBSTRUCTION')
  return (
    <div className={`mt-4 p-4 rounded-xl text-center font-semibold text-lg ${isObstruction ? 'bg-red-100 text-red-700' : 'bg-green-100 text-green-700'}`}>
      <div>{result.prediction}</div>
      {result.probability !== null && <div className="text-sm mt-1">probability: {result.probability.toFixed(2)}</div>}
    </div>
  )
}
