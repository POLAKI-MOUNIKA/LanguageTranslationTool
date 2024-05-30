from django.shortcuts import render
from googletrans import Translator
from .forms import TranslationForm
from .models import Translation

def translate_view(request):
    translation = ''
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            source_language = form.cleaned_data['source_language']
            dest_language = form.cleaned_data['dest_language']
            translator = Translator()
            translated_text = translator.translate(text, src=source_language, dest=dest_language).text

            # Save translation to the database
            Translation.objects.create(
                text=text,
                translated_text=translated_text,
                source_language=source_language,
                dest_language=dest_language
            )

            translation = translated_text
    else:
        form = TranslationForm()

    return render(request, 'translator/translate.html', {'form': form, 'translation': translation})