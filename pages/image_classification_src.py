import streamlit as st


st.header('Image Classification App')
st.subheader('This python code is implemented for Streamlit')
st.code('''
import pickle
from img2vec_pytorch import Img2Vec
from PIL import Image
import streamlit as st
from io import BytesIO

# Load the trained model
with open('pages/clothes.p', 'rb') as f:
    model = pickle.load(f)

img2vec = Img2Vec()

# Streamlit Web App Interface
st.set_page_config(layout="wide", page_title="Image Classification for Clothes")

st.write(
    ":grin: We'll try to predict the clothes depicted in your uploaded image :grin:"
)
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    return byte_im

def fix_image(upload):
    image = Image.open(upload)
    col1.write("Image to be predicted :camera:")
    col1.image(image)

    # Process image and make prediction
    img = image.convert('RGB')
    features = img2vec.get_vec(img)
    pred = model.predict([features])[0]

    col2.write("Category :wrench:")
    col2.header(pred)
    st.sidebar.download_button("Download fixed image", convert_image(image), "fixed.jpg", "image/jpeg")

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
    ''')
