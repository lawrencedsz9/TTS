import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from dotenv import load_dotenv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class EmailService:
    def __init__(self):
        # Gmail specific configuration
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.gmail_username = os.getenv('GMAIL_USERNAME')
        self.gmail_app_password = os.getenv('GMAIL_APP_PASSWORD')
        
        if not self.gmail_username or not self.gmail_app_password:
            raise ValueError(
                "Missing Gmail configuration. Please set GMAIL_USERNAME and GMAIL_APP_PASSWORD in .env file.\n"
                "To get an App Password:\n"
                "1. Enable 2-Step Verification in your Google Account\n"
                "2. Go to Security → App Passwords\n"
                "3. Generate a new app password for 'Mail'"
            )
        
        logger.info("Gmail email service initialized successfully")
        
    def send_audio_email(self, to_email: str, audio_file_path: str, text_content: str):
        """
        Send an email with the audio file attachment using Gmail SMTP
        
        Args:
            to_email (str): Recipient's email address
            audio_file_path (str): Path to the audio file
            text_content (str): The text that was converted to speech
        """
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.gmail_username
            msg['To'] = to_email
            msg['Subject'] = "welcome to SJEC OFFICE COLLABORATIONS"
            
            # Add HTML body
            html_body = f"""
            <html>
                <body>
                    <p>A Message from AI</p>
                </body>
            </html>
            """
            msg.attach(MIMEText(html_body, 'html'))
            
            # Add audio attachment
            audio_path = Path(audio_file_path)
            if not audio_path.exists():
                raise FileNotFoundError(f"Audio file not found: {audio_file_path}")
                
            with open(audio_path, 'rb') as audio_file:
                audio_attachment = MIMEAudio(audio_file.read(), _subtype='wav')
                audio_attachment.add_header('Content-Disposition', 'attachment', filename='audio.wav')
                msg.attach(audio_attachment)
            
            # Send email using Gmail SMTP
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Enable TLS
                server.login(self.gmail_username, self.gmail_app_password)
                server.send_message(msg)
            
            logger.info(f"Email sent successfully to {to_email}")
            
        except smtplib.SMTPAuthenticationError:
            error_msg = (
                "Failed to authenticate with Gmail. Please check your Gmail App Password.\n"
                "Make sure you have:\n"
                "1. Enabled 2-Step Verification in your Google Account\n"
                "2. Generated an App Password for 'Mail'\n"
                "3. Used the correct App Password in your .env file"
            )
            logger.error(error_msg)
            raise RuntimeError(error_msg)
            
        except Exception as e:
            logger.error(f"Error sending email: {str(e)}")
            raise RuntimeError(f"Failed to send email: {str(e)}") 