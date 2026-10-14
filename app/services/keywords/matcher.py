import re


def normilize_text(text: str) -> str:
    text = text.lower()
    text = text.replace("ё", "е")

    return text


def find_keywords(
        text: str,
        keywords: list[str],
) -> list[str]:
    text = normilize_text(text)

    found = []

    for keyword in keywords:
        keyword = normilize_text(keyword)

        pattern = rf"\b{re.escape(keyword)}"

        if re.search(pattern, text, flags=re.U):
            found.append(keyword)

    return found
