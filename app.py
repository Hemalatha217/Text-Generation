## 💻 Source Code

```python
import streamlit as st
from transformers import pipeline

# Page Configuration
st.set_page_config(page_title="AI Text Generator")

# Cache Model
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="Qwen/Qwen3.8-2.4T-A95B"
    )

# Title
st.title("🤖 AI Text Generator")

st.write("✨ Enter a sentence and let AI complete it!")

# Load Model
generator = load_model()

# Input Box
prompt = st.text_area(
    "✍️ Enter your text:",
    height=150
)

# Generate Button
if st.button("✨ Generate Text"):

    if prompt.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("🤖 Generating..."):

            result = generator(
                prompt,
                max_new_tokens=100,
                do_sample=True,
                temperature=0.7
            )

            generated_text = result[0]["generated_text"]

            st.subheader("📄 Generated Text")
            st.write(generated_text)
```
