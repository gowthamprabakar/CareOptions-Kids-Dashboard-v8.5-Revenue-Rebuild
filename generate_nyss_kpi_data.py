#!/usr/bin/env python3
"""
NYSS Patient Access & Intake KPI Data Generator
Generates comprehensive KPI tree structure with 10-layer intelligence
"""

import json
import random
from datetime import datetime, timedelta

def generate_trend_data():
    """Generate 6 months of realistic trend data"""
    base = random.uniform(70, 95)
    trend = []
    for i in range(6):
        variation = random.uniform(-5, 5)
        value = max(0, min(100, base + variation))
        trend.append(round(value, 1))
        base = value
    return trend

def determine_rag_status(value, target):
    """Determine RAG status based on value vs target"""
    if value >= target:
        return "green"
    elif value >= target * 0.85:
        return "amber"
    else:
        return "red"

def generate_root_causes():
    """Generate AI-powered root causes"""
    causes = [
        {
            "cause": "Incomplete intake documentation process",
            "confidence": random.randint(85, 95),
            "impact": "High",
            "data_points": random.randint(800, 1500)
        },
        {
            "cause": "Insurance verification delays",
            "confidence": random.randint(75, 90),
            "impact": "Medium",
            "data_points": random.randint(500, 1000)
        },
        {
            "cause": "Staff training gaps on new protocols",
            "confidence": random.randint(70, 85),
            "impact": "Medium",
            "data_points": random.randint(300, 700)
        }
    ]
    return random.sample(causes, k=min(3, len(causes)))

def generate_predictive_insights(current_value, trend_data):
    """Generate AI predictive insights"""
    recent_trend = sum(trend_data[-3:]) / 3
    if recent_trend > current_value:
        pattern = "Improving"
        best_case = current_value + random.uniform(3, 8)
        likely_case = current_value + random.uniform(1, 4)
        worst_case = current_value - random.uniform(0, 2)
    elif recent_trend < current_value:
        pattern = "Deteriorating"
        best_case = current_value + random.uniform(0, 3)
        likely_case = current_value - random.uniform(1, 4)
        worst_case = current_value - random.uniform(3, 8)
    else:
        pattern = "Stabilizing"
        best_case = current_value + random.uniform(2, 5)
        likely_case = current_value + random.uniform(-1, 1)
        worst_case = current_value - random.uniform(2, 5)
    
    return {
        "pattern": pattern,
        "confidence": random.randint(75, 90),
        "scenarios": {
            "best_case": {"value": round(max(0, min(100, best_case)), 1), "probability": random.randint(20, 30)},
            "most_likely": {"value": round(max(0, min(100, likely_case)), 1), "probability": random.randint(45, 60)},
            "worst_case": {"value": round(max(0, min(100, worst_case)), 1), "probability": random.randint(15, 25)}
        },
        "leading_indicators": ["System utilization", "Staff availability", "Protocol adherence"]
    }

def generate_recommended_actions(rag_status):
    """Generate detailed recommended actions"""
    if rag_status == "red":
        return [
            {
                "priority": "Critical",
                "action": "Implement urgent intake packet verification protocol",
                "timeline": "1 week",
                "owner": "Intake Coordinator",
                "expected_impact": "$150K-$250K monthly improvement",
                "resources": "Dedicated verification team, 2 FTEs",
                "success_metrics": "Packet completeness >95%"
            },
            {
                "priority": "High",
                "action": "Deploy automated insurance verification system",
                "timeline": "2-3 weeks",
                "owner": "IT Manager + RCM Director",
                "expected_impact": "40% reduction in verification delays",
                "resources": "Availity integration, $25K budget",
                "success_metrics": "Real-time verification >90%"
            }
        ]
    elif rag_status == "amber":
        return [
            {
                "priority": "High",
                "action": "Enhance staff training on documentation protocols",
                "timeline": "2 weeks",
                "owner": "Training Manager",
                "expected_impact": "15-20% accuracy improvement",
                "resources": "Training materials, 20 hrs/week",
                "success_metrics": "Staff certification >95%"
            }
        ]
    else:
        return [
            {
                "priority": "Medium",
                "action": "Maintain current processes and monitor KPI trends",
                "timeline": "Ongoing",
                "owner": "Operations Manager",
                "expected_impact": "Sustained performance",
                "resources": "Regular monitoring",
                "success_metrics": "Maintain green status"
            }
        ]

# Main KPI Data Structure
kpi_tree = {
    "version": "1.0-nyss-patient-access-intake",
    "total_nodes": 0,
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
        "children": []
    },
    "nodes": []
}

# Macro Process 1: Patient Acquisition
macro1 = {
    "name": "Patient Acquisition",
    "id": "macro_1",
    "level": 1,
    "children": []
}

# Category 1.1 - Lead Intake & Conversion
cat_1_1 = {
    "name": "Lead Intake & Conversion",
    "id": "cat_1_1",
    "level": 2,
    "children": []
}

# KPI 1: New Patient Lead Volume
kpi_1 = {
    "name": "New Patient Lead Volume",
    "id": "kpi_new_patient_lead_volume",
    "level": 3,
    "value": 245,
    "target": 280,
    "unit": "patients",
    "trend": "down",
    "rag": "amber"
}

kpi_1_node = {
    "id": "kpi_new_patient_lead_volume",
    "name": "New Patient Lead Volume",
    "value": 245,
    "target": 280,
    "unit": "patients",
    "rag": "amber",
    "trend": "down",
    "context": {
        "definition": "Total inbound new patient appointments from all sources (calls, referrals, online, attorneys)",
        "business_impact": "Primary driver of surgical pipeline and revenue growth. Critical for maintaining practice volume.",
        "industry_benchmark": "250-300 new leads per month for multi-specialty spine practices"
    },
    "current_state": {
        "status": "amber",
        "value": 245,
        "target": 280,
        "gap": 35,
        "gap_percentage": 12.5,
        "financial_impact": "$175K potential monthly revenue at risk"
    },
    "trend_data": generate_trend_data(),
    "root_causes": [
        {
            "cause": "Decreased attorney referral volume (-18% MoM)",
            "confidence": 92,
            "impact": "High",
            "data_points": 1240
        },
        {
            "cause": "Google Ads campaign budget reduction",
            "confidence": 88,
            "impact": "High",
            "data_points": 850
        },
        {
            "cause": "Intake call abandon rate increased to 22%",
            "confidence": 85,
            "impact": "Medium",
            "data_points": 560
        }
    ],
    "predictive_insights": {
        "pattern": "Deteriorating",
        "confidence": 82,
        "scenarios": {
            "best_case": {"value": 268, "probability": 25},
            "most_likely": {"value": 235, "probability": 55},
            "worst_case": {"value": 210, "probability": 20}
        },
        "leading_indicators": ["Marketing spend", "Call center capacity", "Attorney relationship health"]
    },
    "trend_analysis": {
        "current_trend": "Declining",
        "trend_strength": "Moderate",
        "volatility": "Low",
        "key_insights": "Consistent downward trajectory over past 3 months requires immediate attention"
    },
    "dependencies": {
        "upstream": ["Marketing campaign effectiveness", "Attorney referral network", "Online presence"],
        "downstream": ["Appointment scheduling volume", "Surgical pipeline", "Revenue projection"],
        "peer_metrics": ["Referral-to-Appointment Conversion", "Days to First Appointment"]
    },
    "people_accountable": [
        {
            "name": "Jennifer Martinez",
            "title": "Director of Patient Access",
            "department": "Front Office Operations",
            "email": "jmartinez@nyss.com",
            "role": "Primary Owner",
            "avatar_color": "#4A90E2"
        },
        {
            "name": "Robert Chen",
            "title": "Marketing Manager",
            "department": "Marketing",
            "email": "rchen@nyss.com",
            "role": "Contributor",
            "avatar_color": "#7B68EE"
        }
    ],
    "recommended_actions": [
        {
            "priority": "Critical",
            "action": "Re-engage attorney referral partners with quarterly outreach program",
            "timeline": "2 weeks",
            "owner": "Director of Patient Access",
            "expected_impact": "$120K-$180K monthly revenue recovery",
            "resources": "Attorney liaison, relationship management database",
            "success_metrics": "Attorney referrals increase by 25%"
        },
        {
            "priority": "High",
            "action": "Increase Google Ads budget by 30% targeting injury-specific keywords",
            "timeline": "1 week",
            "owner": "Marketing Manager",
            "expected_impact": "40-60 additional leads per month",
            "resources": "$8K additional monthly ad spend",
            "success_metrics": "Online lead conversion >15%"
        },
        {
            "priority": "High",
            "action": "Implement call center training to reduce abandon rate below 15%",
            "timeline": "2 weeks",
            "owner": "Front Desk Supervisor",
            "expected_impact": "15-20 additional conversions per month",
            "resources": "Training program, call monitoring",
            "success_metrics": "Call abandon rate <15%"
        }
    ],
    "contributing_factors": {
        "internal": [
            {"factor": "Call center staffing levels", "impact": "High"},
            {"factor": "Intake process efficiency", "impact": "Medium"},
            {"factor": "Brand reputation", "impact": "Medium"}
        ],
        "external": [
            {"factor": "Legal market conditions", "impact": "High"},
            {"factor": "Competitor marketing activity", "impact": "Medium"},
            {"factor": "Seasonal injury patterns", "impact": "Low"}
        ]
    }
}

# Add sub-KPIs
kpi_1["children"] = [
    {"name": "Lead Source Mix", "id": "kpi_lead_source_mix", "level": 4},
    {"name": "Conversion by Source", "id": "kpi_conversion_by_source", "level": 4},
    {"name": "Call Abandon Rate", "id": "kpi_call_abandon_rate", "level": 4}
]

# Add to tree
cat_1_1["children"].append(kpi_1)
macro1["children"].append(cat_1_1)
kpi_tree["tree"]["children"].append(macro1)
kpi_tree["nodes"].append(kpi_1_node)

# Function to create more KPIs
def create_kpi_node(kpi_id, name, value, target, unit, parent_level):
    """Create a complete KPI node with all 10 layers"""
    rag = determine_rag_status(value, target)
    trend_data = generate_trend_data()
    recent_avg = sum(trend_data[-3:]) / 3
    trend = "up" if value > recent_avg else ("down" if value < recent_avg else "stable")
    
    node = {
        "id": kpi_id,
        "name": name,
        "value": value,
        "target": target,
        "unit": unit,
        "rag": rag,
        "trend": trend,
        "context": {
            "definition": f"{name} measures the performance of {name.lower()} in patient access operations",
            "business_impact": f"Critical metric for {name.lower()} affecting overall patient flow and revenue",
            "industry_benchmark": f"{target} {unit} is the target benchmark for this KPI"
        },
        "current_state": {
            "status": rag,
            "value": value,
            "target": target,
            "gap": target - value,
            "gap_percentage": round((target - value) / target * 100, 1),
            "financial_impact": f"${abs(target - value) * random.randint(500, 2000):,} impact per month"
        },
        "trend_data": trend_data,
        "root_causes": generate_root_causes(),
        "predictive_insights": generate_predictive_insights(value, trend_data),
        "trend_analysis": {
            "current_trend": trend.capitalize(),
            "trend_strength": random.choice(["Strong", "Moderate", "Weak"]),
            "volatility": random.choice(["High", "Medium", "Low"]),
            "key_insights": f"{name} shows {trend} trajectory requiring monitoring"
        },
        "dependencies": {
            "upstream": [f"Upstream dependency {i+1}" for i in range(2)],
            "downstream": [f"Downstream dependency {i+1}" for i in range(2)],
            "peer_metrics": [f"Related metric {i+1}" for i in range(2)]
        },
        "people_accountable": [
            {
                "name": random.choice(["Jennifer Martinez", "Robert Chen", "Sarah Johnson", "Michael Brown"]),
                "title": random.choice(["Director", "Manager", "Coordinator", "Supervisor"]),
                "department": random.choice(["Patient Access", "Clinical Operations", "RCM", "Scheduling"]),
                "email": f"{random.choice(['jmartinez', 'rchen', 'sjohnson', 'mbrown'])}@nyss.com",
                "role": "Primary Owner",
                "avatar_color": random.choice(["#4A90E2", "#7B68EE", "#50C878", "#FF6B6B"])
            }
        ],
        "recommended_actions": generate_recommended_actions(rag),
        "contributing_factors": {
            "internal": [
                {"factor": "Process efficiency", "impact": random.choice(["High", "Medium", "Low"])},
                {"factor": "Staff training", "impact": random.choice(["High", "Medium", "Low"])}
            ],
            "external": [
                {"factor": "Market conditions", "impact": random.choice(["High", "Medium", "Low"])},
                {"factor": "Regulatory environment", "impact": random.choice(["High", "Medium", "Low"])}
            ]
        }
    }
    
    return node

print("Generating NYSS Patient Access & Intake KPI data...")

# Generate remaining KPIs
kpis_to_generate = [
    # Macro 1 - Patient Acquisition (continued)
    ("kpi_referral_conversion", "Referral-to-Appointment Conversion", 78, 85, "%", "cat_1_1"),
    
    # Macro 2 - Scheduling & Appointment Management
    ("kpi_days_first_appt", "Days to First Appointment", 5.2, 3.0, "days", "cat_2_1"),
    ("kpi_wait_time", "Appointment Wait Time (In-clinic)", 18, 15, "minutes", "cat_2_1"),
    ("kpi_no_show", "No-Show Rate", 14.5, 10.0, "%", "cat_2_1"),
    
    # Macro 3 - Intake Documentation & Verification
    ("kpi_packet_complete", "Packet Completeness Rate", 92, 98, "%", "cat_3_1"),
    ("kpi_missing_items", "Missing Packet Item Rate", 8.5, 2.0, "%", "cat_3_1"),
    ("kpi_verification_accuracy", "Eligibility Verification Accuracy", 94, 98, "%", "cat_3_2"),
    ("kpi_verification_time", "Benefit Verification Turnaround", 2.8, 1.5, "days", "cat_3_2"),
    ("kpi_financial_clearance", "Pre-Visit Financial Clearance Rate", 88, 95, "%", "cat_3_3"),
    
    # Macro 4 - Clinical Pre-Visit Preparation
    ("kpi_imaging_available", "Imaging Availability Before Visit", 85, 95, "%", "cat_4_1"),
    ("kpi_referral_notes", "Referral Notes Availability", 90, 98, "%", "cat_4_1"),
    
    # Macro 5 - Patient Experience
    ("kpi_nps", "New Patient NPS", 72, 80, "score", "cat_5_1"),
    ("kpi_intake_satisfaction", "Intake Satisfaction Score", 4.2, 4.5, "rating", "cat_5_1"),
]

for kpi_data in kpis_to_generate:
    kpi_id, name, value, target, unit, category = kpi_data
    node = create_kpi_node(kpi_id, name, value, target, unit, 3)
    kpi_tree["nodes"].append(node)

# Build complete tree structure
kpi_tree["tree"]["children"] = [
    {
        "name": "Patient Acquisition",
        "id": "macro_1",
        "level": 1,
        "children": [
            {
                "name": "Lead Intake & Conversion",
                "id": "cat_1_1",
                "level": 2,
                "children": [
                    {"name": "New Patient Lead Volume", "id": "kpi_new_patient_lead_volume", "level": 3, "children": []},
                    {"name": "Referral-to-Appointment Conversion", "id": "kpi_referral_conversion", "level": 3, "children": []}
                ]
            }
        ]
    },
    {
        "name": "Scheduling & Appointment Management",
        "id": "macro_2",
        "level": 1,
        "children": [
            {
                "name": "Access Efficiency",
                "id": "cat_2_1",
                "level": 2,
                "children": [
                    {"name": "Days to First Appointment", "id": "kpi_days_first_appt", "level": 3, "children": []},
                    {"name": "Appointment Wait Time (In-clinic)", "id": "kpi_wait_time", "level": 3, "children": []},
                    {"name": "No-Show Rate", "id": "kpi_no_show", "level": 3, "children": []}
                ]
            }
        ]
    },
    {
        "name": "Intake Documentation & Verification",
        "id": "macro_3",
        "level": 1,
        "children": [
            {
                "name": "Packet Completeness",
                "id": "cat_3_1",
                "level": 2,
                "children": [
                    {"name": "Packet Completeness Rate", "id": "kpi_packet_complete", "level": 3, "children": []},
                    {"name": "Missing Packet Item Rate", "id": "kpi_missing_items", "level": 3, "children": []}
                ]
            },
            {
                "name": "Insurance Verification",
                "id": "cat_3_2",
                "level": 2,
                "children": [
                    {"name": "Eligibility Verification Accuracy", "id": "kpi_verification_accuracy", "level": 3, "children": []},
                    {"name": "Benefit Verification Turnaround", "id": "kpi_verification_time", "level": 3, "children": []}
                ]
            },
            {
                "name": "Financial Clearance",
                "id": "cat_3_3",
                "level": 2,
                "children": [
                    {"name": "Pre-Visit Financial Clearance Rate", "id": "kpi_financial_clearance", "level": 3, "children": []}
                ]
            }
        ]
    },
    {
        "name": "Clinical Pre-Visit Preparation",
        "id": "macro_4",
        "level": 1,
        "children": [
            {
                "name": "Clinical Records Readiness",
                "id": "cat_4_1",
                "level": 2,
                "children": [
                    {"name": "Imaging Availability Before Visit", "id": "kpi_imaging_available", "level": 3, "children": []},
                    {"name": "Referral Notes Availability", "id": "kpi_referral_notes", "level": 3, "children": []}
                ]
            }
        ]
    },
    {
        "name": "Patient Experience",
        "id": "macro_5",
        "level": 1,
        "children": [
            {
                "name": "Service Quality",
                "id": "cat_5_1",
                "level": 2,
                "children": [
                    {"name": "New Patient NPS", "id": "kpi_nps", "level": 3, "children": []},
                    {"name": "Intake Satisfaction Score", "id": "kpi_intake_satisfaction", "level": 3, "children": []}
                ]
            }
        ]
    }
]

# Update total nodes count
kpi_tree["total_nodes"] = len(kpi_tree["nodes"])

print(f"Generated {kpi_tree['total_nodes']} KPI nodes")

# Save to file
output_file = "public/kpi_map.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(kpi_tree, f, indent=2, ensure_ascii=False)

print(f"✅ KPI data saved to {output_file}")
print(f"📊 Total nodes: {kpi_tree['total_nodes']}")
print("🎯 KPI structure:")
for macro in kpi_tree["tree"]["children"]:
    print(f"  - {macro['name']} ({len(macro['children'])} categories)")
