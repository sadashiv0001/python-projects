import requests

def get_linkedin_info(linkedin_url, access_token):
    member_id = linkedin_url.split("/")[-1]
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Connection': 'Keep-Alive',
    }

    api_url = f'https://api.linkedin.com/v2/people/{member_id}?projection=(id,firstName,lastName,positions)'
    
    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            
            first_name = data.get('firstName', '')
            last_name = data.get('lastName', '')
            
            positions = data.get('positions', {}).get('values', [])
            company = positions[0]['company']['name'] if positions else 'Company not found'

            full_name = f"{first_name} {last_name}"

            return full_name, company
        else:
            print(f"Failed to retrieve LinkedIn profile. Status code: {response.status_code}")
            return None, None

    except Exception as e:
        print(f"Error: {e}")
        return None, None

# Example usage
linkedin_url = 'LINKEDIN_URL'
access_token = 'YOUR ACCESS_TOKEN'  # Replace with your actual access token

name, company = get_linkedin_info(linkedin_url, access_token)

print(f"Name: {name}")
print(f"Company: {company}")

    