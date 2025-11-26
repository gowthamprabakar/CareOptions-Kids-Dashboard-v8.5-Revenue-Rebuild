import { Hono } from 'hono'
import { serveStatic } from 'hono/cloudflare-workers'

const app = new Hono()

// Serve static files (HTML, JSON, etc.)
app.use('/*', serveStatic({ root: './public' }))

// API routes for JSON data (optional, for future API needs)
app.get('/api/kpi-data', (c) => {
  return c.json({ message: 'Use /kpi_map.json to access KPI data directly' })
})

app.get('/api/people-data', (c) => {
  return c.json({ message: 'Use /people_data.json to access people data directly' })
})

export default app
