from django.shortcuts import render
from django.http import HttpResponse
import demoji
import random

demoji.download_codes()

emoji_categories = {
    '❤️': 'Love', '😊': 'Smile', '😎': 'Cool', '😂': 'Laugh', '🔥': 'Fire', '💡': 'Idea',
}
emoji_tips = [
    "Use ❤️ to express love.", "😊 is perfect for friendly conversations.",
    "😎 adds coolness!", "😂 means you're laughing hard!", "💡 is great for ideas.",
]

def get_history_stats(request):
    history = request.session.get("history", [])
    stats = request.session.get("emoji_stats", {})
    top_5 = sorted(stats.items(), key=lambda x: x[1], reverse=True)[:5]
    return history, top_5

def home_view(request):
    text = ''
    meanings = {}
    category_data = {}
    tip = random.choice(emoji_tips)

    if request.method == "POST":
        text = request.POST.get("emoji_input", "")
        meanings = demoji.findall(text)

        history = request.session.get("history", [])
        if text and text not in history:
            history.append(text)
        request.session["history"] = history

        stats = request.session.get("emoji_stats", {})
        for emoji in meanings.keys():
            stats[emoji] = stats.get(emoji, 0) + 1
        request.session["emoji_stats"] = stats

        for emoji in meanings:
            category_data[emoji] = emoji_categories.get(emoji, "General")

    return render(request, 'emoji_app/home.html', {
        'meanings': meanings,
        'text': text,
        'tip': tip,
        'categories': category_data,
        'background': 'emoji_app/bg-home.jpg'
    })

def history_view(request):
    history, _ = get_history_stats(request)
    return render(request, 'emoji_app/history.html', {
        'history': history,
        'background': 'emoji_app/bg-other.jpg'
    })

def top_view(request):
    _, top_5 = get_history_stats(request)
    return render(request, 'emoji_app/top.html', {
        'top_emojis': top_5,
        'background': 'emoji_app/bg-other.jpg'
    })

def about_view(request):
    return render(request, 'emoji_app/about.html', {
        'background': 'emoji_app/bg-other.jpg'
    })

def download_results(request):
    text = request.POST.get("emoji_text", "")
    results = demoji.findall(text)
    content = "\n".join([f"{emoji} — {meaning}" for emoji, meaning in results.items()])
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="emoji_results.txt"'
    return response
