import json

# Read the current KPI data
with open('public/kpi_map.json', 'r') as f:
    kpi_data = json.load(f)

# Rebuild tree structure correctly
tree_structure = {}

for node in kpi_data['nodes']:
    pillar = node['pillar']
    macro = node['macro_process']
    category = node['category']
    
    if pillar not in tree_structure:
        tree_structure[pillar] = {}
    if macro not in tree_structure[pillar]:
        tree_structure[pillar][macro] = {}
    if category not in tree_structure[pillar][macro]:
        tree_structure[pillar][macro][category] = []
    
    tree_structure[pillar][macro][category].append({
        "name": node['name'],
        "id": node['id'],
        "level": 4
    })

# Build proper tree
tree_children = []
for pillar_name, macros in tree_structure.items():
    macro_children = []
    for macro_name, categories in macros.items():
        category_children = []
        for category_name, kpis in categories.items():
            category_children.append({
                "name": category_name,
                "id": f"cat_{category_name.replace(' ', '_').replace('&', 'and').lower()}",
                "level": 3,
                "children": kpis
            })
        macro_children.append({
            "name": macro_name,
            "id": f"macro_{macro_name.replace(' ', '_').replace('&', 'and').lower()}",
            "level": 2,
            "children": category_children
        })
    tree_children.append({
        "name": pillar_name,
        "id": f"pillar_{pillar_name.replace(' ', '_').replace('&', 'and').lower()}",
        "level": 1,
        "children": macro_children
    })

kpi_data['tree']['children'] = tree_children

# Save fixed data
with open('public/kpi_map.json', 'w') as f:
    json.dump(kpi_data, f, indent=2)

with open('public/complete_kpi_tree.json', 'w') as f:
    json.dump(kpi_data, f, indent=2)

with open('public/kpi_map_complete.json', 'w') as f:
    json.dump(kpi_data, f, indent=2)

print(f"✅ Fixed tree structure!")
print(f"📊 Pillars: {len(tree_structure)}")
for pillar_name, macros in tree_structure.items():
    kpi_count = sum(len(kpis) for categories in macros.values() for kpis in categories.values())
    print(f"  • {pillar_name}: {kpi_count} KPIs")
