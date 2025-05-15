def setup_pubcrank(settings, pubdir, theme):
  settings['PUBCRANK_DIR'] = pubdir
  settings['PUBCRANK_THEME'] = theme
  settings['TEMPLATES'].append({
    'NAME': 'pubcrank',
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [pubdir / 'themes'],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
  })
