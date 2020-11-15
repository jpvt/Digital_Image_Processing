from opendip.converter import Converter
from opendip.filter import Filter
from opendip.correlator import Correlator
from io import BytesIO
import base64
import streamlit as st
from PIL import Image
st.set_option('deprecation.showfileUploaderEncoding', False)





# def get_image_download_link(img):
# 	"""Generates a link allowing the PIL image to be downloaded
# 	in:  PIL image
# 	out: href string
# 	"""
# 	buffered = BytesIO()
# 	img.save(buffered, format="JPEG")
# 	img_str = base64.b64encode(buffered.getvalue()).decode()
# 	href = f'       <a href="data:file/jpg;base64,{img_str}">Baixe a imagem escolhida</a>  '
# 	return href

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
    author_1, author_2, author_3, author_4 = st.beta_columns(4)

    jp = Image.open('assets/authors/jp.png')
    jw = Image.open('assets/authors/wallace.png')
    ita = Image.open('assets/authors/itamar.png')
    sheywesk = Image.open('assets/authors/sheywesk.png')


    with author_1:
        st.markdown('**[Itamar Filho](https://linkedin.com/in/itamarrocha)**')
        st.image(ita, use_column_width=True)
        st.markdown('Github: **[ItamarRocha](https://github.com/ItamarRocha)**')
    
    with author_2:
        st.markdown('**[João Pedro Teixeira](https://www.linkedin.com/in/jpvt/)**')
        st.image(jp, use_column_width=True)
        st.markdown('Github: **[jpvt](https://github.com/jpvt)**')

    with author_3:
        st.markdown('**[João Wallace Lucena](https://www.linkedin.com/in/jo%C3%A3o-wallace-b821bb1b0/)**')
        st.image(jw, use_column_width=True)
        st.markdown('Github: **[joallace](https://github.com/joallace)**')
    
    with author_4:
        st.markdown('**[Sheywesk Medeiros](https://www.linkedin.com/in/sheywesk-medeiros/)**')
        st.image(sheywesk, use_column_width=True)
        st.markdown('Github: **[sheywesk](https://github.com/sheywesk)**')




elif select == "Conversor RGB-YIQ-RGB":

    st.header("\tConversor RGB-YIQ-RGB")
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


            # st.markdown(get_image_download_link(yiq_image), unsafe_allow_html=True)

        elif conversion_selectbox == "Imagem RGB convertida a partir da imagem YIQ":

            converter.visualize_image(rgb_image, capt='Imagem RGB convertida a partir da imagem YIQ')

            # st.markdown(get_image_download_link(rgb_image), unsafe_allow_html=True)

        if st.checkbox('Explicação sobre como fizemos essa conversão para você'):
            st.markdown("""
                        ## Explicação massa demais!
                        """)

elif select == "Aplicação de Filtros":
    
    st.header("Aplicação de Filtros")
    correlator = Correlator()
    mode_filter = "horizontal"
    redPixel = True
    greenPixel = True
    bluePixel = True
    left_column, right_column = st.beta_columns(2)

    with left_column:
        uploaded_file = st.file_uploader("Escolha uma imagem RGB que deseja aplicar um filtro", type= ['png', 'jpg'] )
    with right_column:
        select_filter = st.selectbox('Selecione o filtro que deseja aplicar', ["Negativo","Sobel", "Média", "Mediana"])
        if select_filter == 'Sobel':
            select_padding = st.checkbox('Aperte caso deseja utilizar Padding')
            select_norm = st.checkbox('Aperte caso deseja utilizar correlação normalizada')
            mode_filter = st.selectbox("Selecione o modo do filtro", ["horizontal","vertical"])
        elif select_filter == "Negativo" : 
            redPixel = st.checkbox('Negativo na banda R')
            greenPixel = st.checkbox('Negativo na banda G')
            bluePixel = st.checkbox('Negativo na banda B')

    if uploaded_file is not None:

        orig_image = Image.open(uploaded_file)
        print(orig_image)
        tranf_image = orig_image
        if select_filter == "Negativo":
            
            filter = Filter()
            tranf_image = filter.apply_negative_filter(image_path= orig_image,R = redPixel,G=greenPixel,B=bluePixel)
        if select_filter == "Sobel":
            tranf_image = correlator.apply_sobel_filter(image_path = orig_image, mode = mode_filter)
        with left_column:
            st.text("")
            st.subheader("Imagem Original")
            st.image(orig_image, use_column_width=True)

        with right_column:
            st.subheader("Imagem transformada")
            st.image(tranf_image, use_column_width=True,clamp=True)


        if st.checkbox('Explicação sobre aplicamos esse filtro para você'):
            st.markdown("""
                        ## Explicação massa demais!
                        """)
   
