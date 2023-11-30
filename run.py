import streamlit as st
import os

# Tiêu đề của ứng dụng
st.title('Ứng Dụng Nhận Diện Đối Tượng')

# Tạo một form cho phép người dùng nhập các tham số
with st.form(key='my_form'):
    weight_file = st.text_input(label='Đường dẫn tới file trọng số (best.pt)', value='best.pt')
    image_size = st.number_input(label='Kích thước ảnh', value=416)
    confidence_threshold = st.slider(label='Ngưỡng tự tin', min_value=0.0, max_value=1.0, value=0.5)
    source = st.text_input(label='Nguồn (0 cho webcam, đường dẫn cho ảnh hoặc video)', value='0')
    submit_button = st.form_submit_button(label='Chạy Nhận Diện')

# Khi người dùng nhấn nút "Chạy Nhận Diện"
if submit_button:
    command = f"python detect.py --weights best.pt --img 416 --conf 0.5 --source 0"
    os.system(command)
