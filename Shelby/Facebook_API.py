#Convert user token to page token
import requests

page_id ="796678578393219"
f_access_token="EAAJY4xlZCWQkBAPCQ2nTXwSixDZAY2EEM6VbxL0j1fZAmto8ZClzQr7LN8xUITUItYFKD4603ZCZCbaMv1e7IZAjSoQA2FwSlMDEkC6L13phDUQTZAf7ZA14jZBT2ZAI1EHq4Y9b9nXrWCeXDMYs9ard1bplMKQTnuf2L9yZAE2AUXVfwAZDZD"

r=requests.get(f"https://graph.facebook.com/{page_id}?fields=access_token={f_access_token}")

print(r.json())