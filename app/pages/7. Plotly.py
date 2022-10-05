# Run this using:
# streamlit run "streamlit tutorial.py"

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path


## Plotly Test  ##################################################

st.title('7. Plotly Test')

@st.cache(allow_output_mutation=True)
def load_file(file_name):
    df = pd.read_excel(file_name,
                       header=0,
                       index_col=None,
                       dtype={'filename': 'category',
                       'title_word': 'category',
                       'content_word': 'string',
                       'content_word_count': 'int16',
                       'cos_similarity': 'float',
                       'weightage': 'float',
                       'sum_of_weights': 'float',
                       'ideation_score': 'float'
                       }
                    )
    return df

# st.text(Path.cwd())

if 'D:' in str(Path.cwd()):
    df = load_file('./Data/Test.xlsx')
else:
    df = load_file('./app/Data/Test.xlsx')


st.text('Dataframe')
st.dataframe(df)

trace1 = go.Histogram(x=df['cos_similarity'],
                      y=df['content_word_count'],
                      name='Nedd830',
                      xbins=dict(start=-0.5,
                                 end=1,
                                 size=0.01
                                ),
                      histfunc='sum',
                     )

fig1 = go.Figure(data=[trace1])

fig1.update_layout(xaxis_range=[-0.5, 1],
                  xaxis_dtick=0.05,
                  template='plotly_dark',
                  width=800,
                  height=500
                 )

st.text('Distribution of Cosine Similarities')
st.plotly_chart(fig1)
##########

df1 = df.drop_duplicates(subset=['filename'])

trace2 = go.Box(x=df1['ideation_score'],
                orientation='h',
               )

fig2 = go.Figure(data=[trace2])

fig2.update_layout(template='plotly_dark',
                  # xaxis_range=[-1, 1],
                  width=800,
                  height=500
                 )

st.text('Box Plot of Ideation Score')
st.plotly_chart(fig2)
##########

df1 = df.groupby(['filename']).apply(lambda row : round(sum(row['content_word_count'] * row['weightage']), 2))
# df1 = df1.sort_values(ascending=True)

trace3 = go.Bar(x=df1,
                y=df1.index,
                orientation='h',
                text=df1,
               )

fig3 = go.Figure(data=[trace3])

fig3.update_layout(template='plotly_dark',
                  # xaxis_range=[-1, 1],
                  width=800,
                  height=500
                 )

st.text('Distribution of Ideation Score by Essay')


but_sort = st.radio('Sort:', ('Original', 'Ascending', 'Descending') )
if but_sort == 'Ascending':

    # df1 = df1.sort_values(ascending=True)
    # fig3.update_traces(x=df1,
    #                    y=df1.index
    #                    )

    aaa = df1.sort_values(ascending=True).index

    fig3.update_layout(
        yaxis={'categoryarray': aaa, 'categoryorder': 'array'}
        )
    st.text('Asc')

elif but_sort == 'Descending':
    # df1 = df1.sort_values(ascending=False)
    # fig3.update_traces(x=df1,
    #                    y=df1.index
    #                    )

    aaa = df1.sort_values(ascending=False).index

    fig3.update_layout(
        yaxis={'categoryarray': aaa, 'categoryorder': 'array'}
        )

    st.text('Desc')
else:
    fig3.update_layout(
        yaxis={'categoryarray': df1.index, 'categoryorder': 'array'})
    st.text('Original')

fig3_container = st.container()
with fig3_container:
    st.plotly_chart(fig3)


##########
df1 = df.groupby(['weightage']).apply(lambda row : round(sum(row['content_word_count'] * row['weightage']), 2))
df1 = df1.drop(labels=[0.00])
df1.index = list(map(str, df1.index))

trace4 = go.Bar(x=df1.index,
                y=df1,
                orientation='v',
                text=df1,
               )

fig4 = go.Figure(data=[trace4])

fig4.update_layout(template='plotly_dark',
                  width=800,
                  height=500
                 )

st.text('Distribution of Weightages')
st.plotly_chart(fig4)