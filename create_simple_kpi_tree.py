#!/usr/bin/env python3
"""
Create simple tree structure: Root → 5 Pillars → KPIs directly
No intermediate Macro/Category levels - just 2 levels for easy access
"""
import json

# Load existing KPI data
with open('public/kpi_map.json', 'r') as f:
    data = json.load(f)

nodes = data['nodes']

# Group KPIs by pillar
from collections import defaultdict
kpis_by_pillar = defaultdict(list)

for kpi in nodes:
    pillar = kpi.get('pillar', 'Unknown')
    kpis_by_pillar[pillar].append(kpi)

print(f'Creating simple tree structure...')
print(f'Total KPIs: {len(nodes)}')
print()

# Define pillar order
pillar_order = [
    'Patient Access & Intake',
    'Clinical Operations',
    'Surgical Coordination',
    'Revenue Cycle Management',
    'Compliance & Risk Management'
]

# Create tree structure
tree = {
    'id': 'root',
    'name': 'NYSS Complete Operations',
    'level': 0,
    'type': 'root',
    'children': []
}

for i, pillar_name in enumerate(pillar_order, 1):
    kpis = kpis_by_pillar.get(pillar_name, [])
    
    if not kpis:
        print(f'⚠️ No KPIs found for pillar: {pillar_name}')
        continue
    
    # Create pillar node
    pillar_node = {
        'id': f'pillar_{i}',
        'name': pillar_name,
        'level': 1,
        'type': 'pillar',
        'children': []
    }
    
    # Add KPIs directly under pillar (Level 2)
    for kpi in kpis:
        kpi_node = {
            'id': kpi['id'],
            'name': kpi['name'],
            'level': 2,  # KPIs are now Level 2 (directly under pillars)
            'type': 'kpi',
            'value': kpi['value'],
            'target': kpi['target'],
            'unit': kpi.get('unit', ''),
            'rag': kpi['rag'],
            'trend': kpi['trend']
        }
        pillar_node['children'].append(kpi_node)
    
    tree['children'].append(pillar_node)
    print(f'✅ {pillar_name}: {len(kpis)} KPIs')

# Update data structure
data['tree'] = tree
data['version'] = '1.0-nyss-simple-2level'

# Save updated structure
with open('public/kpi_map.json', 'w') as f:
    json.dump(data, f, indent=2)

print()
print('=' * 60)
print('✅ SIMPLE TREE STRUCTURE CREATED!')
print('=' * 60)
print('Structure: Root (L0) → 5 Pillars (L1) → 213 KPIs (L2)')
print()
print('Summary:')
for pillar in tree['children']:
    print(f'  {pillar["name"]}: {len(pillar["children"])} KPIs at Level 2')
print()
print('Now KPI cards will open with just 2 clicks:')
print('  1. Click Pillar (Level 1)')
print('  2. Click KPI (Level 2) → Card opens! 🎉')
