# Convert user token to page token
import requests

page_id = "106479581966092"
f_access_token = "EAAJY4xlZCWQkBAIJMwMlSEq8LW8sC8U9yzxZCrMfLKgZByZBkJhIGOUtq1kN8CJWDoZBcY1andA7PNYJ62uZAOZB8oinemuGOoNpyAxg6cew02emH6c9qgR1M9wC0U2RCNNsnYpzlFTa0kDADTLDohpZC9DQ3JinFlNmdOTN5ApTOwZDZD"

r = requests.get(
    f"https://graph.facebook.com/{page_id}?fields=access_token={f_access_token}")

print(r.json())
