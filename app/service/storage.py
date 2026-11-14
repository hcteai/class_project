notes = {}
next_id = 1


def add_note(title, content):
    global next_id
    note = {"id": next_id, "title": title, "content": content, "views": 0}
    notes[next_id] = note
    next_id += 1
    return note


def get_note(note_id):
    return notes.get(note_id)


def get_all_notes():
    return list(notes.values())


def delete_note(note_id):
    if note_id in notes:
        notes.pop(note_id)
        return True
    return False
