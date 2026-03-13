import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='ai_interactions.log',
    level=logging.INFO, 
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_interaction(user_id, interaction):
    """Log interactions with the AI system."""
    logging.info(f"User: {user_id} | Interaction: {interaction}")

def log_error(error_message):
    """Log errors that occur in the interaction."""
    logging.error(f"Error: {error_message}")

def audit_trail(action, user_id):
    """Log actions taken in the system for audit purposes."""
    logging.info(f"Action: {action} | User: {user_id}")

# Example usage
if __name__ == "__main__":
    user = "jayantyadav822-afk"  # Current user's login
    log_interaction(user, "User initiated a query.")
    audit_trail("Query executed", user)