import { Hono } from 'hono'

const app = new Hono()

// API route for health check
app.get('/api/health', (c) => {
  return c.json({ 
    status: 'healthy',
    version: '8.5.0',
    service: 'CareOptions for Kids - RCM Dashboard'
  })
})

export default app
