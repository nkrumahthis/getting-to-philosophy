
import { useState } from 'react';
import './App.css'
import ReactFlow, {Node, Edge} from 'reactflow';
 
import 'reactflow/dist/style.css';
import { updateNodesAndEdges } from './NodesAndEdges';

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
        setHits((prevHits:Hit[]) => { 
          const updatedHits:Hit[] = [...prevHits, newHit]
          const {newNodes, newEdges} = updateNodesAndEdges(updatedHits)
          setNodes(newNodes)
          setEdges(newEdges)
          return updatedHits
        });
      };

      eventSource.onerror = (error) => {
        console.error('EventSource failed:', error);
        eventSource.close();
      };
  }

  const [hits, setHits] = useState<Hit[]>([])
  const [nodes, setNodes] = useState<Node[]>([])
  const [edges, setEdges] = useState<Edge[]>([])


  return (
    <div className=''>
      <h1 className="text-xl">
        Getting to Philosophy!
      </h1>
      
      <button onClick={handleCrawl} className='px-4 py-1 border bg-blue-700 text-white rounded-full'>Crawl </button>

      <div style={{ width: '100vw', height: '100vh' }}>
        <ReactFlow nodes={nodes} edges={edges} />
      </div>

      {hits.map((hit) => (<p key={hit.current}>{JSON.stringify(hit)}</p>))}

    </div>
  )
}

export default App
