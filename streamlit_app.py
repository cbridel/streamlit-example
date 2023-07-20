from collections import namedtuple
from langchain.document_loaders import PyPDFLoader
from PIL import Image
import altair as alt
import math
import pandas as pd
import streamlit as st
import base64


st.title('Policy Contract Q&A')

selectPolicy1 = st.sidebar.checkbox('Select Policy 1')
selectPolicy2 = st.sidebar.checkbox('Select Policy 2')
selectPolicy3 = st.sidebar.checkbox('Select Policy 3')
documentColumn, chatColumn = st.columns(2)

with open('sample_contracts/file-491523.pdf', 'rb') as policy:
    base64_policy = base64.b64encode(policy.read()).decode('utf-8')
display_policy = F'<embed src="data:application/pdf;base64,{base64_policy}" width="600" height="500" type="application/pdf">'
st.markdown(display_policy, unsafe_allow_html=True)

# https://blog.jcharistech.com/2020/11/30/how-to-embed-pdf-in-streamlit-apps/
