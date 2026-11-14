import storage

MAX_CONTENT_LENGTH = 100


def create_note(title, content=""):
    """Create a note. Title is required, content max 100 characters."""
    check_fields(title, content)
    return storage.add_note(title.strip(), content)


def get_all_notes():
    return storage.get_all_notes()


def view_note(note_id):
    """Return a note and add one to its view count."""
    note = find_note(note_id)
    note["views"] += 1
    return note


def edit_note(note_id, title=None, content=None):
    """Change title and/or content. Pass None to keep a value unchanged."""
    note = find_note(note_id)

    new_title = note["title"] if title is None else title
    new_content = note["content"] if content is None else content
    check_fields(new_title, new_content)

    note["title"] = new_title.strip()
    note["content"] = new_content
    return note


def delete_note(note_id):
    if not storage.delete_note(note_id):
        raise ValueError(f"Note {note_id} not found.")


def find_note(note_id):
    note = storage.get_note(note_id)
    if note is None:
        raise ValueError(f"Note {note_id} not found.")
    return note


def check_fields(title, content):
    if not title or not title.strip():
        raise ValueError("Title is required.")
    if len(content) > MAX_CONTENT_LENGTH:
        raise ValueError(f"Content must be at most {MAX_CONTENT_LENGTH} characters.")
