
import './App.css'
import ReactFlow, {Node, Edge, addEdge, useNodesState, useEdgesState} from 'reactflow';
 
import 'reactflow/dist/style.css';
import { createEdge, createNode } from './NodesAndEdges';

const url = 'http://localhost:5002';
interface Hit {
  previous: string,
  current: string
}

function App() {

  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  const handleCrawl = () => {

    const eventSource = new EventSource(`${url}/stream`);

      eventSource.onmessage = (event) => {
        const newHit:Hit = JSON.parse(event.data);

        const newNode:Node = createNode(newHit)
        const newEdge:Edge = createEdge(newHit)

        // Add the new node and edge incrementally to the existing ones
        setNodes((nds) => nds.some(node => node.id === newNode.id) ? nds : [...nds, newNode]);
        setEdges((eds) => eds.some(edge => edge.id === newEdge.id) ? eds : addEdge(newEdge, eds));
          
      };

      eventSource.onerror = (error) => {
        console.error('EventSource failed:', error);
        eventSource.close();
      };
  }

  return (
    <div className=''>
      <h1 className="text-xl">
        Getting to Philosophy!
      </h1>
      
      <button onClick={handleCrawl} className='px-4 py-1 border bg-blue-700 text-white rounded-full'>Crawl </button>

      <div style={{ width: '100vw', height: '100vh' }}>
        <ReactFlow 
          nodes={nodes} 
          edges={edges} 
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
        />
      </div>

    </div>
  )
}

export default App
