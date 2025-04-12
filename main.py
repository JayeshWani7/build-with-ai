import schedule
import time
from tools.gmail_tools import list_recent_emails, get_gmail_service
from tools.calendar_tools import ensure_valid_creds
from agents import email_assistant_with_scheduling
from tools.logger import logger

get_gmail_service()
ensure_valid_creds()


def check_recent_emails():
    """
    Check for new emails in the last 10 minutes and process them.
    This function will be called every 10 minutes.
    """
    try:
        # Get emails from last 10 minutes
        recent_emails = list_recent_emails(minutes=15)

        if not recent_emails:
            logger.info("no_new_emails", minutes=15)
            return

        logger.info("found_new_emails", count=len(recent_emails))

        # Process each email
        for email in recent_emails:
            logger.info("processing_email", 
                       sender=email.get('sender'), 
                       subject=email.get('subject'))
            result = email_assistant_with_scheduling.invoke(
                {"messages": [{"role": "user", "content": f"Email Content: {email}"}]}
            )
            for message in result["messages"]:
                logger.info("assistant_response", response=message.content)

    except Exception as e:
        logger.exception("email_check_error", error=str(e))


def main():
    # Schedule the email checking function to run every 10 minutes
    schedule.every(1).minutes.do(check_recent_emails)

    logger.info("assistant_started", check_interval_minutes=1)

    # Run the first check immediately
    check_recent_emails()

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
