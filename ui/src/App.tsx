
import { useState } from 'react';
import './App.css'
import ReactFlow from 'reactflow';
 
import 'reactflow/dist/style.css';
 
const initialNodes = [
  { id: '1', position: { x: 0, y: 0 }, data: { label: '1' } },
  { id: '2', position: { x: 0, y: 100 }, data: { label: '2' } },
];

const initialEdges = [{ id: 'e1-2', source: '1', target: '2' }];


const url = 'http://localhost:5002';
interface Hit {
  previous: string,
  current: string
}

function App() {

  const handleCrawl = () => {
    const eventSource = new EventSource(`${url}/stream`);

      eventSource.onmessage = (event) => {
        const newHit:Hit = JSON.parse(event.data);
        setHits((prevHits) => [...prevHits, newHit]);
      };

      eventSource.onerror = (error) => {
        console.error('EventSource failed:', error);
        eventSource.close();
      };
  }

  const [hits, setHits] = useState<Hit[]>([])

  return (
    <div className=''>
      <h1 className="text-xl">
        Getting to Philosophy!
      </h1>
      
      <button onClick={handleCrawl} className='px-4 py-1 border bg-blue-700 text-white rounded-full'>Crawl </button>

      {hits.map((hit) => (<p key={hit.current}>{JSON.stringify(hit)}</p>))}

      <div style={{ width: '100vw', height: '100vh' }}>
        <ReactFlow nodes={initialNodes} edges={initialEdges} />
      </div>
    </div>
  )
}

export default App
