class Note:
    def __init__(self, note_id, title, content=""):
        self.id = note_id
        self.title = title
        self.content = content
        self.views = 0

    def add_view(self):
        self.views += 1

    def __repr__(self):
        return f"Note(id={self.id}, title={self.title!r}, views={self.views})"


class Group:
    def __init__(self, group_id, name):
        self.id = group_id
        self.name = name
        self.note_ids = set()

    def has_note(self, note_id):
        return note_id in self.note_ids

    def add_note(self, note_id):
        """Return True if added, False if it was already in the group."""
        if note_id in self.note_ids:
            return False
        self.note_ids.add(note_id)
        return True

    def remove_note(self, note_id):
        """Return True if removed, False if it was not in the group."""
        if note_id not in self.note_ids:
            return False
        self.note_ids.remove(note_id)
        return True

    def __repr__(self):
        return f"Group(id={self.id}, name={self.name!r}, notes={sorted(self.note_ids)})"
