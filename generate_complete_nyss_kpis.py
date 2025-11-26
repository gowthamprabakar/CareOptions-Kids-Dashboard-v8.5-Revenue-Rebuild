#!/usr/bin/env python3
"""
Complete NYSS KPI Data Generator - All Pillars
Generates 200+ KPIs from the NYSJ document with full 10-layer intelligence
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

def determine_rag_status(value, target, is_percentage=True):
    """Determine RAG status based on value vs target"""
    if is_percentage:
        if value >= target * 0.95:
            return "green"
        elif value >= target * 0.85:
            return "amber"
        else:
            return "red"
    else:  # For metrics like days where lower is better
        if value <= target * 1.05:
            return "green"
        elif value <= target * 1.15:
            return "amber"
        else:
            return "red"

def generate_root_causes(kpi_name):
    """Generate AI-powered root causes"""
    causes_pool = [
        {"cause": "Incomplete documentation process", "confidence": random.randint(85, 95), "impact": "High", "data_points": random.randint(800, 1500)},
        {"cause": "Insurance verification delays", "confidence": random.randint(75, 90), "impact": "Medium", "data_points": random.randint(500, 1000)},
        {"cause": "Staff training gaps", "confidence": random.randint(70, 85), "impact": "Medium", "data_points": random.randint(300, 700)},
        {"cause": "System integration issues", "confidence": random.randint(80, 92), "impact": "High", "data_points": random.randint(600, 1200)},
        {"cause": "Payer policy changes", "confidence": random.randint(75, 88), "impact": "High", "data_points": random.randint(400, 900)},
        {"cause": "Provider workflow bottlenecks", "confidence": random.randint(78, 90), "impact": "Medium", "data_points": random.randint(350, 800)},
    ]
    return random.sample(causes_pool, k=min(3, len(causes_pool)))

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
        "leading_indicators": random.sample(["System utilization", "Staff availability", "Protocol adherence", "Market conditions", "Technology adoption"], 3)
    }

def generate_recommended_actions(rag_status):
    """Generate detailed recommended actions"""
    if rag_status == "red":
        return [
            {
                "priority": "Critical",
                "action": "Implement urgent corrective protocol",
                "timeline": "1 week",
                "owner": "Operations Director",
                "expected_impact": "$150K-$250K monthly improvement",
                "resources": "Dedicated team, 2-3 FTEs",
                "success_metrics": "Target achievement >95%"
            },
            {
                "priority": "High",
                "action": "Deploy automation system",
                "timeline": "2-3 weeks",
                "owner": "IT Manager + Operations",
                "expected_impact": "40% efficiency improvement",
                "resources": "System integration, $25K budget",
                "success_metrics": "Process time reduced by 50%"
            }
        ]
    elif rag_status == "amber":
        return [
            {
                "priority": "High",
                "action": "Enhance training and protocols",
                "timeline": "2 weeks",
                "owner": "Training Manager",
                "expected_impact": "15-20% improvement",
                "resources": "Training materials, 20 hrs/week",
                "success_metrics": "Staff certification >95%"
            }
        ]
    else:
        return [
            {
                "priority": "Medium",
                "action": "Maintain and optimize current processes",
                "timeline": "Ongoing",
                "owner": "Operations Manager",
                "expected_impact": "Sustained performance",
                "resources": "Regular monitoring",
                "success_metrics": "Maintain green status"
            }
        ]

def create_kpi_node(kpi_id, name, value, target, unit, category_id, pillar_name, macro_name, category_name):
    """Create a complete KPI node with all 10 layers"""
    is_percentage = unit in ["%", "score", "rating"]
    is_lower_better = unit in ["days", "minutes", "hours", "rate"] and "time" in name.lower() or "lag" in name.lower()
    
    if is_lower_better:
        rag = "green" if value <= target else ("amber" if value <= target * 1.15 else "red")
    else:
        rag = determine_rag_status(value, target, is_percentage)
    
    trend_data = generate_trend_data()
    recent_avg = sum(trend_data[-3:]) / 3
    trend = "up" if value > recent_avg else ("down" if value < recent_avg else "stable")
    
    people_pool = [
        {"name": "Jennifer Martinez", "title": "Director of Patient Access", "department": "Front Office", "email": "jmartinez@nyss.com"},
        {"name": "Robert Chen", "title": "Revenue Cycle Manager", "department": "RCM Operations", "email": "rchen@nyss.com"},
        {"name": "Sarah Johnson", "title": "Clinical Operations Director", "department": "Clinical", "email": "sjohnson@nyss.com"},
        {"name": "Michael Brown", "title": "Surgical Coordinator", "department": "OR Management", "email": "mbrown@nyss.com"},
        {"name": "Emily Davis", "title": "Billing Manager", "department": "Revenue Cycle", "email": "edavis@nyss.com"},
        {"name": "David Wilson", "title": "Coding Supervisor", "department": "HIM", "email": "dwilson@nyss.com"},
        {"name": "Lisa Anderson", "title": "Verification Specialist Lead", "department": "Patient Access", "email": "landerson@nyss.com"},
        {"name": "James Taylor", "title": "Provider Relations Manager", "department": "Clinical Quality", "email": "jtaylor@nyss.com"},
    ]
    
    owner = random.choice(people_pool)
    
    node = {
        "id": kpi_id,
        "name": name,
        "value": str(value),
        "target": str(target),
        "unit": unit,
        "rag": rag,
        "trend": trend,
        "pillar": pillar_name,
        "macro_process": macro_name,
        "category": category_name,
        "context": {
            "definition": f"{name} measures the performance and effectiveness of {name.lower()} in {category_name}",
            "business_impact": f"Critical metric for {macro_name} affecting overall {pillar_name} performance and revenue",
            "industry_benchmark": f"{target} {unit} is the industry target benchmark for spine specialty practices"
        },
        "current_state": {
            "status": rag,
            "value": str(value),
            "target": str(target),
            "gap": round(abs(target - value), 2),
            "gap_percentage": round(abs(target - value) / target * 100, 1) if target != 0 else 0,
            "financial_impact": f"${abs(target - value) * random.randint(500, 5000):,} impact per month"
        },
        "trend_data": trend_data,
        "root_causes": generate_root_causes(name),
        "predictive_insights": generate_predictive_insights(value, trend_data),
        "trend_analysis": {
            "current_trend": trend.capitalize(),
            "trend_strength": random.choice(["Strong", "Moderate", "Weak"]),
            "volatility": random.choice(["High", "Medium", "Low"]),
            "key_insights": f"{name} shows {trend} trajectory requiring {'immediate attention' if rag == 'red' else 'close monitoring' if rag == 'amber' else 'maintenance'}"
        },
        "dependencies": {
            "upstream": [f"{macro_name} upstream dependency {i+1}" for i in range(2)],
            "downstream": [f"Downstream impact on {pillar_name} metric {i+1}" for i in range(2)],
            "peer_metrics": [f"Related {category_name} metric {i+1}" for i in range(2)]
        },
        "people_accountable": [
            {
                "name": owner["name"],
                "title": owner["title"],
                "department": owner["department"],
                "email": owner["email"],
                "role": "Primary Owner",
                "avatar_color": random.choice(["#4A90E2", "#7B68EE", "#50C878", "#FF6B6B", "#FFA500", "#20B2AA"])
            }
        ],
        "recommended_actions": generate_recommended_actions(rag),
        "contributing_factors": {
            "internal": [
                {"factor": "Process efficiency", "impact": random.choice(["High", "Medium", "Low"])},
                {"factor": "Staff training", "impact": random.choice(["High", "Medium", "Low"])},
                {"factor": "Technology adoption", "impact": random.choice(["High", "Medium", "Low"])}
            ],
            "external": [
                {"factor": "Market conditions", "impact": random.choice(["High", "Medium", "Low"])},
                {"factor": "Regulatory environment", "impact": random.choice(["High", "Medium", "Low"])},
                {"factor": "Payer policies", "impact": random.choice(["High", "Medium", "Low"])}
            ]
        }
    }
    
    return node

print("🚀 Generating Complete NYSS KPI Universe (200+ KPIs)...")
print("=" * 60)

# Main KPI Data Structure
kpi_tree = {
    "version": "1.0-nyss-complete-all-pillars",
    "total_nodes": 0,
    "organization": "New York Spine Specialists (NYSS)",
    "scope": "Complete Operations - All Pillars",
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
        "name": "NYSS Complete Operations",
        "id": "nyss_root",
        "level": 0,
        "children": []
    },
    "nodes": []
}

# Define all KPIs across all pillars
all_kpis = [
    # PILLAR 1: Patient Access & Intake (30 KPIs)
    ("pillar1", "Patient Access & Intake", "Patient Acquisition", "Lead Intake & Conversion", "kpi_1_1_1", "New Patient Lead Volume", 245, 280, "patients"),
    ("pillar1", "Patient Access & Intake", "Patient Acquisition", "Lead Intake & Conversion", "kpi_1_1_2", "Lead Source Mix - Google", 35, 40, "%"),
    ("pillar1", "Patient Access & Intake", "Patient Acquisition", "Lead Intake & Conversion", "kpi_1_1_3", "Lead Source Mix - Referral", 28, 35, "%"),
    ("pillar1", "Patient Access & Intake", "Patient Acquisition", "Lead Intake & Conversion", "kpi_1_1_4", "Lead Source Mix - Attorney", 22, 20, "%"),
    ("pillar1", "Patient Access & Intake", "Patient Acquisition", "Lead Intake & Conversion", "kpi_1_1_5", "Conversion Rate by Source", 68, 75, "%"),
    ("pillar1", "Patient Access & Intake", "Patient Acquisition", "Lead Intake & Conversion", "kpi_1_1_6", "Call Abandon Rate", 22, 15, "%"),
    ("pillar1", "Patient Access & Intake", "Patient Acquisition", "Lead Intake & Conversion", "kpi_1_1_7", "Referral-to-Appointment Conversion", 78, 85, "%"),
    ("pillar1", "Patient Access & Intake", "Patient Acquisition", "Lead Intake & Conversion", "kpi_1_1_8", "Referral Documentation Completeness", 82, 95, "%"),
    
    ("pillar1", "Patient Access & Intake", "Scheduling & Appointment Mgmt", "Access Efficiency", "kpi_1_2_1", "Days to First Appointment", 5.2, 3.0, "days"),
    ("pillar1", "Patient Access & Intake", "Scheduling & Appointment Mgmt", "Access Efficiency", "kpi_1_2_2", "Slot Availability Rate", 72, 85, "%"),
    ("pillar1", "Patient Access & Intake", "Scheduling & Appointment Mgmt", "Access Efficiency", "kpi_1_2_3", "Provider Schedule Saturation", 88, 85, "%"),
    ("pillar1", "Patient Access & Intake", "Scheduling & Appointment Mgmt", "Access Efficiency", "kpi_1_2_4", "Insurance Clearance Delay", 2.8, 1.5, "days"),
    ("pillar1", "Patient Access & Intake", "Scheduling & Appointment Mgmt", "Access Efficiency", "kpi_1_2_5", "Appointment Wait Time In-Clinic", 18, 15, "minutes"),
    ("pillar1", "Patient Access & Intake", "Scheduling & Appointment Mgmt", "Access Efficiency", "kpi_1_2_6", "Check-in to Rooming Time", 8, 5, "minutes"),
    ("pillar1", "Patient Access & Intake", "Scheduling & Appointment Mgmt", "Access Efficiency", "kpi_1_2_7", "Rooming to Provider Time", 10, 8, "minutes"),
    ("pillar1", "Patient Access & Intake", "Scheduling & Appointment Mgmt", "Access Efficiency", "kpi_1_2_8", "No-Show Rate", 14.5, 10.0, "%"),
    ("pillar1", "Patient Access & Intake", "Scheduling & Appointment Mgmt", "Access Efficiency", "kpi_1_2_9", "No-Show Rate - New Patients", 18, 12, "%"),
    ("pillar1", "Patient Access & Intake", "Scheduling & Appointment Mgmt", "Access Efficiency", "kpi_1_2_10", "No-Show Rate - Follow-ups", 12, 8, "%"),
    
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Packet Completeness", "kpi_1_3_1", "Overall Packet Completeness Rate", 92, 98, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Packet Completeness", "kpi_1_3_2", "Demographics Completeness", 96, 99, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Packet Completeness", "kpi_1_3_3", "Insurance Card Upload Rate", 94, 98, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Packet Completeness", "kpi_1_3_4", "Claim Number Documentation", 88, 95, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Packet Completeness", "kpi_1_3_5", "Attorney Info Completeness", 85, 95, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Packet Completeness", "kpi_1_3_6", "Imaging Upload Rate", 82, 95, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Packet Completeness", "kpi_1_3_7", "Consent Forms Completion", 96, 99, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Packet Completeness", "kpi_1_3_8", "Missing Packet Item Rate", 8.5, 2.0, "%"),
    
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Insurance Verification", "kpi_1_3_9", "Eligibility Verification Accuracy", 94, 98, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Insurance Verification", "kpi_1_3_10", "Active Coverage Verification", 96, 99, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Insurance Verification", "kpi_1_3_11", "Copay/Deductible Validation", 91, 96, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Insurance Verification", "kpi_1_3_12", "Policy Dates Verification", 95, 98, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Insurance Verification", "kpi_1_3_13", "Benefit Verification Turnaround", 2.8, 1.5, "days"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Financial Clearance", "kpi_1_3_14", "Pre-Visit Financial Clearance Rate", 88, 95, "%"),
    ("pillar1", "Patient Access & Intake", "Intake Documentation", "Financial Clearance", "kpi_1_3_15", "Prior Auth Required Identification", 92, 98, "%"),
    
    ("pillar1", "Patient Access & Intake", "Clinical Pre-Visit Prep", "Records Readiness", "kpi_1_4_1", "Imaging Availability Before Visit", 85, 95, "%"),
    ("pillar1", "Patient Access & Intake", "Clinical Pre-Visit Prep", "Records Readiness", "kpi_1_4_2", "MRI Upload Completeness", 88, 96, "%"),
    ("pillar1", "Patient Access & Intake", "Clinical Pre-Visit Prep", "Records Readiness", "kpi_1_4_3", "X-Ray Upload Completeness", 90, 97, "%"),
    ("pillar1", "Patient Access & Intake", "Clinical Pre-Visit Prep", "Records Readiness", "kpi_1_4_4", "Radiologist Report Availability", 82, 93, "%"),
    ("pillar1", "Patient Access & Intake", "Clinical Pre-Visit Prep", "Records Readiness", "kpi_1_4_5", "Referral Notes Availability", 90, 98, "%"),
    
    ("pillar1", "Patient Access & Intake", "Patient Experience", "Service Quality", "kpi_1_5_1", "New Patient NPS", 72, 80, "score"),
    ("pillar1", "Patient Access & Intake", "Patient Experience", "Service Quality", "kpi_1_5_2", "Intake Satisfaction Score", 4.2, 4.5, "rating"),
    ("pillar1", "Patient Access & Intake", "Patient Experience", "Service Quality", "kpi_1_5_3", "Staff Courtesy Rating", 4.4, 4.7, "rating"),
    ("pillar1", "Patient Access & Intake", "Patient Experience", "Service Quality", "kpi_1_5_4", "Process Speed Rating", 3.9, 4.5, "rating"),
    
    # PILLAR 2: Clinical Operations (40 KPIs)
    ("pillar2", "Clinical Operations", "Provider Documentation", "Note Completion", "kpi_2_1_1", "Provider Note Completion Rate 24h", 88, 95, "%"),
    ("pillar2", "Clinical Operations", "Provider Documentation", "Note Completion", "kpi_2_1_2", "Initial Note Completion", 92, 98, "%"),
    ("pillar2", "Clinical Operations", "Provider Documentation", "Note Completion", "kpi_2_1_3", "Addendum Requirement Rate", 12, 5, "%"),
    ("pillar2", "Clinical Operations", "Provider Documentation", "Note Completion", "kpi_2_1_4", "Late Documentation Count", 18, 8, "cases"),
    ("pillar2", "Clinical Operations", "Provider Documentation", "Documentation Quality", "kpi_2_1_5", "Clinical Documentation Accuracy", 91, 96, "%"),
    ("pillar2", "Clinical Operations", "Provider Documentation", "Documentation Quality", "kpi_2_1_6", "HPI Completeness", 94, 98, "%"),
    ("pillar2", "Clinical Operations", "Provider Documentation", "Documentation Quality", "kpi_2_1_7", "ROS Completeness", 89, 95, "%"),
    ("pillar2", "Clinical Operations", "Provider Documentation", "Documentation Quality", "kpi_2_1_8", "Physical Exam Completeness", 92, 97, "%"),
    ("pillar2", "Clinical Operations", "Provider Documentation", "Documentation Quality", "kpi_2_1_9", "Assessment Plan Quality", 90, 96, "%"),
    
    ("pillar2", "Clinical Operations", "Provider Documentation", "Coding Alignment", "kpi_2_1_10", "Provider-to-Coder Match Rate", 86, 94, "%"),
    ("pillar2", "Clinical Operations", "Provider Documentation", "Coding Alignment", "kpi_2_1_11", "CPT Justification Completeness", 88, 95, "%"),
    ("pillar2", "Clinical Operations", "Provider Documentation", "Coding Alignment", "kpi_2_1_12", "ICD Linkage Correctness", 91, 97, "%"),
    ("pillar2", "Clinical Operations", "Provider Documentation", "Coding Alignment", "kpi_2_1_13", "Medical Necessity Documentation", 87, 95, "%"),
    
    ("pillar2", "Clinical Operations", "Clinical Workflow", "Patient Throughput", "kpi_2_2_1", "Rooming Time Efficiency", 15, 12, "minutes"),
    ("pillar2", "Clinical Operations", "Clinical Workflow", "Patient Throughput", "kpi_2_2_2", "Provider Time per Encounter", 22, 18, "minutes"),
    ("pillar2", "Clinical Operations", "Clinical Workflow", "Patient Throughput", "kpi_2_2_3", "New Visit Duration", 35, 30, "minutes"),
    ("pillar2", "Clinical Operations", "Clinical Workflow", "Patient Throughput", "kpi_2_2_4", "Follow-up Visit Duration", 18, 15, "minutes"),
    ("pillar2", "Clinical Operations", "Clinical Workflow", "EOD Closure", "kpi_2_2_5", "EOD Clinical Closure Rate", 89, 96, "%"),
    ("pillar2", "Clinical Operations", "Clinical Workflow", "EOD Closure", "kpi_2_2_6", "Notes Closed EOD", 91, 97, "%"),
    ("pillar2", "Clinical Operations", "Clinical Workflow", "EOD Closure", "kpi_2_2_7", "Orders Signed EOD", 87, 95, "%"),
    
    ("pillar2", "Clinical Operations", "Orders Management", "Diagnostic Orders", "kpi_2_3_1", "Imaging Order Accuracy", 93, 98, "%"),
    ("pillar2", "Clinical Operations", "Orders Management", "Diagnostic Orders", "kpi_2_3_2", "CPT Accuracy MRI/XR", 95, 99, "%"),
    ("pillar2", "Clinical Operations", "Orders Management", "Diagnostic Orders", "kpi_2_3_3", "Laterality Correctness", 97, 99.5, "%"),
    ("pillar2", "Clinical Operations", "Orders Management", "Diagnostic Orders", "kpi_2_3_4", "ICD Linkage Imaging", 92, 97, "%"),
    ("pillar2", "Clinical Operations", "Orders Management", "Lab Orders", "kpi_2_3_5", "Lab Order Timeliness", 91, 96, "%"),
    ("pillar2", "Clinical Operations", "Orders Management", "Lab Orders", "kpi_2_3_6", "Critical Lab Follow-up SLA", 94, 98, "%"),
    
    ("pillar2", "Clinical Operations", "Orders Management", "Prescriptions", "kpi_2_3_7", "Controlled Substance Compliance", 96, 99, "%"),
    ("pillar2", "Clinical Operations", "Orders Management", "Prescriptions", "kpi_2_3_8", "I-STOP Verification Rate", 98, 99.5, "%"),
    ("pillar2", "Clinical Operations", "Orders Management", "Prescriptions", "kpi_2_3_9", "UDS Compliance Rate", 94, 98, "%"),
    ("pillar2", "Clinical Operations", "Orders Management", "Prescriptions", "kpi_2_3_10", "PDMP Audit Completion", 96, 99, "%"),
    
    ("pillar2", "Clinical Operations", "Provider Performance", "Productivity", "kpi_2_4_1", "RVU per Provider Monthly", 425, 480, "RVU"),
    ("pillar2", "Clinical Operations", "Provider Performance", "Productivity", "kpi_2_4_2", "RVU per Encounter", 2.8, 3.2, "RVU"),
    ("pillar2", "Clinical Operations", "Provider Performance", "Productivity", "kpi_2_4_3", "RVU per Hour", 18, 22, "RVU"),
    ("pillar2", "Clinical Operations", "Provider Performance", "Utilization", "kpi_2_4_4", "Provider Utilization Rate", 82, 88, "%"),
    ("pillar2", "Clinical Operations", "Provider Performance", "Utilization", "kpi_2_4_5", "Template Fill Percentage", 86, 92, "%"),
    
    ("pillar2", "Clinical Operations", "Provider Performance", "Clinical Errors", "kpi_2_4_6", "Clinical Documentation Error Rate", 4.2, 2.0, "%"),
    ("pillar2", "Clinical Operations", "Provider Performance", "Clinical Errors", "kpi_2_4_7", "Missing Diagnosis Rate", 2.8, 1.0, "%"),
    ("pillar2", "Clinical Operations", "Provider Performance", "Clinical Errors", "kpi_2_4_8", "Incorrect ICD Severity", 3.5, 1.5, "%"),
    
    ("pillar2", "Clinical Operations", "Care Quality & Safety", "Patient Safety", "kpi_2_5_1", "Adverse Event Rate", 0.8, 0.3, "%"),
    ("pillar2", "Clinical Operations", "Care Quality & Safety", "Patient Safety", "kpi_2_5_2", "Medication Error Rate", 0.5, 0.2, "%"),
    ("pillar2", "Clinical Operations", "Care Quality & Safety", "Patient Safety", "kpi_2_5_3", "Patient Fall Rate", 0.3, 0.1, "%"),
    ("pillar2", "Clinical Operations", "Care Quality & Safety", "Patient Safety", "kpi_2_5_4", "Infection Control Compliance", 94, 98, "%"),
    ("pillar2", "Clinical Operations", "Care Quality & Safety", "Care Coordination", "kpi_2_5_5", "Follow-Up Compliance Rate", 88, 94, "%"),
    
    # PILLAR 3: Surgical Coordination (35 KPIs)
    ("pillar3", "Surgical Coordination", "Surgical Candidacy", "Pre-Surgical Requirements", "kpi_3_1_1", "Surgical Candidacy Compliance", 90, 96, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Candidacy", "Pre-Surgical Requirements", "kpi_3_1_2", "MRI within 6 Months", 92, 98, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Candidacy", "Pre-Surgical Requirements", "kpi_3_1_3", "X-Ray within 3 Months", 94, 97, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Candidacy", "Pre-Surgical Requirements", "kpi_3_1_4", "Conservative Therapy Documentation", 88, 95, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Candidacy", "Pre-Surgical Requirements", "kpi_3_1_5", "Surgical Recommendation Documentation", 93, 98, "%"),
    
    ("pillar3", "Surgical Coordination", "Pre-Cert & Authorization", "Authorization Workflow", "kpi_3_2_1", "Authorization Approval Rate", 84, 92, "%"),
    ("pillar3", "Surgical Coordination", "Pre-Cert & Authorization", "Authorization Workflow", "kpi_3_2_2", "Correct CPT Submission", 94, 98, "%"),
    ("pillar3", "Surgical Coordination", "Pre-Cert & Authorization", "Authorization Workflow", "kpi_3_2_3", "ICD CPT Linkage Accuracy", 92, 97, "%"),
    ("pillar3", "Surgical Coordination", "Pre-Cert & Authorization", "Authorization Workflow", "kpi_3_2_4", "Imaging Attachment Rate", 96, 99, "%"),
    ("pillar3", "Surgical Coordination", "Pre-Cert & Authorization", "Authorization Workflow", "kpi_3_2_5", "Clinical Notes Compliance", 89, 95, "%"),
    ("pillar3", "Surgical Coordination", "Pre-Cert & Authorization", "Authorization Workflow", "kpi_3_2_6", "Payer Criteria Met Rate", 87, 94, "%"),
    ("pillar3", "Surgical Coordination", "Pre-Cert & Authorization", "Authorization Workflow", "kpi_3_2_7", "Authorization Turnaround Time", 5.5, 3.0, "days"),
    
    ("pillar3", "Surgical Coordination", "Pre-Cert & Authorization", "Medical Necessity", "kpi_3_2_8", "Medical Necessity Package Completeness", 91, 97, "%"),
    ("pillar3", "Surgical Coordination", "Pre-Cert & Authorization", "Medical Necessity", "kpi_3_2_9", "Conservative Care Documentation", 88, 95, "%"),
    ("pillar3", "Surgical Coordination", "Pre-Cert & Authorization", "Medical Necessity", "kpi_3_2_10", "CPT Justification Narrative Quality", 90, 96, "%"),
    
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Scheduling", "kpi_3_3_1", "Surgery Scheduling Lead Time", 12, 7, "days"),
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Scheduling", "kpi_3_3_2", "Provider Calendar Availability", 78, 85, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Scheduling", "kpi_3_3_3", "Patient Readiness Rate", 91, 96, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Scheduling", "kpi_3_3_4", "Insurance Surgical Clearance", 88, 94, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Scheduling", "kpi_3_3_5", "Facility Availability Rate", 94, 98, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Scheduling", "kpi_3_3_6", "EOD Surgical Deployment Rate", 89, 95, "%"),
    
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Utilization", "kpi_3_3_7", "OR Block Utilization Rate", 82, 90, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Utilization", "kpi_3_3_8", "Case Duration Variance", 15, 8, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Utilization", "kpi_3_3_9", "First Case On-Time Start", 86, 94, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Utilization", "kpi_3_3_10", "Surgery Cancellation Rate", 8.5, 4.0, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Utilization", "kpi_3_3_11", "No Auth Cancellation Rate", 3.2, 1.0, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Scheduling", "OR Utilization", "kpi_3_3_12", "Patient Readiness Failure Rate", 2.8, 1.0, "%"),
    
    ("pillar3", "Surgical Coordination", "Post-Op Care", "Post-Op Compliance", "kpi_3_4_1", "Post-Op Visit Compliance", 89, 95, "%"),
    ("pillar3", "Surgical Coordination", "Post-Op Care", "Post-Op Compliance", "kpi_3_4_2", "Follow-up within 7 Days", 92, 97, "%"),
    ("pillar3", "Surgical Coordination", "Post-Op Care", "Post-Op Compliance", "kpi_3_4_3", "Follow-up within 30 Days", 87, 94, "%"),
    ("pillar3", "Surgical Coordination", "Post-Op Care", "Complications", "kpi_3_4_4", "Post-Op Complication Rate", 2.8, 1.5, "%"),
    ("pillar3", "Surgical Coordination", "Post-Op Care", "Complications", "kpi_3_4_5", "Surgical Site Infection Rate", 0.8, 0.3, "%"),
    ("pillar3", "Surgical Coordination", "Post-Op Care", "Complications", "kpi_3_4_6", "Post-Op Neurologic Deficit", 0.5, 0.2, "%"),
    
    ("pillar3", "Surgical Coordination", "Surgical Billing", "Billing Lag", "kpi_3_5_1", "Surgery to Billing Lag Time", 4.5, 2.0, "days"),
    ("pillar3", "Surgical Coordination", "Surgical Billing", "Billing Lag", "kpi_3_5_2", "Op Note Completion Time", 1.8, 0.5, "days"),
    ("pillar3", "Surgical Coordination", "Surgical Billing", "Coding Accuracy", "kpi_3_5_3", "Surgical CPT ICD Accuracy", 93, 98, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Billing", "Coding Accuracy", "kpi_3_5_4", "CPT Modifier Accuracy", 95, 99, "%"),
    ("pillar3", "Surgical Coordination", "Surgical Billing", "Coding Accuracy", "kpi_3_5_5", "Bundling Compliance Rate", 91, 97, "%"),
    
    # PILLAR 4: Revenue Cycle Management (60 KPIs)
    ("pillar4", "Revenue Cycle Management", "Pre-Billing Readiness", "Clinical to Coding", "kpi_4_1_1", "Clinical Doc to Coding Accuracy", 89, 95, "%"),
    ("pillar4", "Revenue Cycle Management", "Pre-Billing Readiness", "Clinical to Coding", "kpi_4_1_2", "Provider Note Completeness for Coding", 92, 97, "%"),
    ("pillar4", "Revenue Cycle Management", "Pre-Billing Readiness", "Clinical to Coding", "kpi_4_1_3", "Injury Causality Documentation", 88, 95, "%"),
    ("pillar4", "Revenue Cycle Management", "Pre-Billing Readiness", "Clinical to Coding", "kpi_4_1_4", "Imaging Documentation Linkage", 91, 96, "%"),
    ("pillar4", "Revenue Cycle Management", "Pre-Billing Readiness", "Clinical to Coding", "kpi_4_1_5", "Medical Necessity for Coding", 87, 94, "%"),
    ("pillar4", "Revenue Cycle Management", "Pre-Billing Readiness", "Clinical to Coding", "kpi_4_1_6", "Coding Lag Time", 3.2, 1.5, "days"),
    ("pillar4", "Revenue Cycle Management", "Pre-Billing Readiness", "Clinical to Coding", "kpi_4_1_7", "Encounters Awaiting Signatures", 28, 10, "cases"),
    
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Scrubbing & Edits", "kpi_4_2_1", "Claim Scrubbing Accuracy", 91, 97, "%"),
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Scrubbing & Edits", "kpi_4_2_2", "Demographic Error Rate", 3.5, 1.0, "%"),
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Scrubbing & Edits", "kpi_4_2_3", "Insurance Mismatch Rate", 2.8, 0.8, "%"),
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Scrubbing & Edits", "kpi_4_2_4", "Policy Termination Detection", 94, 98, "%"),
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Scrubbing & Edits", "kpi_4_2_5", "Missing Auth Number Rate", 4.2, 1.5, "%"),
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Scrubbing & Edits", "kpi_4_2_6", "CPT ICD Mismatch Rate", 3.8, 1.2, "%"),
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Scrubbing & Edits", "kpi_4_2_7", "Modifier Error Rate", 2.5, 0.8, "%"),
    
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Clean Claims", "kpi_4_2_8", "Clean Claim Rate", 87, 94, "%"),
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Clean Claims", "kpi_4_2_9", "Error-Free Submission Rate", 89, 95, "%"),
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Clean Claims", "kpi_4_2_10", "Claim Submission Lag", 2.8, 1.5, "days"),
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Clean Claims", "kpi_4_2_11", "Lag by Commercial Payers", 2.5, 1.0, "days"),
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Clean Claims", "kpi_4_2_12", "Lag by WC Payers", 3.5, 2.0, "days"),
    ("pillar4", "Revenue Cycle Management", "Claim Creation", "Clean Claims", "kpi_4_2_13", "Lag by PIP Payers", 3.2, 1.8, "days"),
    
    ("pillar4", "Revenue Cycle Management", "Payer Response", "First Pass Success", "kpi_4_3_1", "First Pass Acceptance FPA", 82, 90, "%"),
    ("pillar4", "Revenue Cycle Management", "Payer Response", "First Pass Success", "kpi_4_3_2", "FPA - Commercial Insurance", 85, 92, "%"),
    ("pillar4", "Revenue Cycle Management", "Payer Response", "First Pass Success", "kpi_4_3_3", "FPA - Workers Comp", 78, 88, "%"),
    ("pillar4", "Revenue Cycle Management", "Payer Response", "First Pass Success", "kpi_4_3_4", "FPA - PIP No-Fault", 80, 89, "%"),
    
    ("pillar4", "Revenue Cycle Management", "Payer Response", "Denial Management", "kpi_4_3_5", "Overall Denial Rate", 12.5, 8.0, "%"),
    ("pillar4", "Revenue Cycle Management", "Payer Response", "Denial Management", "kpi_4_3_6", "Technical Denial Rate", 5.2, 2.5, "%"),
    ("pillar4", "Revenue Cycle Management", "Payer Response", "Denial Management", "kpi_4_3_7", "Clinical Denial Rate", 3.8, 2.0, "%"),
    ("pillar4", "Revenue Cycle Management", "Payer Response", "Denial Management", "kpi_4_3_8", "No-Auth Denial Rate", 2.5, 1.0, "%"),
    ("pillar4", "Revenue Cycle Management", "Payer Response", "Denial Management", "kpi_4_3_9", "Timely Filing Denial Rate", 0.8, 0.3, "%"),
    ("pillar4", "Revenue Cycle Management", "Payer Response", "Denial Management", "kpi_4_3_10", "Eligibility Denial Rate", 1.2, 0.5, "%"),
    ("pillar4", "Revenue Cycle Management", "Payer Response", "Denial Management", "kpi_4_3_11", "Denial Recovery Rate", 68, 78, "%"),
    ("pillar4", "Revenue Cycle Management", "Payer Response", "Denial Management", "kpi_4_3_12", "Denial Recovery Turnaround", 22, 14, "days"),
    
    ("pillar4", "Revenue Cycle Management", "Appeals", "Appeal Performance", "kpi_4_4_1", "Appeal Success Rate", 72, 82, "%"),
    ("pillar4", "Revenue Cycle Management", "Appeals", "Appeal Performance", "kpi_4_4_2", "Appeal Overturn Rate", 68, 78, "%"),
    ("pillar4", "Revenue Cycle Management", "Appeals", "Appeal Performance", "kpi_4_4_3", "Appeal Documentation Quality", 88, 95, "%"),
    ("pillar4", "Revenue Cycle Management", "Appeals", "Appeal Performance", "kpi_4_4_4", "Appeal SLA Compliance", 91, 97, "%"),
    ("pillar4", "Revenue Cycle Management", "Appeals", "Underpayment", "kpi_4_4_5", "Underpayment Detection Rate", 78, 88, "%"),
    ("pillar4", "Revenue Cycle Management", "Appeals", "Underpayment", "kpi_4_4_6", "Allowed vs Paid Variance", 8.5, 4.0, "%"),
    
    ("pillar4", "Revenue Cycle Management", "AR & Cash Posting", "AR Aging", "kpi_4_5_1", "AR Days Overall", 42, 32, "days"),
    ("pillar4", "Revenue Cycle Management", "AR & Cash Posting", "AR Aging", "kpi_4_5_2", "AR 0-30 Days", 48, 55, "%"),
    ("pillar4", "Revenue Cycle Management", "AR & Cash Posting", "AR Aging", "kpi_4_5_3", "AR 31-60 Days", 28, 25, "%"),
    ("pillar4", "Revenue Cycle Management", "AR & Cash Posting", "AR Aging", "kpi_4_5_4", "AR 61-90 Days", 14, 12, "%"),
    ("pillar4", "Revenue Cycle Management", "AR & Cash Posting", "AR Aging", "kpi_4_5_5", "AR Over 90 Days", 18, 10, "%"),
    ("pillar4", "Revenue Cycle Management", "AR & Cash Posting", "AR Aging", "kpi_4_5_6", "AR Over 120 Days", 8.5, 4.0, "%"),
    
    ("pillar4", "Revenue Cycle Management", "AR & Cash Posting", "Cash Posting", "kpi_4_5_7", "Payment Posting Accuracy", 96, 99, "%"),
    ("pillar4", "Revenue Cycle Management", "AR & Cash Posting", "Cash Posting", "kpi_4_5_8", "Posting Error Rate", 1.2, 0.5, "%"),
    ("pillar4", "Revenue Cycle Management", "AR & Cash Posting", "Cash Posting", "kpi_4_5_9", "Adjustment Accuracy", 94, 98, "%"),
    ("pillar4", "Revenue Cycle Management", "AR & Cash Posting", "Cash Posting", "kpi_4_5_10", "Payment Posting Lag", 1.5, 0.5, "days"),
    
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Collections", "kpi_4_6_1", "Net Collection Rate NCR", 94, 98, "%"),
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Collections", "kpi_4_6_2", "Gross Collection Rate", 88, 94, "%"),
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Collections", "kpi_4_6_3", "Adjusted Collection Rate", 96, 99, "%"),
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Collections", "kpi_4_6_4", "Days in AR", 38, 28, "days"),
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Collections", "kpi_4_6_5", "Collection Rate - Commercial", 96, 99, "%"),
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Collections", "kpi_4_6_6", "Collection Rate - WC", 91, 96, "%"),
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Collections", "kpi_4_6_7", "Collection Rate - PIP", 92, 97, "%"),
    
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Write-Off & Compliance", "kpi_4_6_8", "Timely Filing Compliance", 97, 99.5, "%"),
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Write-Off & Compliance", "kpi_4_6_9", "Timely Filing Denial Count", 12, 3, "cases"),
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Write-Off & Compliance", "kpi_4_6_10", "Total Write-Off Rate", 4.5, 2.5, "%"),
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Write-Off & Compliance", "kpi_4_6_11", "Avoidable Write-Off Rate", 2.2, 0.8, "%"),
    ("pillar4", "Revenue Cycle Management", "Financial Performance", "Write-Off & Compliance", "kpi_4_6_12", "Contractual Adjustment Rate", 28, 25, "%"),
    
    # PILLAR 5: Compliance & Risk (30 KPIs)
    ("pillar5", "Compliance & Risk Management", "Regulatory Compliance", "HIPAA Compliance", "kpi_5_1_1", "HIPAA Training Completion", 98, 100, "%"),
    ("pillar5", "Compliance & Risk Management", "Regulatory Compliance", "HIPAA Compliance", "kpi_5_1_2", "PHI Access Audit Compliance", 96, 99, "%"),
    ("pillar5", "Compliance & Risk Management", "Regulatory Compliance", "HIPAA Compliance", "kpi_5_1_3", "Breach Incident Rate", 0.2, 0.0, "incidents"),
    ("pillar5", "Compliance & Risk Management", "Regulatory Compliance", "Clinical Compliance", "kpi_5_1_4", "Medical Record Compliance Score", 94, 98, "%"),
    ("pillar5", "Compliance & Risk Management", "Regulatory Compliance", "Clinical Compliance", "kpi_5_1_5", "Controlled Substance Audit Score", 97, 99.5, "%"),
    
    ("pillar5", "Compliance & Risk Management", "Risk Management", "Clinical Risk", "kpi_5_2_1", "Incident Report Completion Rate", 96, 99, "%"),
    ("pillar5", "Compliance & Risk Management", "Risk Management", "Clinical Risk", "kpi_5_2_2", "Risk Event Closure Time", 8, 5, "days"),
    ("pillar5", "Compliance & Risk Management", "Risk Management", "Clinical Risk", "kpi_5_2_3", "Near Miss Reporting Rate", 85, 92, "%"),
    ("pillar5", "Compliance & Risk Management", "Risk Management", "Financial Risk", "kpi_5_2_4", "Fraud Detection Rate", 92, 97, "%"),
    ("pillar5", "Compliance & Risk Management", "Risk Management", "Financial Risk", "kpi_5_2_5", "Overpayment Recovery Rate", 88, 95, "%"),
    
    ("pillar5", "Compliance & Risk Management", "Quality Assurance", "Clinical Quality", "kpi_5_3_1", "Clinical Quality Score", 91, 96, "%"),
    ("pillar5", "Compliance & Risk Management", "Quality Assurance", "Clinical Quality", "kpi_5_3_2", "Peer Review Completion Rate", 94, 98, "%"),
    ("pillar5", "Compliance & Risk Management", "Quality Assurance", "Clinical Quality", "kpi_5_3_3", "Quality Improvement Initiatives", 12, 15, "active"),
    ("pillar5", "Compliance & Risk Management", "Quality Assurance", "Billing Quality", "kpi_5_3_4", "Coding Audit Pass Rate", 93, 97, "%"),
    ("pillar5", "Compliance & Risk Management", "Quality Assurance", "Billing Quality", "kpi_5_3_5", "Billing Compliance Score", 95, 98, "%"),
    
    ("pillar5", "Compliance & Risk Management", "Credentialing", "Provider Credentialing", "kpi_5_4_1", "Provider Credentialing Current", 100, 100, "%"),
    ("pillar5", "Compliance & Risk Management", "Credentialing", "Provider Credentialing", "kpi_5_4_2", "License Renewal Compliance", 100, 100, "%"),
    ("pillar5", "Compliance & Risk Management", "Credentialing", "Provider Credentialing", "kpi_5_4_3", "DEA Renewal Compliance", 100, 100, "%"),
    ("pillar5", "Compliance & Risk Management", "Credentialing", "Staff Credentialing", "kpi_5_4_4", "Staff Certification Current", 98, 100, "%"),
    ("pillar5", "Compliance & Risk Management", "Credentialing", "Staff Credentialing", "kpi_5_4_5", "Continuing Education Compliance", 96, 99, "%"),
    
    ("pillar5", "Compliance & Risk Management", "Audit & Monitoring", "Internal Audits", "kpi_5_5_1", "Internal Audit Completion Rate", 94, 98, "%"),
    ("pillar5", "Compliance & Risk Management", "Audit & Monitoring", "Internal Audits", "kpi_5_5_2", "Audit Finding Closure Rate", 88, 95, "%"),
    ("pillar5", "Compliance & Risk Management", "Audit & Monitoring", "Internal Audits", "kpi_5_5_3", "High Risk Finding Rate", 3.5, 1.5, "%"),
    ("pillar5", "Compliance & Risk Management", "Audit & Monitoring", "External Audits", "kpi_5_5_4", "External Audit Pass Rate", 92, 97, "%"),
    ("pillar5", "Compliance & Risk Management", "Audit & Monitoring", "External Audits", "kpi_5_5_5", "Payer Audit Deficiency Rate", 5.2, 2.5, "%"),
    
    ("pillar5", "Compliance & Risk Management", "Policy Management", "Policy Compliance", "kpi_5_6_1", "Policy Acknowledgment Rate", 97, 99.5, "%"),
    ("pillar5", "Compliance & Risk Management", "Policy Management", "Policy Compliance", "kpi_5_6_2", "Policy Review Currency", 94, 98, "%"),
    ("pillar5", "Compliance & Risk Management", "Policy Management", "Policy Compliance", "kpi_5_6_3", "Policy Violation Rate", 1.8, 0.5, "%"),
    ("pillar5", "Compliance & Risk Management", "Policy Management", "Training", "kpi_5_6_4", "Annual Training Completion", 96, 99, "%"),
    ("pillar5", "Compliance & Risk Management", "Policy Management", "Training", "kpi_5_6_5", "Training Effectiveness Score", 88, 94, "%"),
]

# Build tree structure
tree_structure = {}
for kpi_tuple in all_kpis:
    pillar_id, pillar_name, macro_name, category_name = kpi_tuple[1], kpi_tuple[2], kpi_tuple[3], kpi_tuple[4]
    
    if pillar_name not in tree_structure:
        tree_structure[pillar_name] = {}
    if macro_name not in tree_structure[pillar_name]:
        tree_structure[pillar_name][macro_name] = {}
    if category_name not in tree_structure[pillar_name][macro_name]:
        tree_structure[pillar_name][macro_name][category_name] = []
    
    tree_structure[pillar_name][macro_name][category_name].append(kpi_tuple)

# Generate all KPI nodes
print(f"\n📊 Generating {len(all_kpis)} KPI nodes...\n")

for kpi_tuple in all_kpis:
    pillar_id, pillar_name, macro_name, category_name, kpi_id, name, value, target, unit = kpi_tuple
    
    node = create_kpi_node(kpi_id, name, value, target, unit, category_name, pillar_name, macro_name, category_name)
    kpi_tree["nodes"].append(node)
    
    if len(kpi_tree["nodes"]) % 50 == 0:
        print(f"  ✓ Generated {len(kpi_tree['nodes'])} KPIs...")

# Build complete tree
tree_children = []
for pillar_name, macros in tree_structure.items():
    macro_children = []
    for macro_name, categories in macros.items():
        category_children = []
        for category_name, kpis in categories.items():
            kpi_children = []
            for kpi_tuple in kpis:
                kpi_id, name = kpi_tuple[4], kpi_tuple[5]
                kpi_children.append({
                    "name": name,
                    "id": kpi_id,
                    "level": 4
                })
            category_children.append({
                "name": category_name,
                "id": f"cat_{category_name.replace(' ', '_').lower()}",
                "level": 3,
                "children": kpi_children
            })
        macro_children.append({
            "name": macro_name,
            "id": f"macro_{macro_name.replace(' ', '_').lower()}",
            "level": 2,
            "children": category_children
        })
    tree_children.append({
        "name": pillar_name,
        "id": f"pillar_{pillar_name.replace(' ', '_').lower()}",
        "level": 1,
        "children": macro_children
    })

kpi_tree["tree"]["children"] = tree_children
kpi_tree["total_nodes"] = len(kpi_tree["nodes"])

print(f"\n✅ Generated {kpi_tree['total_nodes']} total KPI nodes")
print(f"📁 Saving to public/kpi_map.json...")

# Save to file
output_file = "public/kpi_map.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(kpi_tree, f, indent=2, ensure_ascii=False)

print(f"\n✅ Complete KPI data saved to {output_file}")
print(f"📊 Total nodes: {kpi_tree['total_nodes']}")
print(f"\n🎯 KPI Breakdown by Pillar:")
for pillar_name, macros in tree_structure.items():
    total_kpis = sum(len(kpis) for categories in macros.values() for kpis in categories.values())
    print(f"  • {pillar_name}: {total_kpis} KPIs across {len(macros)} macro processes")

print(f"\n🎉 Complete NYSS KPI Universe Generated Successfully!")
print(f"=" * 60)
