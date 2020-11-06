from opendip.converter import Converter
import streamlit as st
from PIL import Image
st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("OpenDIP API - Demonstration Dashboard")




st.sidebar.title("Configurações")
select = st.sidebar.selectbox('Escolha a opção que deseja visualizar', ["Conversor RGB-YIQ-RGB", "Construindo", "Construindo", "Construindo"])

if select == "Conversor RGB-YIQ-RGB":
    uploaded_file = st.file_uploader("Choose an image...", type= ['png', 'jpg'] )
    if uploaded_file is not None:

        orig_image = Image.open(uploaded_file)
        converter = Converter()

        converter.visualize_image(orig_image, capt='Uploaded Image')

        yiq_image , yiq_img_arr = converter.RGB_2_YIQ(image_obj = orig_image)
        rgb_image , rgb_img_arr = converter.YIQ_2_RGB(yiq_img_arr)

        converter.visualize_all_process(orig_image, yiq_image, rgb_image, capt = ['Original RGB Image','YIQ image','Image converted to RGB'])

