import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#this is an edit
st.write("""
# CSE 163 Final Project
""")

aa = pd.read_csv('/Users/faithong/Desktop/cse163final/cse163final/data_aa.csv')
ea = pd.read_csv('/Users/faithong/Desktop/cse163final/cse163final/data_ea.csv')

aa['Race'] = "African-American"
ea['Race'] = "European-American"
all_races = aa.merge(ea, how='outer')
all_races = all_races.loc[:, all_races.columns != 'gene_id']
st.write(all_races)

# visualization for gene_biotype
gene_biotype_graph = sns.catplot(data=all_races, x="gene_biotype", kind="count", ci=None)
st.pyplot(gene_biotype_graph)


# visualization for pair type
pair_type_graph = sns.catplot(data=all_races, x="pair_type", kind="count", ci=None)
st.pyplot(pair_type_graph)


# visualization for gene class
gene_class_graph = sns.catplot(data=all_races, x="gene_class", kind="count", ci=None)
st.pyplot(gene_class_graph)

