# Email Assistant

A smart email and calendar management system powered by Gemini Pro that automatically processes incoming emails and manages calendar events.

## Features

- **Automated Email Processing**: Monitors inbox for new emails every minute
- **Smart Email Responses**: Generates contextual email responses using Gemini Pro
- **Calendar Management**: Automatically handles calendar event creation, updates, and deletions
- **Gmail Integration**: Seamlessly works with Gmail for email management
- **Google Calendar Integration**: Direct integration with Google Calendar for event management

## Project Structure

```
├── main.py              # Main application entry point
├── agents.py            # AI agents configuration and prompts
├── models.py            # AI model configurations
├── tools/
│   ├── gmail_tools.py   # Gmail API integration tools
│   ├── calendar_tools.py # Google Calendar API tools
│   └── logger.py        # Logging utilities
```

## Prerequisites

- Python 3.x
- Google Cloud Project with Gmail and Calendar APIs enabled
- Google OAuth 2.0 credentials

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Google OAuth 2.0 credentials and save them appropriately

## Usage

Run the main application:
```bash
python main.py
```

The assistant will:
1. Check for new emails every minute
2. Process emails using AI to understand context and requirements
3. Generate appropriate responses and create drafts
4. Handle calendar events when scheduling is involved

## Dependencies

Key dependencies include:
- google-api-python-client: Google API client library
- langgraph: For creating reactive AI agents
- schedule: For periodic task scheduling

## Configuration

Ensure proper setup of:
1. Google OAuth 2.0 credentials
2. Gmail API access
3. Google Calendar API access

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
