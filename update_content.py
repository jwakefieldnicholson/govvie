import json
import os
import requests
from datetime import datetime
import random

# API Configuration
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")  # Get from environment variable
API_URL = "https://api.anthropic.com/v1/messages"

# Headers for API request
headers = {
    "Content-Type": "application/json",
    "X-API-Key": ANTHROPIC_API_KEY,
    "anthropic-version": "2023-06-01"
}

# List of departments
departments = [
    "Department of State",
    "Department of the Treasury",
    "Department of Defense",
    "Department of Justice",
    "Department of the Interior",
    "Department of Agriculture",
    "Department of Commerce",
    "Department of Labor",
    "Department of Health and Human Services",
    "Department of Housing and Urban Development",
    "Department of Transportation",
    "Department of Energy",
    "Department of Education",
    "Department of Veterans Affairs",
    "Department of Homeland Security",
    "Environmental Protection Agency",
    "Federal Communications Commission",
    "Securities and Exchange Commission",
    "National Aeronautics and Space Administration",
    "Federal Trade Commission",
    "Small Business Administration",
    "Nuclear Regulatory Commission",
    "Federal Reserve System",
    "Consumer Financial Protection Bureau",
    "National Science Foundation"
]

# Department-specific context to make content relevant to each department
department_contexts = {
    "Department of State": "international relations, diplomacy, foreign policy",
    "Department of the Treasury": "financial systems, currency, taxation, economic policy",
    "Department of Defense": "military operations, defense contracts, security",
    "Department of Justice": "legal proceedings, investigations, regulations",
    "Department of the Interior": "public lands, natural resources, conservation",
    "Department of Agriculture": "farming, food production, rural development",
    "Department of Commerce": "business, trade, economic growth",
    "Department of Labor": "employment, workforce, labor conditions",
    "Department of Health and Human Services": "healthcare, public health, medical research",
    "Department of Housing and Urban Development": "housing, urban planning, community development",
    "Department of Transportation": "transportation systems, infrastructure, traffic",
    "Department of Energy": "energy production, power systems, energy research",
    "Department of Education": "education systems, schools, learning initiatives",
    "Department of Veterans Affairs": "veteran benefits, healthcare for veterans",
    "Department of Homeland Security": "national security, emergency management",
    "Environmental Protection Agency": "environmental protection, pollution, climate",
    "Federal Communications Commission": "telecommunications, internet, broadcasting",
    "Securities and Exchange Commission": "financial markets, investments, securities",
    "National Aeronautics and Space Administration": "space exploration, aeronautics, research",
    "Federal Trade Commission": "consumer protection, competition, business practices",
    "Small Business Administration": "small businesses, entrepreneurship, startups",
    "Nuclear Regulatory Commission": "nuclear energy, radiation safety",
    "Federal Reserve System": "monetary policy, banking system, interest rates",
    "Consumer Financial Protection Bureau": "consumer financial products, loans, credit",
    "National Science Foundation": "scientific research, funding, innovation"
}

# Function to generate bulletins for a specific department
def generate_bulletins(department):
    # Create a prompt specific to the department
    prompt = f"""You are an official government content writer for the {department}. 
    
Write 5 serious-sounding bullet points about the {department}'s latest initiatives or policies. 
Each bullet point should:
1. Sound completely professional and bureaucratic with technical jargon
2. Subtly troll Elon Musk without mentioning him by name
3. Be related to {department_contexts.get(department, 'government operations')}
4. Use proper government terminology and formal language
5. Include absurd specifics that sound plausible but are slightly ridiculous
6. Include at least one precise but meaningless statistic or measurement
7. Use unnecessarily complex acronyms that sound official

Examples of subtle trolling might reference: 
- Overpromised deadlines that keep moving
- Mars colonization feasibility studies
- Underground transportation systems that lead nowhere
- Erratic social media behavior affecting markets
- Securities violations through tweet-based market manipulation
- Workplace conditions in manufacturing facilities
- Impossible technical promises about AI or autonomous systems
- Regulatory frameworks for flamethrowers sold as "not flamethrowers"
- Tunneling projects with implausible timelines
- Space debris from privately launched vehicles
- Mandatory timeframes for promised features that never arrive

Just provide the 5 bullet points with no introduction or other text. Each bullet point should start with a hyphen and be on a new line."""

    # Prepare the API request payload
    payload = {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 1000,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    # Make the API request
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Extract the bulletins from the response
        bulletins_text = response.json()["content"][0]["text"]
        
        # Process the bulletins (remove hyphens, strip whitespace)
        bulletins = [item.strip()[2:].strip() if item.strip().startswith('-') else item.strip() 
                   for item in bulletins_text.split('\n') if item.strip()]
        
        # Ensure we have exactly 5 bulletins
        while len(bulletins) < 5:
            bulletins.append("Further updates will be provided as information becomes available.")
        
        return bulletins[:5]  # Return only 5 bulletins even if more were generated
        
    except Exception as e:
        print(f"Error generating bulletins for {department}: {e}")
        # Return fallback content in case of API failure
        return [
            f"The {department} is currently reviewing its communication protocols.",
            f"Recent developments have prompted a thorough assessment of our operational guidelines.",
            f"Our department continues to monitor situations that may affect policy implementations.",
            f"Stakeholders are advised to consult the department website for the most up-to-date information.",
            f"The {department} remains committed to transparency and accountability in all proceedings."
        ]

# Function to update the content JSON file
def update_content():
    # Load existing content if it exists
    try:
        with open("content.json", "r") as f:
            content = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Create a new content structure if the file doesn't exist or is invalid
        content = {"departments": {}, "last_updated": ""}

    # Update the last updated timestamp
    content["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    
    # Update content for each department
    for department in departments:
        print(f"Generating content for {department}...")
        bulletins = generate_bulletins(department)
        
        content["departments"][department] = {
            "bulletins": bulletins
        }
    
    # Save the updated content back to the file
    with open("content.json", "w") as f:
        json.dump(content, f, indent=2)
    
    print(f"Content updated successfully on {content['last_updated']}")

if __name__ == "__main__":
    if not ANTHROPIC_API_KEY:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
    else:
        update_content()
