import streamlit as st
from PIL import Image
import io

def resize_image(image, width, height):
    return image.resize((width,height), Image.LANCZOS)  #LANCZOS for high quality resizing

def main():
    st.title("Image Resizer")

    #Uploading image
    uploaded_file=st.file_uploader("Choose an image file",type=["jpg","jpeg","png"])

    if uploaded_file is not None:
        image=Image.open(uploaded_file)
        st.image(image,caption="Uploaded Image",use_column_width=True)
    
        #Resize option
        st.sidebar.header("Resize Options")
        width=st.sidebar.number_input("Width",min_value=1,value=image.width)
        height=st.sidebar.number_input("Height",min_value=1,value=image.height)

        resized_image=resize_image(image, width, height)

        st.subheader("Resized Image")
        st.image(resized_image,caption="Resized Image",use_column_width=True)

        #Save Resized image to ByteIO Object
        buffered=io.BytesIO()
        resized_image.save(buffered,format="PNG")
        img_bytes=buffered.getvalue()

        #Download button
        st.sidebar.download_button(
            label="Download Resized Image",
            data=img_bytes,
            file_name="resized_image.png",
            mime="image/png"
        )
if __name__=="__main__":
    main()