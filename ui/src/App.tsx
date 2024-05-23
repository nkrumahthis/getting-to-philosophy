
import './App.css'
import ReactFlow, {
  Node, 
  Edge, 
  addEdge, 
  useNodesState, 
  useEdgesState,
  MiniMap,
  Controls,
  Background,
  BackgroundVariant
} from 'reactflow';
 
import 'reactflow/dist/style.css';
import { createEdge, createNode, Hit } from './NodesAndEdges';

const url = 'http://localhost:5002';

function App() {

  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  const handleCrawl = () => {

    const eventSource = new EventSource(`${url}/stream`);

    const nodeMap = new Map<string, Node>();

    eventSource.onmessage = (event) => {
      const newHit:Hit = JSON.parse(event.data);

      let previousNode = nodeMap.get(newHit.previous)

      if(!previousNode) previousNode = nodeMap.get("/wiki/Special:Random")

      const newNode:Node = createNode(newHit, previousNode)
      nodeMap.set(newHit.current, newNode)
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
      <div className='absolute z-50'>
        <h1 className="text-xl">
          Getting to Philosophy!
        </h1>
        
        <button onClick={handleCrawl} className='px-4 py-1 border bg-blue-700 text-white rounded-full'>
          Crawl 
        </button>
      </div>

      <div style={{ width: '90vw', height: '90vh' }}>
        <ReactFlow 
          nodes={nodes} 
          edges={edges} 
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
        >
          <Controls />
          <MiniMap />
          <Background variant={BackgroundVariant.Dots} gap={12} size={1} />
        </ReactFlow>
      </div>

    </div>
  )
}

export default App
