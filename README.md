# st.form

`st.form` creates a form that batches elements together with a "Submit" button.

Typically, whenever a user interacts with a widget, the Streamlit app is rerun.

A form is a container that visually groups other elements and widgets together, and contains a Submit button. Herein, a user can interacts with one or more widgets for as many times as they like without causing a rerun. Finally, when the form's Submit button is pressed, all widget values inside the form will be sent to Streamlit in a single batch.

To add elements to a form object, you can use the `with` notation (preferred) or just call methods directly on the form (by first assigning it to a variable and subsequently applying Streamlit methods on it). See in the example app.

Forms have a few constraints:
- Every form must contain a `st.form_submit_button`.
- `st.button` and `st.download_button` cannot be added to a form.
- Forms can appear anywhere in your app (sidebar, columns, etc), but they cannot be embedded inside other forms.

For more information about forms, check out our [blog post](https://blog.streamlit.io/introducing-submit-button-and-forms/).

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/)

## Code
Here's how to use `st.form`:
```python
import streamlit as st


```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
```

## Further reading

