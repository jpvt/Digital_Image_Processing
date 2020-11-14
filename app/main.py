from opendip.converter import Converter
from io import BytesIO
import base64
import streamlit as st
from PIL import Image
st.set_option('deprecation.showfileUploaderEncoding', False)





def get_image_download_link(img):
	"""Generates a link allowing the PIL image to be downloaded
	in:  PIL image
	out: href string
	"""
	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'       <a href="data:file/jpg;base64,{img_str}">Baixe a imagem escolhida</a>  '
	return href

st.title("OpenDIP - Dashboard de Demonstração")




st.sidebar.title("Configurações")
select = st.sidebar.selectbox('Escolha a opção que deseja visualizar', ["Introdução","Conversor RGB-YIQ-RGB", "Aplicação de Filtros"])




if select == "Introdução":

    st.header("Introdução")
    st.subheader("Resumo")
    # Texto resumo do trabalho

    st.subheader("Metodologia")
    # Texto com Metodologia utilizada no trabalho

    st.subheader("Autores")
    # Autores do Trabalho


elif select == "Conversor RGB-YIQ-RGB":
    st.header("Conversor RGB-YIQ-RGB")
    uploaded_file = st.file_uploader("Escolha uma imagem RGB que deseja converter para YIQ", type= ['png', 'jpg'] )
    if uploaded_file is not None:

        orig_image = Image.open(uploaded_file)
        converter = Converter()

        yiq_image , yiq_img_arr = converter.RGB_2_YIQ(image_obj = orig_image)
        rgb_image , rgb_img_arr = converter.YIQ_2_RGB(yiq_img_arr)

        conversion_selectbox = st.selectbox('Selecione a imagem que deseja visualizar em larga escala', ["Imagem RGB Original","Imagem YIQ", "Imagem RGB convertida a partir da imagem YIQ"])

        converter.visualize_all_process(orig_image, yiq_image, rgb_image, capt = ['Imagem RGB Original','Imagem YIQ','Imagem RGB convertida a partir da imagem YIQ'])

        if conversion_selectbox == "Imagem RGB Original":

            converter.visualize_image(orig_image, capt='Imagem RGB Original')

        elif conversion_selectbox == "Imagem YIQ":

            converter.visualize_image(yiq_image, capt='Imagem YIQ')


            st.markdown(get_image_download_link(yiq_image), unsafe_allow_html=True)

        elif conversion_selectbox == "Imagem RGB convertida a partir da imagem YIQ":

            converter.visualize_image(rgb_image, capt='Imagem RGB convertida a partir da imagem YIQ')

            st.markdown(get_image_download_link(rgb_image), unsafe_allow_html=True)

        if st.checkbox('Explicação sobre como fizemos essa conversão para você'):
            st.markdown("""
                        ## Explicação massa demais!
                        """)

elif select == "Aplicação de Filtros":

    st.header("Aplicação de Filtros")

    left_column, right_column = st.beta_columns(2)

    with left_column:
        uploaded_file = st.file_uploader("Escolha uma imagem RGB que deseja aplicar um filtro", type= ['png', 'jpg'] )
    with right_column:
        select_filter = st.selectbox('Selecione o filtro que deseja aplicar', ["Negativo","Sobel", "Média", "Mediana", "Normalizada"])
        select_padding = st.checkbox('Aperte caso deseja utilizar Padding')

    if uploaded_file is not None:

        orig_image = Image.open(uploaded_file)
        converter.visualize_image(orig_image, capt='Uploaded Image')


        if st.checkbox('Explicação sobre aplicamos esse filtro para você'):
            st.markdown("""
                        ## Explicação massa demais!
                        """)