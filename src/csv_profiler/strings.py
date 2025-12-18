def slugify(text: str) -> str:
    """
    Turn 'Report Name' -> 'report-name'
    """
    text = text.lower()       
    
    for value  in "0123456789":
     text = text.replace(value, "")

    text = text.replace(" ", "-")  
    return text
