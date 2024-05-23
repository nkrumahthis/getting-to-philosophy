import {Edge, Node} from 'reactflow';

export interface Hit {
    previous: string,
    current: string
}

export function updateNodesAndEdges(hits: Hit[]) : {newNodes: Node[], newEdges: Edge[]} {

    const newNodes: Node[] = []
    const newEdges: Edge[] = []

    const nodesMap = new Map<string, Node>();

    hits.forEach(hit => {
        
        if(!nodesMap.has(hit.previous)) {
            const node: Node = {
                id: hit.previous, 
                position: { 
                    x: Math.random() * 800, 
                    y: Math.random() * 800
                }, 
                data: { label: hit.previous }
            }
            nodesMap.set(hit.previous, node)
            newNodes.push(node)
        }

        if(!nodesMap.has(hit.current)) {
            const previousNode = nodesMap.get(hit.previous)

            const randomOffset =  (Math.random() * 100) + 100
            const randomBoolean = Math.random() < 0.5
            const newX = previousNode ? 
                previousNode.position.x + (randomBoolean ? randomOffset : -randomOffset) : Math.random() * 800
            const newY = previousNode ? 
                previousNode.position.y + randomOffset : Math.random() * 800
            
            const node: Node = {
                id: hit.current, 
                position: { x: newX, y: newY },
                data: { label: hit.current }
            }

            nodesMap.set(hit.current, node)
            newNodes.push(node)
        }

        const edge: Edge = {
            id: `e${hit.previous}-${hit.current}`,
            source: hit.previous,
            target: hit.current
        }

        newEdges.push(edge)
    })

    return {
        newNodes,
        newEdges
    }


}

export function createNode(hit: Hit, previousNode?: Node): Node{

    const randomOffset =  (Math.random() * 100) + 50
    const randomBoolean = Math.random() < 0.5
    const newX = previousNode ? 
        previousNode.position.x + (randomBoolean ? randomOffset : -randomOffset) : Math.random() * 800
    const newY = previousNode ? 
        previousNode.position.y + randomOffset : Math.random() * 800

    const node: Node = {
        id: hit.previous, 
        position: { 
            x: newX,
            y: newY
        }, 
        data: { label: hit.previous }
    }
    return node
}

export function createEdge(hit: Hit): Edge{
    const edge: Edge = {
        id: `e${hit.previous}-${hit.current}`,
        source: hit.previous,
        target: hit.current
    }

    return edge
}