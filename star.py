def add_recommendation(result):

    def stars(score):

        full = int(score // 20)

        half = (score % 20) >= 10

        text = "⭐" * full

        if half:
            text += "✨"

        empty = 5 - full - half

        text += "☆" * empty

        return f"{text}\n{score:.0f}%"

    result["Recommendation"] = result["Compatibility"].apply(stars)

    return result