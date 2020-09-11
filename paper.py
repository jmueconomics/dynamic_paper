"""
 To get started, initiate a new environment by doing the following:

conda create -n streamlit python=3.7
source activate streamlit

pip install altair
pip install streamlit
pip install vega_datasets
"""

import streamlit as st
import altair as alt
from vega_datasets import data

source = data.cars()

#streamlit sidebar
st.sidebar.markdown(
'''
# Econ 123 Final Assignment
## By Duke Dog Student

[github](https://github.com/jmueconomicsalumni)

[linkedin](https://linkedin.com/in/dukedog)
''')

filtered = st.sidebar.multiselect("Select origins", list(set(source['Origin'])), list(set(source['Origin'])))


st.markdown('''
# My great paper

## Abstract
Wow a little to say here about a lot!

## Introduction
1. First ordered list item
2. Another item
⋅⋅* Unordered sub-list.
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses

## Methods
Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

Table: Table captions are done like this.

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

## Results
> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote.

## Results
Footnotes are best placed right after the paragraph first used.[^footnote]

[^footnote]: But you can also put them at the end of the document.

'''
)

st.title("My awesome interactive graph")

#altair example interactive chart
source = source[source["Origin"].isin(filtered)]
brush = alt.selection(type='interval')

points = alt.Chart(source).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.value('lightgray'))
).add_selection(
    brush
)

bars = alt.Chart(source).mark_bar().encode(
    y='Origin',
    color='Origin',
    x='count(Origin)'
).transform_filter(
    brush
)

points & bars
