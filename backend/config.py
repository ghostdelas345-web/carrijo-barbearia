# Application Configuration for Carrijo Barbearia

class Config:
    """Base configuration for the application."""
    SECRET_KEY = 'your_secret_key'
    DEBUG = False
    TESTING = False
    
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # WhatsApp Settings
    WHATSAPP_API_KEY = 'your_whatsapp_api_key'
    WHATSAPP_NUMBER = 'your_whatsapp_number'
    
    # Email Configuration
    MAIL_SERVER = 'smtp.your-email-provider.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@example.com'
    MAIL_PASSWORD = 'your_email_password'
    
    # OAuth Configuration
    OAUTH_CLIENT_ID = 'your_oauth_client_id'
    OAUTH_CLIENT_SECRET = 'your_oauth_client_secret'
    OAUTH_REDIRECT_URI = 'http://yourdomain.com/callback'
    
    # Business Settings
    BUSINESS_NAME = 'Carrijo Barbearia'
    BUSINESS_PHONE = 'your_business_phone'
    BUSINESS_EMAIL = 'contact@carrijo.com'
    BUSINESS_ADDRESS = '1234 Barber St, HairCity, HC 12345'
    
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass