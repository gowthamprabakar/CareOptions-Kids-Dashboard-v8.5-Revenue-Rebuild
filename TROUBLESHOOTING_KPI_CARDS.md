# Troubleshooting: KPI Cards Not Opening

## ✅ Root Cause Analysis (RESOLVED)

### Issues Fixed:
1. **❌ `scenarios.map is not a function`** - FIXED ✅
   - Problem: `predictive_insights.scenarios` was an object, not an array
   - Fix: Changed data generator to output scenarios as an array
   - File: `generate_complete_nyss_kpis.py`

2. **❌ `key_insights.map is not a function`** - FIXED ✅
   - Problem: `trend_analysis.key_insights` is a string, not an array
   - Fix: Changed HTML to display string instead of using `.map()`
   - Files: `index.html`, `command-center.html`

3. **❌ Tree Structure Broken** - FIXED ✅
   - Problem: Tree showed 27 nodes at Level 1 instead of 5 Pillars
   - Fix: Ran `fix_pillar_structure.py` to rebuild correct hierarchy
   - Structure: Root (L0) → 5 Pillars (L1) → 27 Macros (L2) → 52 Categories (L3) → 213 KPIs (L4)

## 📋 How KPI Cards Work

### Data Structure:
```
kpi_map.json
├── tree: Hierarchical structure with level/type info
│   ├── Root (level 0, type: root)
│   └── Pillars (level 1, type: pillar)
│       └── Macros (level 2, type: macro)
│           └── Categories (level 3, type: category)
│               └── KPIs (level 4, type: kpi) ← THESE ARE CLICKABLE
└── nodes: Flat array with full KPI data (context, root_causes, etc.)
```

### Click Detection Logic:
1. User clicks a node in the tree
2. JavaScript checks: `if (d.data.level === 4 && d.data.type === 'kpi')`
3. If TRUE: Look up full KPI data: `kpiData.nodes.find(node => node.id === d.data.id)`
4. Call: `showInfoPanel(fullKpiData)` to display the 10-layer intelligence card

### Why Non-KPI Nodes Don't Open Cards:
- **Pillars** (Level 1): Used for organization, contain no KPI data
- **Macro Processes** (Level 2): Group related KPIs, no detail cards
- **Categories** (Level 3): Sub-groups of KPIs, no detail cards
- **KPIs** (Level 4): ✅ **ONLY THESE OPEN DETAIL CARDS**

## 🔍 How to Open KPI Cards

### Executive Intelligence (Tree Graph):
URL: `https://3000-i3trzw1s8ci0ydttfvlky-b9b802c4.sandbox.novita.ai/`

**Step-by-Step:**
1. **Hard Refresh**: Press `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
2. **Open Console**: Press `F12` and go to Console tab
3. **Navigate to KPI**:
   - Click `Patient Access & Intake` (Pillar - Level 1)
   - Click `Patient Acquisition` (Macro - Level 2)
   - Click `Lead Intake & Conversion` (Category - Level 3)
   - Now you should see blue KPI nodes (Level 4):
     - `New Patient Lead Volume`
     - `Lead-to-Appointment Conversion Rate`
     - `Lead Response Time`
     - etc.
4. **Click ANY blue KPI node** (Level 4)
5. **Panel slides in** from the right showing 10 layers of intelligence

**Console Output (Success):**
```
🖱️ NODE CLICKED: New Patient Lead Volume
📊 Level: 4
🏷️ Type: kpi
🔑 ID: kpi_1_1_1
✅ This IS a KPI node (level 4)! Opening card...
✅ Found KPI data in nodes array
✅ Calling showInfoPanel...
```

### Command Center (Table View):
URL: `https://3000-i3trzw1s8ci0ydttfvlky-b9b802c4.sandbox.novita.ai/command-center`

**Step-by-Step:**
1. **Hard Refresh**: Press `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
2. **Open Console**: Press `F12` and go to Console tab
3. **Click the Red Test Button** (top of page) - Should show "✅ showDetailPanel called!"
4. **Click ANY row in the table** - Detail panel slides in from right
5. **Alternative**: Click the `👁️` icon in the Actions column

**Console Output (Success):**
```
🖱️ Row clicked for KPI: New Patient Lead Volume
```

## 🐛 Common Mistakes

### ❌ Clicking Wrong Level Nodes:
```
USER CLICKS: "Patient Access & Intake" (Level 1 - Pillar)
RESULT: ❌ No card opens (not a KPI node)

USER CLICKS: "Patient Acquisition" (Level 2 - Macro)
RESULT: ❌ No card opens (not a KPI node)

USER CLICKS: "Lead Intake & Conversion" (Level 3 - Category)
RESULT: ❌ No card opens (not a KPI node)

USER CLICKS: "New Patient Lead Volume" (Level 4 - KPI)
RESULT: ✅ KPI card opens! 🎉
```

### ❌ Not Hard Refreshing:
- Browser may cache old JavaScript with bugs
- Always hard refresh: `Ctrl+Shift+R` or `Cmd+Shift+R`

### ❌ Clicking Collapsed Nodes:
- If KPI nodes aren't visible, you need to expand the Category first
- The tree initially shows down to Level 2 (Macros)
- Click Categories (Level 3) to reveal KPIs (Level 4)

## ✅ Verification Checklist

### Before Reporting Issues:
- [ ] Hard refreshed browser (Ctrl+Shift+R / Cmd+Shift+R)
- [ ] Opened browser console (F12 → Console tab)
- [ ] Navigated to Level 4 KPI nodes (blue nodes on far right)
- [ ] Clicked a Level 4 KPI node (not Pillar/Macro/Category)
- [ ] Checked console for error messages

### Data Verification:
```bash
cd /home/user/webapp
python3 verify_kpi_card.py
```

**Expected Output:**
```
✅ First KPI: New Patient Lead Volume (kpi_1_1_1)
✅ key_insights type: str
✅ scenarios type: list
✅ scenarios length: 3
✅ All required fields present
```

## 📊 Data Structure Reference

### Complete KPI Object (Level 4):
```javascript
{
  // Basic Info
  "id": "kpi_1_1_1",
  "name": "New Patient Lead Volume",
  "level": 4,  // ← MUST BE 4 for card to open
  "type": "kpi",  // ← MUST BE 'kpi'
  
  // Metrics
  "value": "245",
  "target": "280",
  "unit": "patients",
  "rag": "green",
  "trend": "up",
  
  // 10 Layers of Intelligence
  "context": { ... },
  "current_state": { ... },
  "trend_data": [ ... ],
  "root_causes": [ ... ],
  "predictive_insights": {
    "scenarios": [ ... ]  // ← ARRAY (not object)
  },
  "trend_analysis": {
    "key_insights": "..."  // ← STRING (not array)
  },
  "dependencies": [ ... ],
  "accountability": { ... },
  "recommended_actions": [ ... ],
  "contributing_factors": [ ... ]
}
```

## 🔧 Recent Fixes Committed

1. **2025-11-26 15:XX** - Fix key_insights string handling
   - Changed from `.map()` to string display
   - Files: `index.html`, `command-center.html`

2. **2025-11-26 14:XX** - Fix scenarios array structure
   - Changed scenarios from object to array
   - File: `generate_complete_nyss_kpis.py`

3. **2025-11-26 13:XX** - Fix tree structure
   - Rebuilt 5-pillar hierarchy
   - File: `fix_pillar_structure.py`

## 📞 Still Not Working?

If KPI cards still don't open after following all steps:

1. **Capture Console Output**:
   - Open Console (F12)
   - Click a Level 4 KPI node
   - Copy ALL console messages
   - Take a screenshot showing:
     - Tree graph with node highlighted
     - Console messages
     - Whether panel appeared

2. **Verify Data Structure**:
   ```bash
   cd /home/user/webapp
   python3 -c "
   import json
   with open('public/kpi_map.json') as f:
       data = json.load(f)
   print('Tree root:', data['tree']['name'])
   print('Pillars:', len(data['tree']['children']))
   print('KPI nodes:', len(data['nodes']))
   print('First KPI:', data['nodes'][0]['id'])
   "
   ```

3. **Test URLs**:
   - Executive Intelligence: https://3000-i3trzw1s8ci0ydttfvlky-b9b802c4.sandbox.novita.ai/
   - Command Center: https://3000-i3trzw1s8ci0ydttfvlky-b9b802c4.sandbox.novita.ai/command-center
   - GitHub Repo: https://github.com/gowthamprabakar/CareOptions-Kids-Dashboard-v8.5-Revenue-Rebuild

---

**Last Updated**: 2025-11-26  
**Status**: ✅ ALL KNOWN ISSUES RESOLVED
