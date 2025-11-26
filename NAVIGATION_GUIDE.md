# 🧭 Dashboard Navigation Guide - How to Open KPI Cards

## ⚠️ IMPORTANT: Understanding the Tree Structure

The tree graph has **4 levels** of hierarchy. KPI detail cards ONLY open for **Level 4 (KPI nodes)**.

```
Level 0: Root (NYSS Complete Operations)
         │
         ├─ Level 1: Pillars (5 nodes) - Click to expand
         │           │
         │           ├─ Level 2: Macro Processes (27 nodes) - Click to expand
         │           │           │
         │           │           ├─ Level 3: Categories (52 nodes) - Click to expand
         │           │           │           │
         │           │           │           └─ Level 4: KPIs (213 nodes) ← CLICK THESE! 🎯
```

---

## 📍 Method 1: Executive Intelligence (Tree Graph)

**URL:** https://3000-i3trzw1s8ci0ydttfvlky-b9b802c4.sandbox.novita.ai/

### Step-by-Step Instructions:

#### **Step 1: Identify Category Nodes**
When you first load the page, you'll see **3 levels** expanded:
- Root (center)
- 5 Pillars (Level 1)
- Macro Processes (Level 2)
- Categories (Level 3) ← **These are at the edges**

#### **Step 2: Click on a Category Node**
**Example path:**
1. Look for "**Patient Access & Intake**" (Pillar)
2. Follow the branch to "**Patient Acquisition**" (Macro)
3. Follow to "**Lead Intake & Conversion**" (Category) ← **Click this!**
4. Several KPI nodes will appear:
   - New Patient Lead Volume
   - Lead Source Mix - Google
   - Lead Source Mix - Referral
   - etc.

#### **Step 3: Click or Shift+Click a KPI Node**
Once KPI nodes are visible (blue circles at Level 4):
- **Normal Click** → Opens 10-layer detail card on the right
- **Shift+Click** → Also opens detail card

### Visual Cues:
- **Pillar nodes** (Level 1): Largest, closest to center
- **Macro nodes** (Level 2): Medium size
- **Category nodes** (Level 3): Smaller, has **+** indicator
- **KPI nodes** (Level 4): **Blue circles**, leaf nodes (no children)

### Console Debugging:
Open browser console (F12) and watch for these messages when clicking:
- `Shift+Click - Node: [name] | Level: 4 | Type: kpi` ✅ Good!
- `✅ Opening KPI card for: [name]` ✅ Card should open!
- `ℹ️ Category node clicked. Expand to see KPIs below.` ← You clicked Level 3, need to go deeper

---

## 📊 Method 2: Command Center (Table View)

**URL:** https://3000-i3trzw1s8ci0ydttfvlky-b9b802c4.sandbox.novita.ai/command-center.html

### This Should Be EASY - If It's Not Working:

#### **Option A: Click the Entire Row**
- Click anywhere on any row in the table
- Detail panel should slide in from the right

#### **Option B: Click the Eye Icon**
- Click the 👁️ icon in the "Actions" column (last column)
- Detail panel should open

### Troubleshooting Command Center:

If clicking rows doesn't work:
1. **Open browser console** (Press F12)
2. **Click a row** and look for these messages:
   - `🖱️ Row clicked for KPI: [name]` ← Row click detected
   - `🎯 showDetailPanel called for: [name]` ← Function called
   - `📋 Panel element: Found` ← DOM elements found
   - `✅ Adding "open" class to panel` ← Panel should open

3. If you see **NO console messages**:
   - The `onclick` event is not attached
   - Try refreshing with **Ctrl+Shift+R** (hard refresh)

4. If you see console messages but **panel doesn't appear**:
   - Check if panel is hidden behind other elements
   - Look for the panel on the **right side** of the screen

---

## 🔧 Quick Test Checklist

### Test 1: Command Center (Easier)
1. Go to: https://3000-i3trzw1s8ci0ydttfvlky-b9b802c4.sandbox.novita.ai/command-center.html
2. Open console (F12)
3. Click the **first row** in the table
4. Watch console for messages
5. Look for panel sliding in from the right

### Test 2: Executive Intelligence (Requires Navigation)
1. Go to: https://3000-i3trzw1s8ci0ydttfvlky-b9b802c4.sandbox.novita.ai/
2. Open console (F12)
3. Find "**Patient Access & Intake**" pillar
4. Follow branch to "**Patient Acquisition**" macro
5. Click "**Lead Intake & Conversion**" category (has + symbol)
6. Click "**New Patient Lead Volume**" KPI (blue circle)
7. Watch console and panel should appear on right

---

## 🐛 Still Not Working? Send Me This Info:

1. **Which dashboard?** (Command Center or Executive Intelligence)
2. **What you clicked on?** (Row number, or node name)
3. **Console messages?** (Copy all messages after clicking)
4. **Browser?** (Chrome, Firefox, Safari, Edge?)
5. **Any errors in console?** (Red text)

---

## 📖 Additional Navigation Tips

### Tree Graph:
- **Zoom:** Scroll wheel
- **Pan:** Click and drag the background
- **Expand/Collapse:** Click nodes with **+** or **-** indicators
- **Reset View:** Refresh page (Ctrl+R)

### Command Center:
- **Filter:** Click Red/Amber/Green/All buttons at top
- **Search:** Type in search box to find specific KPIs
- **Sort:** Click column headers to sort

---

## ✅ Success Indicators

When a KPI card opens successfully, you'll see:
- **Panel slides in** from the right side
- **10 layers of information** displayed:
  1. KPI Summary (Value, Target, Status)
  2. Context & Business Impact
  3. Current State Analysis
  4. Root Cause Analysis (3 causes)
  5. Predictive Insights (3 scenarios)
  6. Statistical Analysis
  7. Dependency Graph
  8. Accountability & Ownership
  9. Recommended Actions
  10. Contributing Factors
- **Charts and visualizations** appear after a moment
- **Close button (×)** at top-right of panel

---

## 🎯 Most Common Mistakes

1. ❌ **Clicking Pillar/Macro/Category nodes** expecting cards to open
   - ✅ These only expand - keep clicking until you reach Level 4 KPIs

2. ❌ **Not expanding deep enough** in the tree
   - ✅ You need to click 3-4 times to reach KPIs

3. ❌ **Expecting instant results** after clicking
   - ✅ Wait 1-2 seconds for panel animation

4. ❌ **Looking in wrong place** for the panel
   - ✅ Panel appears on the RIGHT side, not left

5. ❌ **Browser cache showing old version**
   - ✅ Hard refresh: Ctrl+Shift+R or Cmd+Shift+R

---

## 📞 Need Help?

If you've tried everything above and it still doesn't work, the issue might be:
- Browser compatibility issue
- JavaScript error blocking execution
- Network/loading issue
- Caching problem

**Send me the console log** and I'll debug it immediately!
