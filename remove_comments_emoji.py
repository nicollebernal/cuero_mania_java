import pathlib, re
emoji_pattern = re.compile(
    "[\U0001F600-\U0001F64F" \
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\U0001F900-\U0001F9FF"
    "\U0001FA70-\U0001FAFF"
    "\U0000200D"
    "\U0000FE0F"
    "]+", re.UNICODE)
comment_pattern = re.compile(r"<!--.*?-->", re.S)
root = pathlib.Path('web')
for path in root.rglob('*.xhtml'):
    text = path.read_text(encoding='utf-8')
    new_text = comment_pattern.sub('', text)
    new_text = emoji_pattern.sub('', new_text)
    if new_text != text:
        new_text = re.sub(r'\n{3,}', '\n\n', new_text)
        path.write_text(new_text, encoding='utf-8')
