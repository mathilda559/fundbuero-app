import streamlit as st
from PIL import Image
import os
from model_utils import classify_image
from database import save_entry, load_entries
import uuid

st.set_page_config(page_title="Schul Fundbüro", layout="wide")

st.title("🧥 Online Fundbüro")

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

st.header("Fundstück hochladen")

uploaded_file = st.file_uploader("Bild hochladen", type=["jpg","png","jpeg"])

title = st.text_input("Titel des Fundstücks")

if uploaded_file and title:

    img = Image.open(uploaded_file)

    category = classify_image(img)

    unique_name = str(uuid.uuid4()) + ".jpg"

    image_path = os.path.join(UPLOAD_FOLDER, unique_name)

    img.save(image_path)

    save_entry(title, category, image_path)

    st.success(f"Gespeichert als {category}")


st.header("Gefundene Gegenstände")

entries = load_entries()

cols = st.columns(3)

for idx,row in entries.iterrows():

    with cols[idx % 3]:

        st.image(row["Bild"], use_column_width=True)
        st.markdown(f"**{row['Titel']}**")
        st.write(f"Kategorie: {row['Kategorie']}")
