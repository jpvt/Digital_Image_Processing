from opendip.converter import Converter
from opendip.filter import Filter
from opendip.correlator import Correlator
from io import BytesIO
import base64
import numpy as np
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
select = st.sidebar.selectbox('Escolha a opção que deseja visualizar', ["Introdução","Conversor RGB-YIQ-RGB", "Aplicação de Filtros", "Correlação Normalizada"])





if select == "Introdução":

    st.header("Introdução")

    st.markdown("""
    Nesta aplicação demonstraremos a primeira versão do OpenDIP, uma biblioteca desenvolvida como trabalho prático para o curso Introdução ao Processamento Digital de Imagens durante o período 2020.1, ministrada pelo [Prof. Leonardo Vidal](http://lattes.cnpq.br/1047122596139990).

    Nessa primeira versão, apresentaremos três funcionalidades: Conversão de espaço, em que implementamos os conversores RGB-YIQ e YIQ-RGB; Correlação de Imagens, em que aplicamos filtros pontuais como Sobel, Negativo em RGB, Negativo em Y, Média e Mediana; Correlação Normalizada, que encontra o que é mais semelhante de uma imagem em outra.
    """)

    st.subheader("Metodologia")
    # Texto com Metodologia utilizada no trabalho
    st.markdown("""
    Para o desenvolvimento da biblioteca escolhemos a linguagem Python, devido à sua praticidade e bibliotecas como Numpy e Pillow, que respectivamente permitem trabalhar melhor com vetores e manipular a entrada e saída de imagens. Além disso, utilizamos a biblioteca Streamlit para realizar essa demonstração, a fim de documentar nosso trabalho de maneira clara e com uma linguagem bastante visual.
    """)

    st.subheader("Como contribuir")
    st.markdown("""
    Caso tenha gostado da iniciativa e queira contribuir para com o desenvolvimento da biblioteca, após a finalização da disciplina iremos começar a aceitar pull requests no nosso [repositório no github](https://github.com/jpvt/Digital_Image_Processing).
    """)

    st.subheader("Contato")
    st.markdown("""
    Sinta-se livre para nos contactar via email ou issues no github. Mais informações sobre contato estão no tópico autores.
    """)
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

        select_filter = st.selectbox('Selecione o filtro que deseja aplicar', ["Negativo RGB", "Negativo Y","Sobel", "Média", "Mediana"])

        if select_filter == 'Sobel':

            select_padding = st.checkbox('Aperte caso deseja utilizar Padding')
            mode_filter = st.selectbox("Selecione o modo do filtro", ["horizontal","vertical"])

        elif select_filter == "Negativo RGB" : 

            redPixel = st.checkbox('Negativo na banda R')
            greenPixel = st.checkbox('Negativo na banda G')
            bluePixel = st.checkbox('Negativo na banda B')
        
        elif select_filter == "Média" or select_filter == "Mediana":
            select_padding = st.checkbox('Aperte caso deseja utilizar Padding')
            vertical = st.number_input("Digite o tamanho vertical do box", min_value=1, step=1)
            horizontal = st.number_input("Digite o tamanho horizontal do box", min_value=1, step = 1)

    if uploaded_file is not None:

        orig_image = Image.open(uploaded_file)

        if select_filter == "Negativo RGB":
            
            filter = Filter()
            tranf_image = filter.apply_negative_filter(image_path=uploaded_file, R=redPixel, G=greenPixel, B=bluePixel)

        if select_filter == "Negativo Y":

            filter = Filter()
            tranf_image = filter.apply_negative_filter_in_y(image_path=uploaded_file)

        if select_filter == "Sobel":
            
            filter = Filter()
            _ , _, transf_arr = filter.apply_sobel_filter(image_path=uploaded_file, mode=mode_filter, zero_padding=select_padding)
            tranf_image = Image.fromarray(transf_arr.astype('uint8'))

        if select_filter == "Média":
           
            filter = Filter()
            img, preprocessed, output = filter.apply_box_filter(image_path=uploaded_file, box_shape=(vertical, horizontal), zero_padding=select_padding)
            tranf_image = Image.fromarray(output.astype('uint8'))

        if select_filter == "Mediana":

            filter = Filter()
            img, preprocessed, output = filter.apply_median_filter(image_path=uploaded_file, filter_shape=(vertical, horizontal), zero_padding=select_padding)
            tranf_image = Image.fromarray(output.astype('uint8'))


        l, r = st.beta_columns(2)

        l.subheader("Imagem Original")
        l.image(orig_image, use_column_width=True)

        r.subheader("Imagem Transformada")
        r.image(tranf_image, use_column_width=True)


        if st.checkbox('Explicação sobre aplicamos esse filtro para você'):
            st.markdown("""
                        ## Explicação massa demais!
                        """)

elif select == "Correlação Normalizada":
    st.header("Correlação Normalizada")
    correlator = Correlator()
    left_column, right_column = st.beta_columns(2)

    with left_column:

        uploaded_file = st.file_uploader("Escolha uma imagem RGB que deseja aplicar um filtro", type= ['png', 'jpg'] )


    with right_column:
        
        uploaded_filter = st.file_uploader("Escolha um filtro RGB que deseja aplicar na imagem", type= ['png', 'jpg'] )
        

    select_padding = st.checkbox('Aperte caso deseja utilizar Padding')

    if uploaded_file is not None and uploaded_filter is not None:
        orig_image = np.array(Image.open(uploaded_file).convert('RGB'))
        left_column.image(orig_image, use_column_width=True)

        filter_matrix = np.array(Image.open(uploaded_filter).convert('RGB'))
        right_column.image(filter_matrix, use_column_width=True)

        orig_image, tranf_image = correlator.apply_norm_correlation(uploaded_file, filter_matrix)

        l, r = st.beta_columns(2)

        l.subheader("Imagem Original")
        l.image(orig_image, use_column_width=True)

        r.subheader("Imagem Transformada")
        r.image(tranf_image, use_column_width=True)


        if st.checkbox('Explicação sobre aplicamos esse filtro para você'):
            st.markdown("""
                        ## Explicação massa demais!
                        """)