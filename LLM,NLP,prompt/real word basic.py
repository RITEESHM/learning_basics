#conversion of text to json
import re
import json

text = """Birthday gift for my 140 months old son"""

# Define patterns to extract gender, occasion, and age
gender_patterns = r'\b(?:son|daughter)\b'
occasion_patterns = r'\b(?:party|birthday|anniversary)\b'
age_patterns = r'\b(\d+)\s*(?:months|years)\b'

# Extract gender
gender_match = re.search(gender_patterns, text, flags=re.IGNORECASE)
gender = "female" if gender_match and "daughter" in gender_match.group().lower() else "male"

# Extract occasion
occasion_match = re.search(occasion_patterns, text, flags=re.IGNORECASE)
occasion = occasion_match.group().lower() if occasion_match else None

# Extract age
age_match = re.search(age_patterns, text, flags=re.IGNORECASE)
age_years = int(age_match.group(1)) / 12 if age_match else None

# Construct JSON object
result = {
    "gender": gender,
    "occasion": occasion,
    "age_years": age_years
}

# Print the JSON object
print(json.dumps(result, indent=4))
