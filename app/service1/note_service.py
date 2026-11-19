class NoteService:
    MAX_CONTENT_LENGTH = 100

    def __init__(self, note_storage):
        self._storage = note_storage

    def create_note(self, title, content=""):
        """Create a note. Title is required, content max 100 characters."""
        self._check_fields(title, content)
        return self._storage.add(title.strip(), content)

    def get_all_notes(self):
        return self._storage.get_all()

    def view_note(self, note_id):
        """Return a note and add one to its view count."""
        note = self.find_note(note_id)
        note.add_view()
        return note

    def edit_note(self, note_id, title=None, content=None):
        """Change title and/or content. Pass None to keep a value unchanged."""
        note = self.find_note(note_id)

        new_title = note.title if title is None else title
        new_content = note.content if content is None else content
        self._check_fields(new_title, new_content)

        note.title = new_title.strip()
        note.content = new_content
        return note

    def delete_note(self, note_id):
        if not self._storage.delete(note_id):
            raise ValueError(f"Note {note_id} not found.")

    def find_note(self, note_id):
        note = self._storage.get(note_id)
        if note is None:
            raise ValueError(f"Note {note_id} not found.")
        return note

    def _check_fields(self, title, content):
        if not title or not title.strip():
            raise ValueError("Title is required.")
        if len(content) > self.MAX_CONTENT_LENGTH:
            raise ValueError(
                f"Content must be at most {self.MAX_CONTENT_LENGTH} characters."
            )
