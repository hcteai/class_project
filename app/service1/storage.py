from models import Note, Group


class NoteStorage:
    def __init__(self):
        self._notes = {}
        self._next_id = 1

    def add(self, title, content):
        note = Note(self._next_id, title, content)
        self._notes[note.id] = note
        self._next_id += 1
        return note

    def get(self, note_id):
        return self._notes.get(note_id)

    def get_all(self):
        return list(self._notes.values())

    def delete(self, note_id):
        return self._notes.pop(note_id, None) is not None


class GroupStorage:
    def __init__(self):
        self._groups = {}
        self._next_id = 1

    def add(self, name):
        group = Group(self._next_id, name)
        self._groups[group.id] = group
        self._next_id += 1
        return group

    def get(self, group_id):
        return self._groups.get(group_id)

    def get_all(self):
        return list(self._groups.values())

    def delete(self, group_id):
        return self._groups.pop(group_id, None) is not None
