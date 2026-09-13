import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title='Salesforce Transformation Executive Dashboard', layout='wide')
DATA = Path(__file__).parent / 'metrics' / 'kpi_framework.csv'
df = pd.read_csv(DATA)

st.title('Salesforce Transformation Executive Dashboard')
st.caption('Global CRM transformation • adoption • SLA • release quality • value realization')

c1, c2, c3, c4 = st.columns(4)
c1.metric('Facilities', '127')
c2.metric('Illustrative OPEX Reduction', '40%')
c3.metric('Release Success Target', '≥98%')
c4.metric('SLA Attainment Target', '≥95%')

st.subheader('Transformation KPI Framework')
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader('Executive Value Story')
col1, col2 = st.columns(2)
with col1:
    st.markdown('''
### Operational Outcomes
- Standardized global CRM operating model
- Automated service workflows
- Improved SLA visibility
- Stronger release governance
- Scalable regional configuration model
''')
with col2:
    st.markdown('''
### Leadership Outcomes
- KPI-driven decision support
- Adoption and value-realization tracking
- Better production readiness
- Reduced support complexity
- Illustrative 40% IT OPEX reduction
''')

st.subheader('Program Governance')
st.markdown('''
1. **Business & Requirements** — prioritize capabilities and regional needs  
2. **Architecture & Integration** — validate platform, data, API, and security design  
3. **Release Readiness** — confirm UAT, migration, training, support, rollback, and KPI baselines  
4. **Adoption & Value** — measure usage, SLA performance, release success, and operating cost
''')

st.info('This is a portfolio case study using illustrative metrics. No confidential employer or client data is included.')
