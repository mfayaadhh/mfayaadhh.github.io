import streamlit as st
from PIL import Image


st.set_page_config(page_title= "Website", page_icon= ":skull:", layout='wide')


#----Header----
col1, col2 = st.columns(2)
image = Image.open("C:/Users/ACER/Downloads/pp.jpg")
new_image = image.resize((400,400))
with st.container():
    with col1:
        st.title("Hey friends :wave:")
        st.subheader('I\'m Fayaadh and I\'m a Accountant Student.')
        st.write("I am passionate about finding ways to use Python.")
    with col2:
        st.image(new_image)


with st.container():
    st.write("---")    
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What I Do')
        st.write('##')
        st.write(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Nullam vulputate hendrerit est, convallis convallis sem vestibulum in.
            Nulla mi risus, iaculis pretium facilisis vitae, finibus eget purus.
            Nulla accumsan, arcu in malesuada laoreet, sem lacus facilisis justo, nec pretium lectus elit id libero.
            Mauris tempor ornare posuere. Maecenas ut ex blandit, laoreet mi et, tempus est.
            Sed turpis purus, tristique id nisi ac, rhoncus fermentum nisl. Vivamus nunc ex, vulputate a tellus ut, facilisis euismod risus.
            Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas in pellentesque purus, ultricies maximus ante.
            Aenean eget tortor at felis ultrices lacinia in at mauris.
            """
        )
with st.container():
    col1,col2,col3 = st.columns((1,3,1))
    with col2:
        st.image(image)
    
