#!/usr/bin/env python3
"""
Fix Tree Structure - Create proper pillar hierarchy
Correct structure: Root → Pillars → Macro Processes → Categories → KPIs
"""

import json

def main():
    # Load current KPI data
    with open('public/kpi_map.json', 'r') as f:
        data = json.load(f)
    
    nodes = data['nodes']
    print(f"Total KPI nodes: {len(nodes)}")
    
    # Define 5 pillars with their macro processes (using exact names from data)
    pillar_structure = {
        "Patient Access & Intake": [
            "Patient Acquisition",
            "Scheduling & Appointment Mgmt",
            "Intake Documentation",
            "Clinical Pre-Visit Prep",
            "Patient Experience"
        ],
        "Clinical Operations": [
            "Provider Documentation",
            "Clinical Workflow",
            "Orders Management",
            "Provider Performance",
            "Care Quality & Safety"
        ],
        "Surgical Coordination": [
            "Surgical Candidacy",
            "Pre-Cert & Authorization",
            "Surgical Scheduling",
            "Post-Op Care",
            "Surgical Billing"
        ],
        "Revenue Cycle Management": [
            "Pre-Billing Readiness",
            "Claim Creation",
            "Payer Response",
            "Appeals",
            "AR & Cash Posting",
            "Financial Performance"
        ],
        "Compliance & Risk Management": [
            "Regulatory Compliance",
            "Risk Management",
            "Quality Assurance",
            "Credentialing",
            "Audit & Monitoring",
            "Policy Management"
        ]
    }
    
    # Group nodes by pillar and macro process
    pillar_map = {}
    
    for node in nodes:
        pillar_name = node['pillar']
        macro_name = node['macro_process']
        category_name = node.get('category', 'General')
        
        if pillar_name not in pillar_map:
            pillar_map[pillar_name] = {}
        
        if macro_name not in pillar_map[pillar_name]:
            pillar_map[pillar_name][macro_name] = {}
        
        if category_name not in pillar_map[pillar_name][macro_name]:
            pillar_map[pillar_name][macro_name][category_name] = []
        
        pillar_map[pillar_name][macro_name][category_name].append(node)
    
    # Build hierarchical tree with pillars
    tree_children = []
    node_counter = 1
    
    for pillar_idx, (pillar_name, macro_list) in enumerate(pillar_structure.items(), 1):
        pillar_node = {
            "id": f"pillar_{pillar_idx}",
            "name": pillar_name,
            "level": 1,
            "type": "pillar",
            "children": []
        }
        
        # Add macro processes to this pillar
        for macro_name in macro_list:
            if pillar_name not in pillar_map or macro_name not in pillar_map[pillar_name]:
                continue
            
            macro_node = {
                "id": f"pillar_{pillar_idx}_macro_{len(pillar_node['children'])+1}",
                "name": macro_name,
                "level": 2,
                "type": "macro",
                "children": []
            }
            
            # Add categories to this macro process
            categories = pillar_map[pillar_name][macro_name]
            for category_name, kpis in categories.items():
                category_node = {
                    "id": f"pillar_{pillar_idx}_macro_{len(pillar_node['children'])+1}_cat_{len(macro_node['children'])+1}",
                    "name": category_name,
                    "level": 3,
                    "type": "category",
                    "children": []
                }
                
                # Add KPIs to this category
                for kpi in kpis:
                    kpi_node = {
                        "id": kpi['id'],
                        "name": kpi['name'],
                        "level": 4,
                        "type": "kpi",
                        "value": kpi['value'],
                        "target": kpi['target'],
                        "unit": kpi['unit'],
                        "rag": kpi['rag']
                    }
                    category_node['children'].append(kpi_node)
                
                macro_node['children'].append(category_node)
            
            pillar_node['children'].append(macro_node)
        
        tree_children.append(pillar_node)
    
    # Create root node with pillars
    tree = {
        "id": "root",
        "name": "NYSS Complete Operations",
        "level": 0,
        "type": "root",
        "children": tree_children
    }
    
    # Update data structure
    data['tree'] = tree
    data['version'] = "1.0-nyss-complete-all-pillars-fixed"
    
    # Save updated structure
    with open('public/kpi_map.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    with open('public/complete_kpi_tree.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    with open('public/kpi_map_complete.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("\n✅ Tree structure fixed!")
    print(f"📊 Structure: Root → {len(tree_children)} Pillars → Macro Processes → Categories → 213 KPIs")
    
    # Print summary
    print("\n🎯 Pillar Summary:")
    for pillar in tree_children:
        macro_count = len(pillar['children'])
        kpi_count = sum(
            len(cat['children']) 
            for macro in pillar['children'] 
            for cat in macro['children']
        )
        print(f"  • {pillar['name']}: {macro_count} macros, {kpi_count} KPIs")

if __name__ == "__main__":
    main()
