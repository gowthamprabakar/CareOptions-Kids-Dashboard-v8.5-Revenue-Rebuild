# New York Spine Specialists (NYSS) - Patient Access & Intake Dashboard

## 🏥 Overview

A comprehensive executive intelligence system for **New York Spine Specialists (NYSS)** focusing on Patient Access & Intake operations, featuring **14 strategic KPIs** across 5 macro processes with complete **10-layer decision intelligence** for each metric, including AI-powered root cause analysis, predictive insights, and detailed action plans.

**Built on:** Hono + TypeScript + Cloudflare Pages  
**Organization:** New York Spine Specialists (NYSS)  
**Focus:** Pillar 1 - Patient Access & Intake  

## 🌐 Live Dashboard

**Production URL:** https://3000-i3trzw1s8ci0ydttfvlky-b9b802c4.sandbox.novita.ai/

## 📊 Five Complete Dashboards

### 1. **Executive Intelligence** (D3 Tree Visualization + AI Chatbot)
🔗 Access: `/` or `/index.html`

**Features:**
- Interactive D3.js hierarchical tree with 14 KPI nodes
- **Normal Click:** Expand/collapse nodes to explore tree structure
- **Shift+Click:** Open complete 10-layer intelligence card
- Tree expands horizontally (left to right) with +/- indicators
- AI-powered root cause analysis and predictive forecasts
- Real-time RAG (Red/Amber/Green) status indicators

### 2. **Command Center** (KPI Matrix Table)
🔗 Access: `/command-center.html`

**Features:**
- Complete table view of all 14 KPIs
- Filter by RAG status (Red/Amber/Green/All)
- Search functionality across all metrics
- Sort by any column
- **Click any row for same 10-layer intelligence card** with 3 interactive charts

### 3. **Control Center** (Interactive Simulation)
🔗 Access: `/control-center.html`

**Features:**
- Interactive KPI sliders for simulation
- Real-time updates and baseline comparison
- What-If Scenario Simulation with immediate feedback

### 4. **People Graph** (Organizational Hierarchy)
🔗 Access: `/people-graph.html`

**Features:**
- Complete organizational hierarchy
- KPI ownership mapping
- Interactive person profiles with detailed KPI assignments

### 5. **🤖 Automation Hub** (Agentic AI Workflow Automation)
🔗 Access: `/automation-hub.html`

**Features:**
- 5 high-impact automation workflows
- Real-time workflow execution simulation
- Financial impact and ROI calculations

## 📊 KPI Structure (14 Strategic KPIs)

### **Macro Process 1: Patient Acquisition** (2 KPIs)

#### Category 1.1 — Lead Intake & Conversion
1. **New Patient Lead Volume**
   - Target: 280 patients/month
   - Current: 245 patients/month
   - Status: 🟡 Amber
   - Sub-KPIs: Lead source mix, Conversion by source, Call abandon rate

2. **Referral-to-Appointment Conversion**
   - Target: 85%
   - Current: 78%
   - Status: 🟡 Amber

### **Macro Process 2: Scheduling & Appointment Management** (3 KPIs)

#### Category 2.1 — Access Efficiency
3. **Days to First Appointment**
   - Target: 3.0 days
   - Current: 5.2 days
   - Status: 🔴 Red
   - Sub-KPIs: Slot availability, Provider load, Insurance clearance lag

4. **Appointment Wait Time (In-clinic)**
   - Target: 15 minutes
   - Current: 18 minutes
   - Status: 🟡 Amber

5. **No-Show Rate**
   - Target: 10%
   - Current: 14.5%
   - Status: 🔴 Red

### **Macro Process 3: Intake Documentation & Verification** (5 KPIs)

#### Category 3.1 — Packet Completeness
6. **Packet Completeness Rate**
   - Target: 98%
   - Current: 92%
   - Status: 🟡 Amber
   - Sub-KPIs: Demographics, Insurance card, Claim #, Attorney info, Imaging, Consent forms

7. **Missing Packet Item Rate**
   - Target: 2%
   - Current: 8.5%
   - Status: 🔴 Red

#### Category 3.2 — Insurance Verification
8. **Eligibility Verification Accuracy**
   - Target: 98%
   - Current: 94%
   - Status: 🟡 Amber
   - Critical for: PIP/WC/Commercial insurance clearance

9. **Benefit Verification Turnaround**
   - Target: 1.5 days
   - Current: 2.8 days
   - Status: 🔴 Red

#### Category 3.3 — Financial Clearance
10. **Pre-Visit Financial Clearance Rate**
    - Target: 95%
    - Current: 88%
    - Status: 🟡 Amber

### **Macro Process 4: Clinical Pre-Visit Preparation** (2 KPIs)

#### Category 4.1 — Clinical Records Readiness
11. **Imaging Availability Before Visit**
    - Target: 95%
    - Current: 85%
    - Status: 🟡 Amber
    - Types: MRI, X-ray, Radiologist reports

12. **Referral Notes Availability**
    - Target: 98%
    - Current: 90%
    - Status: 🟡 Amber

### **Macro Process 5: Patient Experience** (2 KPIs)

#### Category 5.1 — Service Quality
13. **New Patient NPS (Net Promoter Score)**
    - Target: 80
    - Current: 72
    - Status: 🟡 Amber

14. **Intake Satisfaction Score**
    - Target: 4.5/5
    - Current: 4.2/5
    - Status: 🟡 Amber

## 🎯 10-Layer Decision Intelligence

Every KPI includes comprehensive intelligence across 10 layers:

1. **Context & Business Impact** - Metric definition, business significance, industry benchmarks
2. **Current State Analysis** - RAG status, current value, performance gap, financial impact
3. **Historical Trends** - Interactive sparkline visualizations (6 months)
4. **Root Cause Analysis** - AI-powered identification with confidence scores
5. **Predictive Insights** - AI forecasts with 3 scenarios (Best/Likely/Worst)
6. **Trend Analysis** - Statistical trend quality assessment
7. **Dependencies** - Upstream/downstream/peer relationships
8. **People & Accountability** - Owners with titles, departments, emails
9. **Recommended Actions** - Detailed action objects with priorities, owners, timelines
10. **Contributing Factors** - Internal/external drivers

## 🚀 Technical Stack

- **Backend:** Hono v4.10+ (TypeScript)
- **Frontend:** HTML5, CSS3, JavaScript ES6+
- **Visualization:** D3.js v7.8.5 (tree graphs), Chart.js v4.4.0 (sparklines)
- **Data Structure:** Hierarchical JSON with flat index
- **Deployment:** Cloudflare Pages + PM2 (development)
- **Build Tool:** Vite 6.3+
- **Runtime:** Cloudflare Workers

## 📁 Project Structure

```
webapp/
├── src/
│   ├── index.tsx               # Main Hono application entry
│   └── renderer.tsx            # TSX renderer
├── public/                     # Static assets
│   ├── index.html              # Executive Intelligence Dashboard
│   ├── command-center.html     # KPI Matrix Table View
│   ├── control-center.html     # Interactive Simulation
│   ├── people-graph.html       # Organizational Hierarchy
│   ├── automation-hub.html     # AI Workflow Automation
│   ├── kpi_map.json            # NYSS KPI data (14 nodes)
│   └── people_data.json        # Organizational data
├── generate_nyss_kpi_data.py   # KPI data generator script
├── dist/                       # Build output directory
├── ecosystem.config.cjs        # PM2 configuration
├── vite.config.ts              # Vite configuration
├── wrangler.jsonc              # Cloudflare Pages configuration
└── README.md                   # This file
```

## 💾 Data Architecture

### **kpi_map.json Structure:**
```json
{
  "version": "1.0-nyss-patient-access-intake",
  "total_nodes": 14,
  "organization": "New York Spine Specialists (NYSS)",
  "pillar": "Patient Access & Intake",
  "intelligence_layers": [
    "Context & Business Impact",
    "Current State Analysis",
    "Historical Trends (6 months)",
    "Root Cause Analysis",
    "Predictive Insights (AI-powered)",
    "Trend Analysis (Statistical)",
    "Dependencies (Upstream/Downstream)",
    "People & Accountability",
    "Recommended Actions (Detailed)",
    "Contributing Factors"
  ],
  "tree": {
    "name": "Patient Access & Intake",
    "id": "nyss_root",
    "level": 0,
    "children": [ /* 5 macro processes */ ]
  },
  "nodes": [ /* Flat array of 14 nodes with full intelligence */ ]
}
```

## 🎨 Visual Features

### **RAG Status Colors:**
- 🔴 **Red**: Critical issues requiring immediate attention (5 KPIs)
- 🟡 **Amber**: Warning status, monitor closely (9 KPIs)
- 🟢 **Green**: On track, meeting targets (0 KPIs - opportunity for improvement!)

### **Interactive Charts & Graphs:**
- **📈 Historical Trend Sparklines** - 6 months performance data with Chart.js
- **📊 Predictive Forecast Chart** - 3-scenario projection (Best/Likely/Worst cases)
- **🔗 Neo4j-Style Dependency Network** - Interactive D3.js force-directed graph

## 🔧 Development

### **Local Development:**
```bash
# Build the project (REQUIRED before first start)
npm run build

# Start development server with PM2
fuser -k 3000/tcp 2>/dev/null || true
pm2 start ecosystem.config.cjs

# Test the service
curl http://localhost:3000/

# Check logs
pm2 logs webapp --nostream

# Restart service
pm2 restart webapp
```

### **Regenerate KPI Data:**
```bash
cd /home/user/webapp
python3 generate_nyss_kpi_data.py
```

### **Available Scripts:**
```json
{
  "dev": "vite",
  "dev:sandbox": "wrangler pages dev dist --ip 0.0.0.0 --port 3000",
  "build": "vite build",
  "preview": "wrangler pages dev dist",
  "deploy": "npm run build && wrangler pages deploy dist",
  "clean-port": "fuser -k 3000/tcp 2>/dev/null || true",
  "test": "curl http://localhost:3000"
}
```

## 📈 Key Metrics Summary

| Macro Process | KPIs | Red | Amber | Green |
|--------------|------|-----|-------|-------|
| Patient Acquisition | 2 | 0 | 2 | 0 |
| Scheduling & Appointment | 3 | 2 | 1 | 0 |
| Intake Documentation | 5 | 2 | 3 | 0 |
| Clinical Pre-Visit | 2 | 0 | 2 | 0 |
| Patient Experience | 2 | 0 | 2 | 0 |
| **Total** | **14** | **4** | **10** | **0** |

## 🎯 Use Cases

1. **Executive Leadership:** High-level patient access performance overview
2. **Operations Teams:** Intake efficiency, scheduling optimization
3. **Front Office:** Lead conversion, appointment management
4. **Clinical Operations:** Documentation readiness, imaging availability
5. **Revenue Cycle:** Insurance verification, financial clearance
6. **Patient Experience:** Service quality monitoring, satisfaction tracking

## 🚨 Critical Areas Requiring Attention

### **🔴 Red Status KPIs (Immediate Action Required):**
1. **Days to First Appointment** - 5.2 days (Target: 3.0 days)
   - Impact: Patient dissatisfaction, competitor loss
   - Action: Implement urgent slot protocol, increase provider capacity

2. **No-Show Rate** - 14.5% (Target: 10%)
   - Impact: Revenue loss, provider underutilization
   - Action: Enhanced reminder system, patient engagement

3. **Missing Packet Item Rate** - 8.5% (Target: 2%)
   - Impact: Verification delays, claim denials
   - Action: Automated checklist, staff training

4. **Benefit Verification Turnaround** - 2.8 days (Target: 1.5 days)
   - Impact: Appointment delays, patient frustration
   - Action: Implement Availity integration, add verification staff

## 🚀 Deployment to Cloudflare Pages

### **Prerequisites:**
1. Cloudflare account
2. Wrangler CLI installed
3. Cloudflare API token configured

### **Deployment Steps:**
```bash
# 1. Build the project
npm run build

# 2. Deploy to Cloudflare Pages
npm run deploy:prod

# 3. Access your production URL
# https://careoptions-kids-dashboard.pages.dev
```

## 📝 Recent Updates

### **Version 1.0 - NYSS Patient Access & Intake** (November 26, 2025)
- ✅ Complete replacement of KPI data with NYSS Patient Access & Intake metrics
- ✅ Generated 14 strategic KPIs across 5 macro processes
- ✅ Full 10-layer decision intelligence for each KPI
- ✅ AI-powered root cause analysis and predictive insights
- ✅ Comprehensive dependency mapping
- ✅ Detailed people accountability with contact information
- ✅ Priority-based recommended actions with timelines and ROI
- ✅ Historical trend data and statistical analysis
- ✅ All dashboards updated with new data structure
- ✅ Python data generator script for easy updates
- ✅ Ready for production deployment

## 🔗 Related Resources

- [D3.js Documentation](https://d3js.org/)
- [Chart.js Documentation](https://www.chartjs.org/)
- [Hono Framework](https://hono.dev/)
- [Cloudflare Pages](https://pages.cloudflare.com/)
- [NYSS Operations Manual](https://nyss.com/)

---

**Version:** 1.0-nyss-patient-access-intake  
**Last Updated:** November 26, 2025  
**Organization:** New York Spine Specialists (NYSS)  
**Status:** ✅ Active - All 5 dashboards operational  
**Dashboards:** Executive Intelligence, Command Center, Control Center, People Graph, Automation Hub  
**Total KPIs:** 14 strategic metrics with complete **10-layer decision intelligence**  
**Tech Stack:** Hono + TypeScript + Cloudflare Pages  
**Deployment:** Production-ready on Cloudflare edge network
