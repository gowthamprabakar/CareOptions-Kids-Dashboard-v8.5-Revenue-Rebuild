# 📊 Complete KPI Data Structure & Card Layout

## ✅ DATA CONFIRMED PRESENT - ALL 213 KPIs

Every KPI in the system has **complete 10-layer intelligence** with all required fields.

---

## 📋 **KPI Data Fields (19 Total)**

Each KPI object contains:

### **Basic Identifiers:**
1. `id` - Unique KPI identifier (e.g., "kpi_1_1_1")
2. `name` - KPI name (e.g., "New Patient Lead Volume")
3. `value` - Current value (string, e.g., "245")
4. `target` - Target value (string, e.g., "280")
5. `unit` - Unit of measurement (e.g., "patients")
6. `rag` - Status indicator (green/amber/red)
7. `trend` - Trend direction (up/down/stable)

### **Categorization:**
8. `pillar` - Which pillar (e.g., "Patient Access & Intake")
9. `macro_process` - Which macro process (e.g., "Patient Acquisition")
10. `category` - Which category (e.g., "Lead Intake & Conversion")

### **10 Layers of Intelligence:**

#### **LAYER 1: Context** (object)
```json
{
  "definition": "What this KPI measures",
  "business_impact": "Why it matters",
  "industry_benchmark": "Industry standard"
}
```

#### **LAYER 2: Current State** (object)
```json
{
  "status": "green/amber/red",
  "value": "245",
  "target": "280",
  "gap": 35,
  "gap_percentage": 12.5,
  "financial_impact": "$89,845 impact per month"
}
```

#### **LAYER 3: Trend Data** (array of 6 numbers)
```json
[83.8, 86.2, 84.7, 88.3, 89.4, 85.3]
```
6 months of historical performance values

#### **LAYER 4: Root Causes** (array of 3 objects)
```json
[
  {
    "cause": "Provider workflow bottlenecks",
    "confidence": 80,
    "impact": "Medium",
    "data_points": 405
  },
  ...
]
```
3 AI-identified root causes with confidence scores

#### **LAYER 5: Predictive Insights** (object)
```json
{
  "pattern": "Deteriorating",
  "confidence": 87,
  "timeframe": "Next 30 days",
  "scenarios": [
    {
      "name": "Best Case Scenario",
      "value": 100,
      "probability": "28%"
    },
    {
      "name": "Most Likely Scenario",
      "value": 100,
      "probability": "54%"
    },
    {
      "name": "Worst Case Scenario",
      "value": 100,
      "probability": "16%"
    }
  ],
  "leading_indicators": ["Market conditions", "Protocol adherence", "Staff availability"]
}
```

#### **LAYER 6: Trend Analysis** (object)
```json
{
  "current_trend": "Up",
  "trend_strength": "Moderate",
  "volatility": "Medium",
  "key_insights": "Shows up trajectory requiring maintenance"
}
```

#### **LAYER 7: Dependencies** (object)
```json
{
  "upstream": ["Upstream KPI 1", "Upstream KPI 2"],
  "downstream": ["Downstream KPI 1", "Downstream KPI 2"],
  "peer_metrics": ["Related KPI 1", "Related KPI 2"]
}
```
Shows which KPIs affect this one (upstream) and which this affects (downstream)

#### **LAYER 8: Accountability** (array)
```json
[
  {
    "name": "David Wilson",
    "title": "Coding Supervisor",
    "department": "Revenue Cycle",
    "email": "david.wilson@example.com",
    "role": "Primary Owner",
    "avatar_color": "#3B82F6"
  }
]
```

#### **LAYER 9: Recommended Actions** (array)
```json
[
  {
    "priority": "Medium",
    "action": "Maintain and optimize current processes",
    "timeline": "2-3 weeks",
    "owner": "Operations Manager",
    "expected_impact": "$75K-$125K monthly improvement",
    "resources": "Process team, 1-2 FTEs",
    "success_metrics": "Target achievement >90%"
  }
]
```

#### **LAYER 10: Contributing Factors** (object)
```json
{
  "internal": [
    "Staff training effectiveness",
    "Process efficiency",
    "Technology adoption"
  ],
  "external": [
    "Market demand fluctuations",
    "Regulatory changes",
    "Competitive landscape"
  ]
}
```

---

## 🎨 **KPI Card Display Layout**

When a KPI card opens, it should show:

### **Header Section:**
- KPI Name (large)
- Current Value with unit (e.g., "245 patients")
- Target value (e.g., "Target: 280")
- RAG Status badge (🔴 Red / 🟡 Amber / 🟢 Green)
- Category label

### **Body Section (Scrollable):**

1. **Context & Business Impact**
   - Definition
   - Business Impact
   - Industry Benchmark

2. **Current State Analysis**
   - Status
   - Gap from target
   - Gap percentage
   - Financial impact (highlighted box)

3. **Historical Trend** (Chart)
   - 6-month sparkline visualization
   - Trend direction indicator

4. **Root Cause Analysis**
   - 3 causes with colored impact indicators
   - Confidence scores
   - Data points used

5. **Predictive Insights**
   - Pattern description
   - Confidence level
   - 3 forecast scenarios with probabilities
   - Leading indicators list

6. **Trend Analysis**
   - Current trend
   - Trend strength
   - Volatility
   - Key insights

7. **Dependency Graph** (Visual)
   - Neo4j-style network diagram
   - Upstream KPIs → This KPI → Downstream KPIs

8. **Accountability & Ownership**
   - Owner name, title, department
   - Email for contact
   - Role description

9. **Recommended Actions**
   - Priority level
   - Action description
   - Timeline
   - Expected impact
   - Required resources

10. **Contributing Factors**
    - Internal factors (3)
    - External factors (3)

---

## ✅ **Data Verification Summary**

| Field | Status | Data Type |
|-------|--------|-----------|
| Basic Info (7 fields) | ✅ Present | strings/numbers |
| Context | ✅ Present | object with 3 keys |
| Current State | ✅ Present | object with 6 keys |
| Trend Data | ✅ Present | array of 6 numbers |
| Root Causes | ✅ Present | array of 3 objects |
| Predictive Insights | ✅ Present | object with scenarios array ✅ FIXED |
| Trend Analysis | ✅ Present | object with 4 keys |
| Dependencies | ✅ Present | object with 3 arrays |
| People Accountable | ✅ Present | array of 1 object |
| Recommended Actions | ✅ Present | array of 1 object |
| Contributing Factors | ✅ Present | object with 2 arrays |

---

## 🎯 **Key Fixes Applied**

1. ✅ **scenarios array** - Fixed from object to array (was causing .map() error)
2. ✅ **Tree structure** - 5 Pillars → 27 Macros → 52 Categories → 213 KPIs
3. ✅ **String values** - value and target are strings for .replace() compatibility
4. ✅ **Complete data** - All 10 layers present for all 213 KPIs

---

## 🔍 **How to Verify Card Opens**

1. Open Console (F12)
2. Navigate tree to Level 4 (KPI node)
3. Click KPI node
4. Look for these console messages:
   ```
   🖱️ NODE CLICKED: New Patient Lead Volume
   📊 Level: 4
   🏷️ Type: kpi
   ✅ This IS a KPI node (level 4)! Opening card...
   ✅ Found KPI data in nodes array
   ✅ Calling showInfoPanel...
   ```
5. Panel should slide in from right with all 10 layers displayed

---

## 📦 **Data Location**

- **Tree Structure:** `kpi_map.json` → `tree` object
- **Flat KPI Data:** `kpi_map.json` → `nodes` array (213 KPIs)
- **Each KPI:** Has all 19 fields listed above
- **Panel Display:** Uses `showInfoPanel(kpi)` function in `index.html`
