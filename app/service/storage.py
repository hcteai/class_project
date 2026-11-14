notes = {}
groups = {}
next_id = 1
next_group_id = 1


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


def add_group(name):
    global next_group_id
    group = {"id": next_group_id, "name": name, "note_ids": set()}
    groups[next_group_id] = group
    next_group_id += 1
    return group


def get_group(group_id):
    return groups.get(group_id)


def get_all_groups():
    return list(groups.values())


def delete_group(group_id):
    if group_id in groups:
        groups.pop(group_id)
        return True
    return False


def add_note_to_group(group_id, note_id):
    group = groups.get(group_id)
    if group is None or note_id not in notes or note_id in group["note_ids"]:
        return False
    group["note_ids"].add(note_id)
    return True


def remove_note_from_group(group_id, note_id):
    group = groups.get(group_id)
    if group is None or note_id not in group["note_ids"]:
        return False
    group["note_ids"].remove(note_id)
    return True


def get_group_notes(group_id):
    group = groups.get(group_id)
    if group is None:
        return None
    return [notes[note_id] for note_id in group["note_ids"] if note_id in notes]
