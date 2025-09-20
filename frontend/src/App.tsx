import { useState, useEffect } from 'react'

function App() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    // Load ElevenLabs script
    const script = document.createElement('script')
    script.src = 'https://unpkg.com/@elevenlabs/convai-widget-embed'
    script.async = true
    script.type = 'text/javascript'
    document.head.appendChild(script)

    return () => {
      // Cleanup script on unmount
      document.head.removeChild(script)
    }
  }, [])

  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h1>Small Business Hack</h1>
      <p>Welcome to your React TypeScript app!</p>
      <button 
        onClick={() => setCount(count + 1)}
        style={{ 
          padding: '0.5rem 1rem', 
          fontSize: '1rem',
          backgroundColor: '#007bff',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: 'pointer'
        }}
      >
        Count: {count}
      </button>
      
      {/* ElevenLabs Conversation AI Widget */}
      <elevenlabs-convai agent-id="agent_3801k5k9vyj3evntfhx9j8kakjwy"></elevenlabs-convai>
    </div>
  )
}

export default App
