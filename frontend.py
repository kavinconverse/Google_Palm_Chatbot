import streamlit as st
from dotenv import load_dotenv
from backend import *

def main():
    load_dotenv()
    st.set_page_config(page_title='CHATBOT')
    st.title('CHATBOT FOR PDF')
    st.subheader('CHATBOT')

    if 'conversation' not in st.session_state:
        st.session_state.conversation = None
    if 'chat_history' not in st.session_state:
         st.session_state.chat_history = None

    query = st.text_input('Ask a question')
    st.button('Response')
    if query:
        response = get_response(query)
        #st.write(response)   #o/p-->query,chat_history(human,ai),result
        st.session_state.chat_history = response['chat_history']

        for i,message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write('Human😎:',message.content)
            else:
                st.write('Bot🤖:', message.content)


    with st.sidebar:
        st.header('CHATBOT for Pdf')
        pdf_files = st.file_uploader('upload your PDF',type=['pdf'],accept_multiple_files=True)
        button = st.button('Upload')


        if button:
            st.spinner('Progresssing...')
            raw_text = get_pdf_read(pdf_files)
            st.write('Uploaded')
            st.write(len(raw_text))

            text_chunks = get_text_split(raw_text)
            st.write('length of chunks',len(text_chunks))

            embeddings = get_embeddings()
            st.info('Embedding created')

            vectorstore = push_to_vector_store(text_chunks, embeddings)
            st.success('Till vector store process completed')

            st.session_state.conversation = get_conv_chain(vectorstore)
            st.warning('Ready for conversation')

        #st.button('clear chat ',on_click=clear_chat)


if __name__ == '__main__':
    main()