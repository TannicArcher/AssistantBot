import requests


def get_new_temp_mail(domain):
    url = "https://temporary-mail-afeg-ru.p.rapidapi.com/api/create"
    querystring = {"domain": f"{domain}"}
    headers = {
        'x-rapidapi-key': "eaf8ab0103mshd0bd6e48a652cdap1b0779jsn8ee624a39294",
        'x-rapidapi-host': "temporary-mail-afeg-ru.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


def get_messages(email):
    url = "https://temporary-mail-afeg-ru.p.rapidapi.com/api/fetch"
    querystring = {"email": f"{email}"}
    headers = {
        'x-rapidapi-key': "eaf8ab0103mshd0bd6e48a652cdap1b0779jsn8ee624a39294",
        'x-rapidapi-host': "temporary-mail-afeg-ru.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


def get_domains():
    url = "https://temporary-mail-afeg-ru.p.rapidapi.com/api/domains"
    headers = {
        'x-rapidapi-key': "eaf8ab0103mshd0bd6e48a652cdap1b0779jsn8ee624a39294",
        'x-rapidapi-host': "temporary-mail-afeg-ru.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    return response.text
