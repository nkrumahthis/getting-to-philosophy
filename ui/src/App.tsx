// import { useState } from 'react'

import './App.css'

const handleClick = () => {
  console.log('clicked')
}

function App() {

  return (
    <div className=''>
      <button onClick={handleClick}>Crawl</button>
    </div>
  )
}

export default App
