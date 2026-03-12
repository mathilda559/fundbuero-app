import os
from supabase import create_client

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

def save_item(titel, kategorie, bild_url):

    data = {
        "titel": titel,
        "kategorie": kategorie,
        "bild_url": bild_url
    }

    supabase.table("fundstuecke").insert(data).execute()


def load_items():

    response = supabase.table("fundstuecke").select("*").execute()

    return response.data
