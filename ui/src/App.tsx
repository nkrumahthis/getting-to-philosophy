
import './App.css'

const url = 'http://localhost:5002';
interface Hit {
  previous: string,
  current: string
}

const handleCrawl = () => {
  const eventSource = new EventSource(`${url}/stream`);

    eventSource.onmessage = (event) => {
      const newMessage:Hit = JSON.parse(event.data);
      console.log(newMessage);
      // setMessages((prevMessages) => [...prevMessages, newMessage]);
    };

    eventSource.onerror = (error) => {
      console.error('EventSource failed:', error);
      eventSource.close();
    };

}

function App() {

  // const [nodes, setNodes] = useState<Hit[]>([])

  return (
    <div className=''>
      <h1 className="text-xl">
        Getting to Philosophy!
      </h1>
      
      <button onClick={handleCrawl} className='px-4 py-1 border bg-blue-700 text-white rounded-full'>Crawl </button>

    </div>
  )
}

export default App
