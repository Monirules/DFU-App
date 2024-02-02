import streamlit as st
from PIL import Image
from util import predictor
import smtplib


# Function to run the image classifier
def run_image_classifier():
    st.title("Predict Foot Ulcers")

    # Sidebar for user input
    crop_image = st.sidebar.checkbox("Crop Image", value=False)

    # File uploader
    uploaded_file = st.file_uploader("Add Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Convert the uploaded file to an OpenCV image
        image = Image.open(uploaded_file).convert("RGB")

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Run prediction when the user clicks the button
        if st.button("Run Prediction"):
            probability, index = predictor(image)

            if index == 0:
                class_name = "Foot Ulcer"
            else:
                class_name = "Normal"

            if class_name is not None:
                st.success(f"Predicted Class: {class_name}, Probability: {probability*100:.2f}%")
            else:
                st.warning("Prediction failed.")
    else:
        st.info("Please upload an image.")



# Function for the contact page
def contact_page():
    st.title("Contact Page")

    # Form for user input
    with st.form("contact_form"):
        email = st.text_input("Your Email:")
        message = st.text_area("Message:")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Send email notification (you need to configure your SMTP server)
            send_email(email, message)
            st.success("Message sent successfully!")


# Email Sent Notification

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email, message):
    # Configure Gmail SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "mahmudislam2025@gmail.com"  # Your Gmail address
    smtp_password = "rjug wzkp lskn ggmn"  # Generate an app password for your Gmail account

    # Create an SMTP connection
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Compose the email
        subject = "New Contact Form Submission"
        body = f"Email: {email}\nMessage: {message}"

        # Create a multipart message and set headers
        msg = MIMEMultipart()
        msg["From"] = smtp_username
        msg["To"] = "mahmudislam2025@gmail.com"
        msg["Subject"] = subject

        # Attach the body to the email
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        server.sendmail(smtp_username, "mahmudislam2025@gmail.com", msg.as_string())


# Function to create a two-column layout with an image and text
        
def homepage():
    st.title("Diabetic Foot Ulcer Detection")
    st.markdown("Developed and maintain by Monirul, Hafeza and Olid")
    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Column 1: Display an image
    with col1:
        st.image("https://sa1s3optim.patientpop.com/assets/images/provider/photos/2069609.jpg", caption="Diabetic Foot Ulcer", use_column_width=True)
        st.image("https://static.bangkokpost.com/media/content/20231110/4955333.jpg", caption="Foot Ulcer and Wound", use_column_width=True)

    # Column 2: Display text
    with col2:
        st.write(
            """
            Diabetic Foot Ulcers (DFUs) are a common complication of diabetes and can lead to serious consequences 
            if not detected and treated early. Our web app leverages machine learning to assist in the early detection 
            of diabetic foot ulcers through the analysis of uploaded images. By using advanced image classification 
            techniques, our app aims to provide a quick and accurate assessment, helping individuals and healthcare 
            professionals in making informed decisions about preventive measures and treatments.

            Features:
            - Upload an image to check for the presence of foot ulcers.
            - Optional cropping of the uploaded image for better analysis.
            - Receive real-time predictions with probabilities.
            """
        )




# Main function to control the app
def main():

    # Create radio buttons in the sidebar for navigation
    selected_page = st.sidebar.radio("Navigation", ["Home", "Predict", "Contact"])

    # Show content based on the selected radio button
    if selected_page == "Home":
        homepage()
    elif selected_page == "Predict":
        run_image_classifier()
    elif selected_page == "Contact":
        contact_page()
    else:
        homepage()



# Run the Streamlit app
if __name__ == "__main__":
    main()
