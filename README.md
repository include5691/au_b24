# au_b24
Bitrix24 REST API Automation Library

A comprehensive Python library that provides convenient high-level functions for interacting with the Bitrix24 REST API. Simplifies common CRM operations like managing leads, deals, contacts, users, and more.

## Installation

```bash
pip install .
```

## Setup

Create a `.env` file in your project root with your Bitrix24 credentials:

```env
BITRIX_ID=your_bitrix_id
CRM_USERTOKEN=/your_user_id/your_webhook_token
USER_USERTOKEN=/your_user_id/your_webhook_token
IMOPENLINES_USERTOKEN=/your_user_id/your_webhook_token
VOXIMPLANT_USERTOKEN=/your_user_id/your_webhook_token
TASKS_USERTOKEN=/your_user_id/your_webhook_token
DEPARTMENT_USERTOKEN=/your_user_id/your_webhook_token
IM_USERTOKEN=/your_user_id/your_webhook_token
```

## Quick Start

```python
from dotenv import load_dotenv
load_dotenv()

import au_b24

# Initialize with rate limiting (optional)
au_b24.init_requests_pause(0.5)  # 500ms pause between requests

# Get a lead
lead = au_b24.get_lead(123)

# Get leads with filters
leads = au_b24.get_leads(
    filters={"STATUS_ID": "NEW"},
    select=["ID", "TITLE", "NAME", "PHONE"],
    order="ASC"
)

# Update a lead
au_b24.update_lead(123, {"TITLE": "Updated Title"})
```

## Core Features

### 🎯 CRM Entities Management

#### Leads
- `get_lead(lead_id)` - Get single lead
- `get_leads(filters, select, order, limit)` - Get multiple leads
- `update_lead(lead_id, fields)` - Update lead
- `delete_lead(lead_id)` - Delete lead
- `parse_leads(function)` - Parse all leads with custom function
- `get_phone_by_lead(lead_id)` - Extract phone number

#### Deals
- `get_deal(deal_id)` - Get single deal
- `get_deals(filters, select, order, limit)` - Get multiple deals
- `update_deal(deal_id, fields)` - Update deal
- `delete_deal(deal_id)` - Delete deal
- `parse_deals(function)` - Parse all deals with custom function

#### Contacts
- `get_contact(contact_id)` - Get single contact
- `get_contacts(filters, select, order, limit)` - Get multiple contacts
- `update_contact(contact_id, fields)` - Update contact
- `delete_contact(contact_id)` - Delete contact
- `parse_contacts(function)` - Parse all contacts with custom function
- `get_phone_by_contact(contact_id)` - Extract phone number

#### Products
- `get_product(product_id)` - Get single product
- `get_products(filters, select, order, limit)` - Get multiple products
- `create_product(name, fields)` - Create new product
- `update_product(product_id, fields)` - Update product
- `delete_product(product_id)` - Delete product

### 🤖 Smart Processes
- `get_smart(entity_id, smart_id)` - Get single smart process item
- `get_smarts(entity_id, filters, select, order, limit)` - Get multiple items
- `update_smart(entity_id, smart_id, fields)` - Update smart process item
- `parse_smarts(function)` - Parse smart process items with custom function

### 👥 User Management
- `get_user(user_id)` - Get user information
- `get_users(filters)` - Get multiple users
- `update_user(user_id, user_data)` - Update user
- `get_user_name(user_id)` - Get formatted user name

### 📊 Status and Stage Management
- `get_statuses()` - Get lead statuses
- `get_sources()` - Get lead sources
- `get_stages(category_id)` - Get deal stages
- `get_deal_categories()` - Get deal categories
- `get_stage_history(entity_type, entity_id)` - Get status/stage change history

### 💬 Communication
- `get_openlines(entity_id, entity_type)` - Get open lines for entity
- `get_last_openline_id(entity_id, entity_type)` - Get last open line ID
- `transfer_openline(ol_id, user_id)` - Transfer open line to user
- `intercept_openline(ol_id)` - Intercept open line
- `get_openline_messages(openline_id, session_id)` - Get messages
- `notify_user(user_id, message)` - Send notification to user

### 📝 Comments and Timeline
- `add_comment(entity_id, entity_type, text)` - Add comment to entity
- `get_comments(entity_id, entity_type, select)` - Get entity comments

### 📞 Call Management
- `get_calls(filters, order, limit)` - Get call records

### ✅ Task Management
- `get_tasks(filters, select, order)` - Get tasks
- `add_task(title, created_by, responsible_id, extra_fields)` - Create task
- `delete_task(task_id)` - Delete task
- `parse_tasks(function)` - Parse all tasks with custom function

### 🏢 Department Management
- `get_department(dep_id)` - Get department info
- `get_all_departaments()` - Get all departments

### 🔧 Field Utilities
- `get_enumerated_field_values(entity_type, field_id)` - Get enum field options
- `extract_enumerated_field_value(entity_type, field_id, value)` - Extract enum value
- `extract_enumerated_smart_field_value(entity_id, field_id, value)` - Extract smart enum value

### 🔗 Utility Functions
- `create_crm_link(entity_type, entity_id)` - Generate CRM entity link
- `to_unix_time(datetime)` - Convert ISO datetime to Unix timestamp

## Advanced Usage

### Parsing Entities with Custom Functions

```python
def process_lead(lead):
    print(f"Processing lead {lead['ID']}: {lead['TITLE']}")
    if lead['STATUS_ID'] == 'CONVERTED':
        au_b24.update_lead(lead['ID'], {'STATUS_ID': 'PROCESSED'})

# Use the decorator to parse all leads
@au_b24.parse_leads
def my_lead_processor(lead):
    process_lead(lead)

# Execute parsing
my_lead_processor(
    filters={'STATUS_ID': 'NEW'},
    select=['ID', 'TITLE', 'STATUS_ID']
)
```

### Working with Smart Processes

```python
# Get smart process items
smarts = au_b24.get_smarts(
    entity_id=1234,  # Smart process type ID
    filters={'stageId': 'NEW'},
    select=['id', 'title', 'stageId']
)

# Update smart process item
au_b24.update_smart(1234, 5678, {'title': 'Updated Title'})
```

### Rate Limiting

```python
# Set pause between requests to avoid rate limits
au_b24.init_requests_pause(0.5)  # 500ms pause
```

### Exception Handling

```python
from au_b24 import StopParsing

@au_b24.parse_leads
def selective_processor(lead):
    if lead['ID'] > 1000:
        raise StopParsing()  # Stop processing
    # Process lead...

selective_processor(filters={}, select=['ID'])
```

## Error Handling

The library includes comprehensive error handling and logging. Set up logging to see detailed information:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

## Notes

- All `get_entities` functions provide only ID-based ordering
- Rate limiting is recommended to avoid API limits
- ID filtering in entity functions uses special operators (`>ID`, `<ID`)
- Smart processes support full ID filtering including comparison operators
- Some functions return `None` on error, others return `False` or empty lists

## Requirements

- Python 3.8+
- requests
- cachetools  
- python-dotenv

## License

MIT License