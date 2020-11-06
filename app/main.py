from opendip.converter import Converter
import streamlit as st
from PIL import Image
st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("OpenDIP API - Demonstration Dashboard")

uploaded_file = st.file_uploader("Choose an image...", type= ['png', 'jpg'] )
if uploaded_file is not None:
    print(uploaded_file)
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    converter = Converter()

    yiq_image , yiq_img_arr = converter.RGB_2_YIQ(image_obj = image)
    st.image(yiq_image, caption='Original RGB image converted to YIQ', use_column_width=True)

    rgb_image , rgb_img_arr = converter.YIQ_2_RGB(yiq_img_arr)
    st.image(rgb_image, caption='YIQ image converted back to RGB', use_column_width=True)

