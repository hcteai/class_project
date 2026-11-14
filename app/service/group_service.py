import storage

MAX_GROUP_NAME_LENGTH = 50


def create_group(name):
    """Create a uniquely named group for notes."""
    check_group_name(name)
    normalized_name = name.strip()
    if any(group["name"] == normalized_name for group in storage.get_all_groups()):
        raise ValueError(f"Group '{normalized_name}' already exists.")
    return storage.add_group(normalized_name)


def get_all_groups():
    return storage.get_all_groups()


def find_group(group_id):
    group = storage.get_group(group_id)
    if group is None:
        raise ValueError(f"Group {group_id} not found.")
    return group


def delete_group(group_id):
    if not storage.delete_group(group_id):
        raise ValueError(f"Group {group_id} not found.")


def add_note(group_id, note_id):
    find_group(group_id)
    if storage.get_note(note_id) is None:
        raise ValueError(f"Note {note_id} not found.")
    if not storage.add_note_to_group(group_id, note_id):
        raise ValueError(f"Note {note_id} is already in group {group_id}.")
    return storage.get_group(group_id)


def remove_note(group_id, note_id):
    find_group(group_id)
    if not storage.remove_note_from_group(group_id, note_id):
        raise ValueError(f"Note {note_id} is not in group {group_id}.")
    return storage.get_group(group_id)


def get_group_notes(group_id):
    find_group(group_id)
    return storage.get_group_notes(group_id)


def check_group_name(name):
    if not name or not name.strip():
        raise ValueError("Group name is required.")
    if len(name.strip()) > MAX_GROUP_NAME_LENGTH:
        raise ValueError(
            f"Group name must be at most {MAX_GROUP_NAME_LENGTH} characters."
        )
