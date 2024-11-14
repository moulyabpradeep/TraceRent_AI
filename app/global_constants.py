# global_constants.py

# All the constants in the Project will be placed here

# Define table names as constants
TENANT_PERSONAL_DETAILS_TABLE = 'tenant_personal_details'
TENANT_PREFERENCE_DETAILS_TABLE = 'tenant_preference_details'
TENANT_CATEGORY_TABLE = 'tenant_category'
PROPERTY_CATEGORY_TABLE = 'property_category'
TENANT_PREFERRED_PROPERTIES_TABLE = 'tenant_preferred_properties'
PROPERTY_DATA_TABLE = 'property_data'
USER_TABLE = 'user'
TENANT_ACTIONS_TABLE = 'tenant_actions'

# Define column names as constants (keep them here for easy access)
PROP_CAT_ID_COLUMN = 'prop_cat_id'
TENT_CAT_ID_COLUMN = 'tent_cat_id'
# Add other column constants as needed

# Configurable interval (in days)
DAYS_THRESHOLD = 7

# Constants for API responses
GENERAL_ERROR_MSG = "An error occurred. Please try again."
INVALID_PASSWORD_MSG = "Invalid password entry"
USER_NOT_FOUND_MSG = "User not found"
PASSWORD_INCORRECT_MSG = "Incorrect password"
USER_FOUND_MSG = "User found successfully"
PREFERENCES_SAVE_SUCCESS = "Preferences saved successfully!"
PREFERENCES_SAVE_FAILURE = "Failed to save preferences."
INVALID_EMAIL_MSG = "Invalid input for email."
USER_EXISTS_MSG = "User already exists."
USER_SIGNUP_SUCCESS_MSG = "User saved successfully."
NO_DATA_MSG = "No data received in the request."
PROPERTIES_FETCH_SUCCESS_MSG = "Properties fetched successfully."
PROPERTIES_FETCH_FAILURE_MSG = "No properties fetched"
LIKED_FILTER = "LIKED"
DISLIKED_FILTER = "DISLIKED"
VIEWED_FILTER = "VIEWED"
CONTACTED_FILTER = "CONTACTED"
PRICE_RANGE_FETCH_SUCCESS_MSG = "Price range fetched successfully"
PRICE_RANGE_FETCH_FAILURE_MSG = "Unable to fetch price range"