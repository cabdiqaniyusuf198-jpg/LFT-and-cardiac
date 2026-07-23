import streamlit as st

# 1. DEVELOPER DATA (Defined as variables to avoid errors)
DEV_NAME = "Abdi Kani Yusuf Kasim"
DEV_PHONE = "+252 634050084"

# Application Configuration
st.set_page_config(
    page_title="Medical Laboratory Reference",
    page_icon="🩺",
    layout="wide"
)

# 2. SIDEBAR DEVELOPER INFO
st.sidebar.title("👨‍💻 Developer Info")
st.sidebar.info(f"""
**Name:** {DEV_NAME}  
**Phone:** [{DEV_PHONE}](tel:{DEV_PHONE.replace(' ', '')})  
""")

st.sidebar.markdown("---")
st.sidebar.title("🧭 Navigation")

# Elaborate Data Dictionary
lab_data = {
    "Lipid Profile Tests": {
        "Total Cholesterol": {
            "Overview": "Cholesterol is a vital steroid molecule. It is required to build and maintain cell membranes and modulates membrane fluidity. It serves as a precursor for Vitamin D, bile salts (for fat digestion), and essential steroid hormones like cortisol, aldosterone, and sex hormones (estrogen, testosterone).",
            "Significance": "About 20–25% is produced in the liver. High levels are directly linked to the development of atherosclerosis (plaque buildup), which increases the risk of heart attacks.",
            "Sample": "Serum or plasma. Requires a strict 12-hour fasting period.",
            "Ranges": """
- **Desirable**: < 200 mg/dL (Lower risk for heart disease)
- **Borderline high**: 200–240 mg/dL
- **High risk**: > 240 mg/dL
""",
            "Interpretation": """
**Primary Hypercholesterolemia**: Often due to genetic LDL receptor defects.  
**Secondary Hypercholesterolemia**: Caused by Cholestasis, Nephrotic syndrome, Chronic renal failure, Hypothyroidism, or Obesity.  
**Hypocholesterolemia**: Seen in severe liver disease, malabsorption, or severe burns."""
        },
        "Triglycerides (TG)": {
            "Overview": "An ester derived from glycerol and three fatty acids. They are the main constituent of vegetable oil and animal fats. The body stores unused calories as TGs in adipocytes (fat cells).",
            "Significance": "High levels are associated with atherosclerosis. Levels above 1000 mg/dL significantly increase the risk of acute pancreatitis.",
            "Sample": "Serum or plasma. Must be 12-hour fasting (levels rise 5-10x within hours of eating).",
            "Ranges": """
- **Normal**: < 150 mg/dL
- **Borderline high**: 150–199 mg/dL
- **High**: 200–498 mg/dL
- **Very high**: > 500 mg/dL (Pancreatitis risk)
""",
            "Interpretation": """
**Elevated**: High-carb diets, Hypothyroidism, Pancreatitis, Alcoholism, or Myocardial Infarction.  
**Decreased**: Low-fat diets, hyperthyroidism, or malabsorption syndrome."""
        },
        "HDL (Good Cholesterol)": {
            "Overview": "High-Density Lipoprotein is known as 'Good Cholesterol' because it removes cholesterol from atheromas (plaques) within arteries and transports it back to the liver for excretion.",
            "Significance": "HDL acts as a repository for proteins (Apo C and Apo E) used in lipid metabolism. High levels are protective against cardiovascular disease.",
            "Sample": "Serum or plasma (12-hour fast).",
            "Ranges": """
- **Low (High risk)**: < 40 mg/dL
- **Medium**: 40–59 mg/dL
- **High (Optimal)**: > 60 mg/dL (Protective)
""",
            "Interpretation": "**Decreased**: Heightened risk for heart disease; commonly seen in sedentary lifestyles, smoking, and obesity."
        },
        "LDL (Bad Cholesterol)": {
            "Overview": "Low-Density Lipoprotein transports cholesterol to body tissues. It is considered 'Bad' because high levels lead to the formation of foam cells in artery walls, initiating atherosclerosis.",
            "Significance": "Calculated using the Friedewald formula: [Total Cholesterol] – [Total HDL] – [VLDL] (where VLDL = TG/5).",
            "Sample": "Serum or plasma.",
            "Ranges": """
- **Optimal**: < 100 mg/dL
- **Near Optimal**: 100–129 mg/dL
- **High**: 160–189 mg/dL
- **Very high**: > 190 mg/dL
""",
            "Interpretation": "**Note**: The calculation is inaccurate if Triglycerides are above 400 mg/dL; direct measurement is required in those cases."
        }
    },
    "Cardiac Marker Tests": {
        "Cardiac Troponins (T and I)": {
            "Overview": "Troponins are proteins that leak into the bloodstream from injured myocardial cells. They are currently the 'Gold Standard' for heart attack diagnosis.",
            "Significance": "Highly sensitive and specific. They have largely replaced older markers like AST and LDH for primary cardiac assessment.",
            "Sample": "Serum.",
            "Ranges": "Reference ranges vary by laboratory and assay sensitivity (usually measured in ng/mL).",
            "Interpretation": "Elevated levels are nearly always indicative of myocardial injury. Unlike enzymes, troponins can stay elevated for a longer duration."
        },
        "CK-MB (Creatine Kinase-MB)": {
            "Overview": "A specific isoenzyme of Creatine Kinase found primarily in the myocardium (heart muscle). While total CK is found in skeletal muscle, CK-MB is heart-specific.",
            "Significance": "It is the first cardiac enzyme to rise after a Myocardial Infarction (MI). Useful for confirming early diagnosis and detecting a second heart attack (re-infarction).",
            "Sample": "Serum.",
            "Ranges": "Usually < 5% of total CK activity.",
            "Interpretation": """
- **Initial Rise**: 2–4 hours post-MI.
- **Peak**: 12–24 hours.
- **Return to Normal**: 1–3 days.  
**Note**: Sensitivity reaches ~100% at 10–12 hours after the onset of chest pain."""
        },
        "Total Creatine Kinase (CK)": {
            "Overview": "An enzyme acting as an energy reservoir in tissues that consume ATP rapidly, like heart and skeletal muscle.",
            "Significance": "Composed of three isoenzymes: CK-MM (Muscle), CK-BB (Brain), and CK-MB (Heart). Total CK rises rapidly whenever there is muscle damage.",
            "Sample": "Serum.",
            "Ranges": "Gender and muscle-mass dependent.",
            "Interpretation": """
- **Initial Rise**: 4–6 hours post-MI.
- **Peak**: 18–24 hours.
- **Return to Normal**: 2–3 days.  
**Elevated in**: Muscle trauma, strenuous exercise, and Duchenne muscular dystrophy."""
        },
        "Lactate Dehydrogenase (LDH)": {
            "Overview": "An enzyme that catalyzes the interconversion of pyruvate and lactate. LDH-1 is the isoenzyme specific to the heart.",
            "Significance": "Acts as a delayed marker for heart attacks. It remains elevated longer than CK or AST, making it useful for late diagnosis.",
            "Sample": "Serum (Avoid Hemolysis as RBCs contain high LDH).",
            "Ranges": "Laboratory specific.",
            "Interpretation": """
- **Initial Rise**: 24–48 hours post-MI.
- **Peak**: 3–4 days.
- **Return to Normal**: Up to 10 days.  
**Diagnostic Pattern**: If LDH-1 becomes higher than LDH-2 (Flipped Pattern), it strongly suggests an MI."""
        },
        "AST / GOT": {
            "Overview": "Aspartate Transaminase is an enzyme found in the liver and heart muscle. It was one of the earliest markers used for cardiac assessment.",
            "Significance": "The extent of the rise is directly proportional to the size of the heart muscle damage (infarct size).",
            "Sample": "Serum.",
            "Ranges": "Typically < 40 U/L.",
            "Interpretation": """
- **Initial Rise**: 4–6 hours post-MI.
- **Peak**: 16–48 hours.
- **Return to Normal**: 3–5 days.  
**Prognosis**: Values 10-15x higher than normal indicate a poor/fatal prognosis."""
        }
    }
}

# 3. MAIN UI
st.title("🔬 Clinical Laboratory Diagnostic Excellence Hub")
st.subheader("Comprehensive Guide for Lipid & Cardiac Profiles")
st.markdown("---")

# Category selection
category = st.sidebar.radio("Select Profile Category", list(lab_data.keys()))
test_name = st.sidebar.selectbox("Select Specific Test", list(lab_data[category].keys()))

if test_name:
    data = lab_data[category][test_name]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header(f"📊 {test_name}")
        st.write(f"### Overview")
        st.write(data["Overview"])
        
        st.write(f"### Clinical Significance")
        st.write(data["Significance"])
        
        st.write(f"### Interpretation & Causes")
        st.warning(data["Interpretation"])

    with col2:
        st.write(f"### Reference Ranges")
        st.success(data["Ranges"])
        
        st.write(f"### Specimen Requirements")
        st.info(data["Sample"])

# 4. FOOTER
st.markdown("---")
st.caption(f"© 2024 Developed by: **{DEV_NAME}** | Contact: **{DEV_PHONE}**")